import tushare as ts
import os
from technology.src.StockIndexDatasManager import StockIndexDatasManager
from technology.src.StockDatasManager import StockDatasManager
from technology.src.decision_department.StockAnalyst import StockAnalyst
from technology.auxiliary_lib.ConfigLoader import ConfigLoader

'''
    主服务入口
'''


class StockService(object):
    mPro = None
    __instance = None
    mIndexDataGetter = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.mPro = ts.pro_api(token='797e877a9b26ec820adc5ef5e093e83ab9b2814fbe7f458ddfa887b4')

    '''
        开启主服务
    '''

    def startService(self):
        if ConfigLoader().get("stocks", "use_analysis_engine") == '0':  # 仅获取数据
            self.startDataCollection()
        elif ConfigLoader().get("stocks", "use_analysis_engine") == '1':  # 获取数据，并进行技术分析
            self.startDataCollection()
            self.startDataAnalysis()
        elif ConfigLoader().get("stocks", "use_analysis_engine") == '2':  # 仅进行技术分析
            # 提取带有历史数据文件的所有股票
            files = os.listdir("../datas/股票数据")
            code_list_cfg = ConfigLoader().get("stocks", "code_list")
            code_list = code_list_cfg.split(",")
            monitor_code_list = ConfigLoader().get("stocks", "monitor_code_list").split(",")  #获取需要监控的股票数据
            code_list = code_list_cfg
            print("len: ", len(code_list_cfg))
            for file in files:
                file = file.split('.xlsx')[0]
                code = file[0:6]
                if code_list_cfg and code not in code_list and code not in monitor_code_list:  #检查获取的股票数据是否是在指定的列表中
                    continue
                name = file[6::]
                StockAnalyst().setCode2Name(code, name)  #设置code->name映射
            self.startDataAnalysis()
        else:
            print('错误的分析标识：[use_analysis_engine]')

    '''
        开始获取基础数据
    '''

    def startDataCollection(self):
#        self.getStockIndexDatas()  # 获取指数数据
        self.getStockDatas()  # 获取股票数据

    '''
        获取指数基础日K数据
    '''

    def getStockIndexDatas(self):
        mIndexDataManager = StockIndexDatasManager()
        mIndexDataManager.setPro(self.mPro)
        mIndexDataManager.getAllIndexDaily()

    '''
        获取股票基础信息、日K数据
    '''

    def getStockDatas(self):
        mStockDatasManager = StockDatasManager()
        mStockDatasManager.setPro(self.mPro)
        mStockDatasManager.getAllStockInfoPro()  # 从中获取A股代码
        mStockDatasManager.getAllStockHistoryDatas()  # 获取所有A股的历史数据

    '''
        开始进行股票数据分析
            - 技术指标分析
            - ML预测
    '''

    def startDataAnalysis(self):
        df_default, df_purchased, df_monitor = StockAnalyst().startAnalysisKLineForm()
        df_default.to_excel("../datas/1_执行结果.xlsx", sheet_name='执行结果', index=False)
        df_purchased.to_excel("../datas/2_已买股票执行结果.xlsx", sheet_name='执行结果', index=False)
        df_monitor.to_excel("../datas/3_监控的股票执行结果.xlsx", sheet_name='执行结果', index=False)
        pass
