from execution.mt5_connector import positions, tick, send
import MetaTrader5 as mt5
from utils.logger import TradeLogger

logger = TradeLogger()
def manage(symbol):
    pos = positions(symbol)
    if not pos:
        return

    p = pos[0]

    t = tick(symbol)
    price = t.bid if p.type == 1 else t.ask

    entry = p.price_open

    point = 0.01

    # TP1 logic
    if p.type == mt5.ORDER_TYPE_BUY:

        if not p.tp1_done and price >= entry + 50 * point:
            partial_close(p, 0.8)
            move_be(p, entry)
            p.tp1_done = True   

    if p.type == mt5.ORDER_TYPE_SELL:

        if not p.tp1_done and price <= entry - 50 * point:
            partial_close(p, 0.8)
            move_be(p, entry)
            p.tp1_done = True


def partial_close(position, ratio):
    

    logger = TradeLogger()

    vol = position.volume * ratio

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": position.symbol,
        "volume": round(vol, 2),
        "type": mt5.ORDER_TYPE_SELL if position.type == 0 else mt5.ORDER_TYPE_BUY,
        "position": position.ticket,
        "price": tick(position.symbol).bid,
        "deviation": 10,
        "magic": 123456,
    }

    result = send(request)

    logger.log_trade(
        symbol=position.symbol,
        strategy="HYBRID",
        trade_type="PARTIAL_CLOSE",
        entry=position.price_open,
        exit_price=0,
        result="PARTIAL",
        pnl=0,
        equity=0
    )

    return result


def move_be(position, entry):

    #prevent repeated BE moves
    if hasattr(position, "be_moved") and position.be_moved:
        return

    request = {
        "action": mt5.TRADE_ACTION_SLTP,
        "position": position.ticket,
        "sl": entry,
        "tp": position.tp,
    }

    result = send(request)

    #verify execution success
    if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
        logger.log_trade(
            symbol=position.symbol,
            strategy="HYBRID",
            trade_type="MOVE_BE_FAILED",
            entry=position.price_open,
            exit_price=0,
            result="FAILED",
            pnl=0,
            equity=0
        )
        return

    # mark state
    position.be_moved = True
    
    logger.log_trade(
        symbol=position.symbol,
        strategy="HYBRID",
        trade_type="MOVE_BE",
        entry=position.price_open,
        exit_price=0,
        result="BE",
        pnl=0,
        equity=0
    )

    return result