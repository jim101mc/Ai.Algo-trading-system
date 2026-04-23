import streamlit as st
import MetaTrader5 as mt5
import sys
import os
from data.data_fetcher import get_data
from strategies.advanced_strategy import AdvancedStrategy
from backtesting.engine import BacktestEngine
from backtesting.metrics import analyze, plot_equity
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(page_title="XAUUSD Backtester", layout="wide")

st.title("📊 XAUUSD AI Backtesting System")

# -----------------------
# INPUT CONTROLS
# -----------------------
symbol = st.text_input("Symbol", "XAUUSD")

sl = st.slider("Stop Loss (pips)", 20, 300, 100)
tp = st.slider("Take Profit (pips)", 20, 300, 50)

bars = st.slider("Historical Bars", 500, 5000, 2000)

run = st.button("Run Backtest")

# -----------------------
# RUN BACKTEST
# -----------------------
if run:
    mt5.initialize()

    st.info("Loading data...")
    df = get_data(symbol, mt5.TIMEFRAME_M5, bars)

    strategy = AdvancedStrategy()

    engine = BacktestEngine(df, strategy, sl_pips=sl, tp_pips=tp)

    trades, equity = engine.run()

    results = analyze(trades)

    # -----------------------
    # RESULTS
    # -----------------------
    st.subheader("Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Trades", results["total_trades"])
    col2.metric("Win Rate", f"{results['win_rate']}%")
    col3.metric("Net Score", results["net_score"])

    # -----------------------
    # EQUITY CURVE
    # -----------------------
    st.subheader("Equity Curve")

    st.line_chart(equity)

    # -----------------------
    # RAW DATA
    # -----------------------
    st.subheader("Trades")
    st.write(trades)