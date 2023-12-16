import fresh_delivery.data_utils as data_util
import pandas as pd
import adata as ad_utils
from sspipe import px, p

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', 1000)

rsh_data_adata = data_util.prepare_rsh_data(index_list=['000001', '399106'],
                                            rsh_data_dir=r'C:\Github\data\stocks\adata_stock_rsh_data.pkl')
rsh_data_akshare = data_util.prepare_rsh_data(index_list=['000001', '399106'],
                                              rsh_data_dir=r'C:\Github\data\stocks\akshare_stock_rsh_data.pkl')

