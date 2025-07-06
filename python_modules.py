from datetime import date
import akshare as ak


result1 = date.fromisoformat('2019-12-04')

result2 = date.fromisoformat('20191204')

result3 = date.fromisoformat('2021-W01-1')

print(result2)

stock_szse_summary_df = ak.stock_szse_summary(date="20200619")
print(stock_szse_summary_df)