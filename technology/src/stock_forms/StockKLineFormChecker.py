
from pandas import DataFrame
from src.stock_forms.SingleKLineFormChecker import SingleKLineFormChecker
from src.stock_forms.DoubleKLineFormChecker import DoubleKLineFormChecker
from src.stock_forms.MultipleKLineFormChecker import MultipleKLineFormChecker

'''
    - 单例模式
    - 股票形态检测器
    - 股票形态检测标准：
    （1） 反转形态：
        - 检测近期的均线趋势（判断上涨或下跌行情）
        - 检测当日或（最多近3日）的K线组合形态是否存在反转形态
    （2） 持续形态：
        - 检测近期的均线趋势（判断上涨或下跌行情）
        - 检测当日或（最近3日）的K线组合形态是否存在持续形态
    （3） 十字星形态：
        - 当日是否以十字星收盘
        - 如果是以十字星收盘，则判断是否存在跳空、启明星、黄昏星等强烈反转信号
    （4） 判别形态主要以价格参数为依据，因此可分为：
        - 单日价格形态判别（只需要当前交易日的价格数据即可）
        - 两日价格形态判别（需要当前交易日和上一个交易日的价格数据）
        - 三日价格形态判别（需要当前交易日和上两个交易日的价格数据）
'''
class StockKLineFormChecker(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    '''
        单K线形态检测
    '''
    def checkSingleKLineForm(self, date:str, day:list):
        resStr = ""
        if SingleKLineFormChecker().hammerWire(day):
            resStr += date + " 锤子线\n"
        return resStr

    '''
        双K线形态检测
    '''
    def checkDoubleKLineForm(self, date:str, dayOne: list, dayTwo: list):
        resStr = ""
        if DoubleKLineFormChecker().engulfingForm(dayOne, dayTwo):
            resStr += date + "吞没形态\n"
        if DoubleKLineFormChecker().darkCloudCover(dayOne, dayTwo):
            resStr += date + "乌云盖顶\n"
        if DoubleKLineFormChecker().piercingForm(dayOne, dayTwo):
            resStr += date + "刺透形态\n"
        return resStr

    '''
        多K线形态检测
    '''
    def checkMultipleKLineForm(self, date:str, dayOne:list, dayTwo:list, dayThree:list):
        resStr = ""
        if MultipleKLineFormChecker().venusForm(dayOne, dayTwo, dayThree):
            resStr = date + "启明星形态\n"
        if MultipleKLineFormChecker().eveningStarForm(dayOne, dayTwo, dayThree):
            resStr = date + "黄昏星形态\n"
        if MultipleKLineFormChecker().crossVenusForm(dayOne, dayTwo, dayThree):
            resStr = date + "十字启明星形态\n"
        if  MultipleKLineFormChecker().crossEveningStarForm(dayOne, dayTwo, dayThree):
            resStr = date + "十字黄昏星\n"
        return resStr

########################################################################################################################

def oneDayAnalysisIndicators(df: DataFrame):
    resResult = ""
    for i in range(0, len(df)):
        line_lst = list(df.iloc[i])
        date, open, high, close, low = line_lst[0:5]
        day = [open, high, close, low]
        resResult += StockKLineFormChecker().checkSingleKLineForm(date, day)
    return resResult

def twoDayAnalysisIndicators(df: DataFrame):
    resResult = ""
    for i in range(0, len(df)-1):
        dayOne = list(df.iloc[i + 1])
        dayTwo = list(df.iloc[i])
        date = dayOne[0]
        resResult += StockKLineFormChecker().checkDoubleKLineForm(date, dayOne, dayTwo)
    return resResult


def threeDayAnalysisIndicators(df: DataFrame):
    resResult = ""
    for i in range(0, len(df)-2):
        dayOne = list(df.iloc[i + 2])
        dayTwo = list(df.iloc[i + 1])
        dayThree = list(df.iloc[i])
        date = dayTwo[0]
        resResult += StockKLineFormChecker().checkMultipleKLineForm(date, dayOne, dayTwo, dayThree)
    return resResult

if __name__ == '__main__':
    import pandas as pd
    stockMap = {
        "000524": "岭南控股",
        "002108": "沧州明珠",
        "002138": "顺络电子",
        "002407": "多氟多",
        "002625": "光启技术",
        "600776": "东方通信",
        "603703": "盛洋科技",
        "603869": "新智认知",
        "600988": "赤峰黄金"
    }

    for id in stockMap.keys():
        df = pd.read_excel('../../datas/股票数据/' + id + stockMap[id] + '.xlsx', sheet_name='历史日K数据', parse_dates=True)
        print('-----------------------------: ' + id + stockMap[id])
        oneDay_res = oneDayAnalysisIndicators(df)
        twoDay_res = twoDayAnalysisIndicators(df)
        threeDay_res = threeDayAnalysisIndicators(df)
        print("一天: " + oneDay_res)
        print("二天: " + twoDay_res)
        print("三天: " + threeDay_res)
        print('===========================================\n')