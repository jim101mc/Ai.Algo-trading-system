import matplotlib.pyplot as plt

def plot_equity(equity_curve):
    plt.figure()
    plt.plot(equity_curve)
    plt.title("Equity Curve")
    plt.xlabel("Trades")
    plt.ylabel("Equity")
    plt.grid()
    plt.show()


def analyze(trades):
    wins = len([t for t in trades if t["result"] == "WIN"])
    losses = len([t for t in trades if t["result"] == "LOSS"])

    total = len(trades)
    win_rate = wins / total * 100 if total > 0 else 0

    profit = 0
    for t in trades:
        if t["result"] == "WIN":
            profit += 1
        else:
            profit -= 1

    return {
        "total_trades": total,
        "wins": wins,
        "losses": losses,
        "win_rate": round(win_rate, 2),
        "net_score": profit
    }