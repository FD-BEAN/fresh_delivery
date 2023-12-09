import pandas as pd
from sspipe import px, p
import Ashare.Ashare as as_util
import adata as ad_util
import MyTT.MyTT as tt_util

res_df = ad_util.stock.info.all_code()
print(res_df)


df = as_util.get_price('sh000001', frequency='1d', count=1000)
print('上证指数日线行情\n', df)
