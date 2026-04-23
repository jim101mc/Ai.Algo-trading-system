import time
import MetaTrader5 as mt5

from config import *
from data.data_fetcher import get_data

from strategies.hybrid_ma_rsi import HybridMARSI
from management.risk_manager import RiskManager
from management.order_manager import place_trade, has_position
from management.trade_manager import manage

mt5.initialize()

strategy = HybridMARSI(SHORT_MA, LONG_MA, RSI_PERIOD, RSI_BUY, RSI_SELL)
risk = RiskManager(RISK_PERCENT)

while True:
    df = get_data(SYMBOL, mt5.TIMEFRAME_M5)

    if not has_position(SYMBOL):
        signal = strategy.generate_signal(df)

        if signal != "HOLD":
            lot = risk.lot_size(SYMBOL, SL_PIPS)
            place_trade(SYMBOL, signal, lot, SL_PIPS, TP_PIPS)
            
            logger.log_trade(
                symbol=SYMBOL,
                strategy="HYBRID",
                trade_type=signal,
                entry=result.price,
                exit_price=0,
                result="OPEN",
                pnl=0,
                equity=0
)

    else:
        manage(SYMBOL)

    time.sleep(LOOP_SECONDS)