# AI.Algo Trading System (Backtesting + Live Execution + Analytics)

A modular algorithmic trading system built in Python for research, backtesting, and live execution using MetaTrader 5.  
Includes a full trade lifecycle engine, risk management, and a Streamlit analytics dashboard.

---

## 🚀 Features

### 📊 Backtesting Engine
- Event-driven backtesting system
- Custom strategy support
- Equity curve tracking
- Trade-by-trade logging
- Partial TP (TP1) logic
- Break-even logic simulation

### 📡 Live Trading (MetaTrader 5)
- MT5 integration
- Automated order execution
- Real-time price handling
- Position management system
- Risk-based trade sizing

### 🧠 Strategy System
- Modular strategy architecture
- Easy plug-and-play design
- Supports indicator-based strategies (RSI, MA, MACD, etc.)

### 📉 Trade Management
- TP1 partial close system
- Break-even stop-loss adjustment
- Full SL/TP execution handling
- Trade state tracking

### 🧾 Logging System
Standard format used across backtesting and live trading:

timestamp | symbol | strategy | type | entry | exit | result | pnl | equity

- CSV-based trade journal
- Unified structure for analytics & ML

### 📊 Streamlit Dashboard
- Interactive backtest UI
- Equity curve visualization
- Trade history viewer
- Strategy parameter controls

---

## Installation

bash
```markdown id="r7"
git clone https://github.com/yourusername/ai-trading-system.git
cd ai-trading-system
```
```markdown id="r7"
pip install -r requirements.txt
```
```markdown id="r7"
streamlit run app.py
```

---

## 📈 Workflow

1. Build strategy in `/strategies`
2. Run backtest in `/backtesting`
3. Optimize parameters
4. Deploy live via MT5
5. Monitor via Streamlit dashboard

---

## 📊 Metrics Tracked

- Total trades
- Win rate
- Net PnL
- Equity curve
- TP1 performance
- Break-even adjustments
- Trade-level outcomes

---

## 🧠 Design Philosophy

- Modular architecture
- Backtest = live parity
- Event-driven execution model
- Reproducible trading research system

---

## 🛠 Tech Stack

- Python
- MetaTrader 5 API
- Pandas
- Streamlit
- Matplotlib

---

## ⚠️ Disclaimer

This project is for educational and research purposes only.  
It does not guarantee financial returns.

---

## 🚀 Future Improvements

- Walk-forward optimization
- ML-based signal generation
- Portfolio-level backtesting
- Real-time data feeds
- Docker deployment
