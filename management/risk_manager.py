import MetaTrader5 as mt5

class RiskManager:
    def __init__(self, risk_percent):
        self.risk_percent = risk_percent

    def lot_size(self, symbol, sl_pips):
        acc = mt5.account_info()
        balance = acc.balance

        risk_amount = balance * (self.risk_percent / 100)

        # XAUUSD approximation:
        pip_value = 1  # per 0.01 move per 1 lot (simplified safe model)

        lot = risk_amount / (sl_pips * pip_value)

        return round(max(lot, 0.01), 2)