class HybridMARSI:
    def __init__(self, short_ma, long_ma, rsi_period, rsi_buy, rsi_sell):
        self.short_ma = short_ma
        self.long_ma = long_ma
        self.rsi_period = rsi_period
        self.rsi_buy = rsi_buy
        self.rsi_sell = rsi_sell

    def rsi(self, series, period):
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def generate_signal(self, df):
        df["ma_s"] = df["close"].rolling(self.short_ma).mean()
        df["ma_l"] = df["close"].rolling(self.long_ma).mean()
        df["rsi"] = self.rsi(df["close"], self.rsi_period)

        c = df.iloc[-1]

        if c["ma_s"] > c["ma_l"] and c["rsi"] < self.rsi_buy:
            return "BUY"

        if c["ma_s"] < c["ma_l"] and c["rsi"] > self.rsi_sell:
            return "SELL"

        return "HOLD"