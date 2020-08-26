
from pandas import DataFrame

'''
    英文-->中文转换器
'''
class NounsEng2Chn(object):
    __instance = None
    mDataAllIndexInfo = {}                  # 所有交易指数的基本数据       英文--中文对照关系
    mDataSpecIndexInfo = {}                 # 特定交易指数的基本数据       英文--中文对照关系
    mDataTradingDaysMap = {}                # 记录A股当前交易日数据        英文--中文对照关系
    mDataSpecStockHistory = {}              # 记录特定股票的历史性数据     英文--中文对照关系
    mDataCompanyBasicInfo = {}              # 记录上市公司的基本情况       英文--中文对照关系

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        # get_index（）所有交易指数基本信息列
        self.mDataAllIndexInfo["code"] = "指数代码"
        self.mDataAllIndexInfo["name"] = "指数名称"
        self.mDataAllIndexInfo["change"] = "涨跌幅"
        self.mDataAllIndexInfo["open"] = "开盘价"
        self.mDataAllIndexInfo["preclose"] = "昨日收盘价"
        self.mDataAllIndexInfo["close"] = "收盘价"
        self.mDataAllIndexInfo["high"] = "最高价"
        self.mDataAllIndexInfo["low"] = "最低价"
        self.mDataAllIndexInfo["volume"] = "成交量(手)"
        self.mDataAllIndexInfo["amount"] = "成交金额（亿元）"

        # index_basic()特定交易指数基本信息列
        self.mDataSpecIndexInfo["ts_code"] = "TS代码"
        self.mDataSpecIndexInfo["name"] = "简称"
        self.mDataSpecIndexInfo["fullname"] = "指数全称"
        self.mDataSpecIndexInfo["market"] = "市场"
        self.mDataSpecIndexInfo["publisher"] = "发布方"
        self.mDataSpecIndexInfo["index_type"] = "指数风格"
        self.mDataSpecIndexInfo["category"] = "指数类别"
        self.mDataSpecIndexInfo["base_date"] = "基期"
        self.mDataSpecIndexInfo["base_point"] = "基点"
        self.mDataSpecIndexInfo["list_date"] = "发布日期"
        self.mDataSpecIndexInfo["weight_rule"] = "加权方式"
        self.mDataSpecIndexInfo["desc"] = "描述"
        self.mDataSpecIndexInfo["exp_date"] = "终止日期"

        # get_today_all()股票实时数据列
        self.mDataTradingDaysMap["code"] = "代码"
        self.mDataTradingDaysMap["name"] = "名称"
        self.mDataTradingDaysMap["changepercent"] = "涨跌幅（%）"
        self.mDataTradingDaysMap["trade"] = "现价（元）"
        self.mDataTradingDaysMap["open"] = "开盘价（元）"
        self.mDataTradingDaysMap["close"] = "收盘价（元）"
        self.mDataTradingDaysMap["high"] = "最高价（元）"
        self.mDataTradingDaysMap["low"] = "最低价（元）"
        self.mDataTradingDaysMap["settlement"] = "昨日收盘价（元）"
        self.mDataTradingDaysMap["volume"] = "成交量（股）"
        self.mDataTradingDaysMap["turnoverratio"] = "换手率（%）"
        self.mDataTradingDaysMap["amount"] = "成交额"
        self.mDataTradingDaysMap["per"] = "市盈率"
        self.mDataTradingDaysMap["pb"] = "市净率"
        self.mDataTradingDaysMap["mktcap"] = "总市值（万）"
        self.mDataTradingDaysMap["nmc"] = "流通市值（万）"

        # get_hist_data()特定股票历史数据列
        self.mDataSpecStockHistory["date"] = "日期"
        self.mDataSpecStockHistory["open"] = "开盘价"
        self.mDataSpecStockHistory["high"] = "最高价"
        self.mDataSpecStockHistory["close"] = "收盘价"
        self.mDataSpecStockHistory["low"] = "最低价"
        self.mDataSpecStockHistory["volume"] = "成交量（手）"
        self.mDataSpecStockHistory["price_change"] = "价格变动"
        self.mDataSpecStockHistory["p_change"] = "涨跌幅（%）"
        self.mDataSpecStockHistory["ma5"] = "5日均价"
        self.mDataSpecStockHistory["ma10"] = "10日均价"
        self.mDataSpecStockHistory["ma20"] = "20日均价"
        self.mDataSpecStockHistory["v_ma5"] = "5日均量"
        self.mDataSpecStockHistory["v_ma10"] = "10日均量"
        self.mDataSpecStockHistory["v_ma20"] = "20日均量"
        self.mDataSpecStockHistory["turnover"] = "换手率（%）"

        # get_stock_basics()股票基本面信息列
        self.mDataCompanyBasicInfo["code"] = "代码"
        self.mDataCompanyBasicInfo["name"] = "名称"
        self.mDataCompanyBasicInfo["industry"] = "细分行业"
        self.mDataCompanyBasicInfo["area"] = "地区"
        self.mDataCompanyBasicInfo["pe"] = "市盈率"
        self.mDataCompanyBasicInfo["outstanding"] = "流通股本"
        self.mDataCompanyBasicInfo["totals"] = "总股本(万)"
        self.mDataCompanyBasicInfo["totalAssets"] = "总资产(万)"
        self.mDataCompanyBasicInfo["liquidAssets"] = "流动资产"
        self.mDataCompanyBasicInfo["fixedAssets"] = "固定资产"
        self.mDataCompanyBasicInfo["reserved"] = "公积金"
        self.mDataCompanyBasicInfo["reservedPerShare"] = "每股公积金"
        self.mDataCompanyBasicInfo["esp"] = "每股收益"
        self.mDataCompanyBasicInfo["bvps"] = "每股净资"
        self.mDataCompanyBasicInfo["pb"] = "市净率"
        self.mDataCompanyBasicInfo["timeToMarket"] = "上市日期"
        self.mDataCompanyBasicInfo["undp"] = "未分利润"
        self.mDataCompanyBasicInfo["perundp"] = "每股未分配"
        self.mDataCompanyBasicInfo["rev"] = "收入同比(%)"
        self.mDataCompanyBasicInfo["profit"] = "毛利率(%)"
        self.mDataCompanyBasicInfo["npr"] = "净利润率(%)"
        self.mDataCompanyBasicInfo["holders"] = "股东人数"

    def converseEng2Chn(self, df:DataFrame, name_dic:dict):
        for name in list(df.columns):
            if name in name_dic:
                df.rename(columns={name: name_dic[name]}, inplace=True)  # 修改列名
        return df

