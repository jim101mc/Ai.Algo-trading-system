import pandas as pd

class AdvancedStrategy:
    def __init__(self):
        pass

    def ema(self, series, span):
        return series.ewm(span=span, adjust=False).mean()

    def compute_macd(self, series):
        ema12 = self.ema(series, 12)
        ema26 = self.ema(series, 26)
        macd = ema12 - ema26
        signal = self.ema(macd, 9)
        return macd, signal

    def compute_atr(self, df, period=14):
        high_low = df['high'] - df['low']
        high_close = (df['high'] - df['close'].shift()).abs()
        low_close = (df['low'] - df['close'].shift()).abs()
        tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        return tr.rolling(period).mean()

    def generate_signal(self, df):
        df['ema200'] = self.ema(df['close'], 200)
        df['macd'], df['macd_signal'] = self.compute_macd(df['close'])
        df['atr'] = self.compute_atr(df)

        latest = df.iloc[-1]
        prev = df.iloc[-2]

        # Bullish breakout
        if latest['close'] > latest['ema200']:
            if latest['macd'] > latest['macd_signal'] and prev['macd'] <= prev['macd_signal']:
                return "BUY"

        # Bearish breakout
        if latest['close'] < latest['ema200']:
            if latest['macd'] < latest['macd_signal'] and prev['macd'] >= prev['macd_signal']:
                return "SELL"

        return "HOLD"