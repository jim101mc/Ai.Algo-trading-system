import pandas as pd
from utils.logger import TradeLogger

logger = TradeLogger()

class BacktestEngine:
    def __init__(self, data, strategy, sl_pips=100, tp_pips=50):
        self.data = data
        self.strategy = strategy
        self.sl = sl_pips * 0.01
        self.tp = tp_pips * 0.01

        self.trades = []
        self.position = None

        self.equity = 100
        self.equity_curve = []

    def run(self):
        for i in range(250, len(self.data)):
            window = self.data.iloc[:i]

            signal = self.strategy.generate_signal(window)
            price = self.data.iloc[i]["close"]

            self._handle_position(price)
            self._open_trade(signal, price)

        return self.trades, self.equity_curve

    def _open_trade(self, signal, price):
        if self.position is not None:
            return

        if signal == "BUY":
            self.position = {
                "type": "BUY",
                "entry": price,
                "sl": price - self.sl,
                "tp": price + self.tp
            }

        elif signal == "SELL":
            self.position = {
                "type": "SELL",
                "entry": price,
                "sl": price + self.sl,
                "tp": price - self.tp
            }

    def _handle_position(self, price):
        if self.position is None:
            return

        p = self.position

        if p["type"] == "BUY":
            if price <= p["sl"]:
                self._close_trade(price, "LOSS")
            elif price >= p["tp"]:
                self._close_trade(price, "WIN")

        elif p["type"] == "SELL":
            if price >= p["sl"]:
                self._close_trade(price, "LOSS")
            elif price <= p["tp"]:
                self._close_trade(price, "WIN")

    def _close_trade(self, price, result):
        entry = self.position["entry"]
        trade_type = self.position["type"]

        pnl = price - entry if trade_type == "BUY" else entry - price

        self.equity += pnl
        self.equity_curve.append(self.equity)

        self.trades.append({
            "entry": entry,
            "exit": price,
            "type": trade_type,
            "result": result,
            "pnl": pnl
        })

        logger.log_trade(
            symbol="BACKTEST",
            strategy="ADVANCED",
            trade_type=trade_type,
            entry=entry,
            exit_price=price,
            result=result,
            pnl=pnl,
            equity=self.equity
        )

        self.position = None