# stock_analysis
python 股票分析工具

# 股票分析
- 股票投资的分析方法主要有3种：基本分析、技术分析、演化分析
- 基本分析主要应用于投资标的物的选择
- 技术分析和演化分析则应用于具体投资操作的时间和空间的判断上，作为提高投资分析有效性和可靠性的重要手段
## 基本面分析(basic)
- 基本面分析行情的走势，包括宏观经济重大突发事件以及行业形势等
- 证券的价格由其内在价值决定的
- 价格受政治、经济、心里等因素影响而频繁变动，并总是围绕价值上下波动
### 利用宏观经济信息
- GDP对股市的影响
- 通货膨胀对股市的影响
- 利率对股市的影响
- 经济周期对股市的影响
- 存款准备金率对股市的影响
- 汇率对股市的影响
- 物价变动对股市的影响
- 政治因素对股市的影响
- 自然因素对股市的影响
### 利用行业信息
- 行业的分类
- 行业的性质
- 行业的生命周期
- 行业的分析方法（核心思想：板块轮动）
### 利用公司信息
- 计算上市公司的净资产：支撑股票市场价格的重要寄出
```text
    公式：净资产=所有者权益（包括实收资本或股本、资本公积、盈余公积和未分配利润等）=资产总额-负债总额
```
- 利用报表分析上市公司
```text
    财报，查看公司的盈利能力、成长能力、营运能力、偿债能力以及现金流等；
    财务报表可分为4部分：
        资产负债表
        损益表
        股东权益变动表
        现金流量表
```
- 公司经营管理能力分析
```text
    财务状况、经营情况、管理水平、技术能力、市场大小、行业特点、发展潜力等
``` 

## 技术面分析(technology)
- 证券市场的价格是复杂变化的，在投资时都要有一套方法来指定或选择投资策略
- 技术分析是以预测市场价格变化未来趋势为目的（并非要准去的预测具体的价格！！！）
- 技术分析是以市场行为为研究对象
- 技术分析认为：市场行为包容消化一切
### 利用K线技术分析
- K线分析是靠人类的主观印象而建立的，并且是基于历史的形态组合进行表达的分析方法
- K线的基本形态
- 各种图像影线的意义
- K线组合的规律
### 利用趋势线技术分析（顺势而为）
- 意义：顺从股价沿最小阻力运行的趋势方向而展开操作，与股价波动趋势达到“天人合一”
- 趋势线
```text
    趋势线是你的朋友，永远顺着趋势展开操作，不可逆势而为。
```
- 管道线
```text
    趋势线的演化版本，进一步描述趋势、判断出入点的方法
```
- 支撑线和压力线
### 利用形态技术分析
- 反转形态
```text
    V形与倒V形
    圆弧顶与圆弧底
    双重顶与双重底
```
- 持续形态
```text
    三角形形态
    矩形形态
    旗形形态
    楔形形态
    头肩底形态
```
### 利用指标技术分析
- 均线
- KDJ指标
- BOLL指标
- MACD指标
- RSI指标
- 大单净量（同花顺level2功能）


- 分析K线形态，各种技术指标，输出具备可操作性的股票信息和指标输出
### K线形态
- 包含各种反转形态、持续形态和特殊形态

### 技术指标
- 主要包含：
```text
    - MACD：平滑异同移动平均线指标
        金叉、死叉、零轴和背离 分析
    - KDJ ：随机动量指标
        金叉、死叉分析
    - RSI ：相对强弱指标
        金叉、死叉分析
```

# 使用库
## tushare
- [tushare github](https://github.com/waditu/tushare)
- [tushare使用指南(官方)](https://tushare.pro/document/2)
- [tushare基本教程(官方)](http://tushare.org/index.html)
## mplfinance
- [mplfinance详解](https://blog.csdn.net/wuwei_201/article/details/105781844)

# 常用分析网站
- [问财网](http://www.iwencai.com/stockpick)