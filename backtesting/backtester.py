import MetaTrader5 as mt5
from data.data_fetcher import get_data
from strategies.hybrid_ma_rsi import HybridMARSI
from strategies.advanced_strategy import AdvancedStrategy

from backtesting.engine import BacktestEngine
from backtesting.metrics import analyze, plot_equity
mt5.initialize()

symbol = "XAUUSD"

# load historical data
df = get_data(symbol, mt5.TIMEFRAME_M5, 2000)

# use SAME strategy as live trading
strategy = HybridMARSI(20, 50, 14, 35, 65)
strategy2 = AdvancedStrategy()

engine = BacktestEngine(df, strategy, sl_pips=100, tp_pips=50)
engine2 = BacktestEngine2(df, strategy2, sl_pips=100, tp_pips=50)

#trades = engine.run()
#trades2 = engine2.run()

#results = analyze(trades)
#results2 = analyze(trades2)
#print("\nBACKTEST base RESULTS")
#print(results)
#print("\nBACKTEST adv RESULTS")
#print(results2)


trades, equity_curve = engine.run()
trades2, equity_curve2 = engine.run()

results = analyze(trades)
results2 = analyze(trades2)

print("\nBACKTEST RESULTS")
print(results)
plot_equity(equity_curve)

print("\nBACKTEST adv RESULTS")
print(results2)
plot_equity(equity_curve2)