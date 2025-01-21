import tushare as ts

ts.set_token('ff7e6b3cf4985954032e2a121cadd265b859b6ceab312b986467e9c5')

pro = ts.pro_api()

df = pro.query('daily', ts_code='000001.SZ', start_date='20250115', end_date='20250116')
print(df)
print(len(df))
