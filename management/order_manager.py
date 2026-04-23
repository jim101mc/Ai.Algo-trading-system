import MetaTrader5 as mt5
from execution.mt5_connector import send, tick, positions

def has_position(symbol):
    pos = positions(symbol)
    return pos is not None and len(pos) > 0


def place_trade(symbol, signal, lot, sl_pips, tp_pips):
    t = tick(symbol)

    point = 0.01  # XAUUSD

    if signal == "BUY":
        price = t.ask
        sl = price - sl_pips * point
        tp = price + tp_pips * point
        order_type = mt5.ORDER_TYPE_BUY

    elif signal == "SELL":
        price = t.bid
        sl = price + sl_pips * point
        tp = price - tp_pips * point
        order_type = mt5.ORDER_TYPE_SELL
    else:
        return None

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 123456,
        "comment": "AI BOT",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    return send(request)