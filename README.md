# AI Algorithmic Trading System (Backtesting + Live Execution + Analytics)

A modular algorithmic trading system built in Python for research, backtesting, and live execution using MetaTrader 5.  
The system includes a full trade lifecycle engine, risk management, and a Streamlit-based analytics dashboard.

---

## Features

### Backtesting Engine
- Event-driven backtesting framework  
- Custom strategy support  
- Equity curve tracking  
- Trade-level logging  
- Partial take-profit (TP1) logic  
- Break-even simulation  

### Live Trading (MetaTrader 5)
- MetaTrader 5 integration  
- Automated order execution  
- Real-time price handling  
- Position management system  
- Risk-based position sizing  

### Strategy System
- Modular strategy architecture  
- Plug-and-play design  
- Supports indicator-based strategies (RSI, MA, MACD)

### Trade Management
- TP1 partial close system  
- Break-even stop-loss adjustment  
- Full SL/TP handling  
- Trade state tracking

```bash
git clone https://github.com/jim101mc/Ai.Algo-trading-system.git
cd ai-trading-system
pip install -r requirements.txt
```
```
streamlit run app.py
```
```
python -m backtesting.backtester
```
