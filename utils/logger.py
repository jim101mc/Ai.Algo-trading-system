import csv
import os
from datetime import datetime

class TradeLogger:
    def __init__(self, file="trade_log.csv"):
        self.file = file
        self._init_file()

    def _init_file(self):
        if not os.path.exists(self.file):
            with open(self.file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp",
                    "symbol",
                    "strategy",
                    "type",
                    "entry",
                    "exit",
                    "result",
                    "pnl",
                    "equity"
                ])

    def log_trade(self, symbol, strategy, trade_type, entry, exit_price, result, pnl, equity):
        with open(self.file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now(),
                symbol,
                strategy,
                trade_type,
                entry,
                exit_price,
                result,
                pnl,
                equity
            ])