import pandas as pd
from sspipe import px, p
import Ashare.Ashare as as_util
import adata as ad_util
import MyTT.MyTT as tt_util


class StockSummary:
    def __init__(self):
        self.data_dirs = {
            'all_stocks': r'C:\Github\data\stocks\all_stock_tickers.pkl',
            'all_concepts': r'C:\Github\data\stocks\all_concept_tickers.pkl',
            'all_constituents': r'C:\Github\data\stocks\all_INDEXPLACEHODLER_member_tickers.pkl',
            'all_concepts_east': r'C:\Github\data\stocks\all_concept_tickers_east.pkl',
            'all_constituents_east': r'C:\Github\data\stocks\all_INDEXPLACEHODLER_member_tickers_east.pkl',
            'all_indices': r'C:\Github\data\stocks\all_indices.pkl',
            'all_index_members': r'C:\Github\data\stocks\all_INDEXPLACEHODLER_index_members.pkl'
        }

    @staticmethod
    def execute_actions(keyword, index_code=None):
        if keyword == 'all_stocks':
            out = ad_util.stock.info.all_code()
        elif keyword == 'all_concepts':
            out = ad_util.stock.info.all_concept_code_ths()
        elif keyword == 'all_constituents':
            out = ad_util.stock.info.concept_constituent_ths(index_code=index_code)
        elif keyword == 'all_concepts_east':
            out = ad_util.stock.info.all_concept_code_east()
        elif keyword == 'all_constituents_east':
            out = ad_util.stock.info.concept_constituent_east(index_code=index_code)
        elif keyword == 'all_indices':
            out = ad_util.stock.info.all_index_code()
        elif keyword == 'all_index_members':
            out = ad_util.stock.info.index_constituent(index_code=index_code)
        else:
            out = pd.DataFrame()
        return out

    def get_data(self, keyword, refresh=False, index_code=None):
        if keyword not in self.data_dirs.keys():
            raise Exception(f'Please use supported keywords: {self.data_dirs.keys()}!')
        save_dir = self.data_dirs.get(keyword)
        if keyword in ['all_constituents', 'all_constituents_east', 'all_index_members']:
            if index_code is None:
                raise Exception('index_code cannot be None for all_index_members keyword!')
            else:
                if save_dir is not None:
                    save_dir = save_dir.replace('INDEXPLACEHOLDER', index_code)
        if refresh:
            out = self.execute_actions(keyword, index_code)
        else:
            try:
                out = pd.read_pickle(save_dir)
            except (ValueError, FileNotFoundError):
                out = self.execute_actions(keyword, index_code)
        if save_dir is not None:
            out.to_pickle(save_dir)
        return out

