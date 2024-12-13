import os

import pandas as pd
import pytz

from qstrader.alpha_model.fixed_signals import FixedSignalsAlphaModel
from qstrader.asset.equity import Equity
from qstrader.asset.universe.static import StaticUniverse
from qstrader.data.backtest_data_handler import BacktestDataHandler
from qstrader.data.daily_bar_csv import CSVDailyBarDataSource
from qstrader.statistics.tearsheet import TearsheetStatistics
from qstrader.trading.backtest import BacktestTradingSession

if __name__ == "__main__":
    start_dt = pd.Timestamp('2003-09-30 14:30:00', tz=pytz.UTC)
    end_dt = pd.Timestamp('2019-12-31 23:59:00', tz=pytz.UTC)

    strategy_symbols = ['SPY', 'AGG']
    strategy_assets = ['EQ:%s' % symbol for symbol in strategy_symbols]
    strategy_universe = StaticUniverse(strategy_assets)

    csv_dir = os.environ.get('QSTRADER_CSV_DATA_DIR', '.')
    data_source = CSVDailyBarDataSource(csv_dir, Equity, csv_symbols=strategy_symbols)
    data_handler = BacktestDataHandler(strategy_universe, data_sources=[data_source])