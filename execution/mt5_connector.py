import MetaTrader5 as mt5

def tick(symbol):
    return mt5.symbol_info_tick(symbol)

def positions(symbol):
    return mt5.positions_get(symbol=symbol)

def send(request):
    return mt5.order_send(request)