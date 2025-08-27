# Pattern Recognition Strategy: High-Low Turning Points

## 📌 Strategy Title
**Pattern-Based High-Low Turning Point Detection**

---

## 📖 Strategy Description

This strategy identifies **local highs and lows** in price movements by analyzing patterns in consecutive closing prices.  
It detects potential turning points that may indicate **short-term reversals or continuation signals**.

### 🔹 Steps Followed

1. **Initialize instruments & price history**  
   - Subscribes to a list of instruments.  
   - Maintains a rolling history (`deque`) of the latest 180 closing prices per instrument.  

2. **Update Price History**  
   - On each bulk data feed, the latest closing price and timestamp are appended to the instrument’s price history.  

3. **Pattern Recognition**  
   - Once at least 3 data points are available, the algorithm checks for patterns:  
     - **High Point (Low → High → Low)**:  
       - If the current price is greater than both the previous and next price, mark as a **High**.  
     - **Low Point (High → Low → High)**:  
       - If the current price is lower than both the previous and next price, mark as a **Low**.  

4. **Reporting**  
   - Logs all detected Highs and Lows with timestamp and close price.  
   - If no new pattern is found, explicitly reports that no pattern is detected.  

---

### 📊 Trading Interpretations

- **High Point Detected (Potential Resistance)**  
  - Indicates a local peak.  
  - May signal a potential **short-term sell opportunity** or resistance level.  

- **Low Point Detected (Potential Support)**  
  - Indicates a local bottom.  
  - May signal a potential **short-term buy opportunity** or support level.  

- **No Pattern Found**  
  - Market is trending without clear reversal points.  
  - Suggests waiting for stronger confirmation before taking action.  

⚠️ *Note: This strategy is a **pattern recognition tool**. It should be combined with trend confirmation indicators (e.g., moving averages, VWAP, RSI) for robust trading decisions.*  

---

## 🛠️ Libraries Used

- **AlgoAPI**  
  - `AlgoAPIUtil`, `AlgoAPI_Backtest`  
  - Provides backtesting and event-driven trading framework.  

- **collections**  
  - `deque` (double-ended queue)  
  - Efficient rolling history storage with fixed maximum length (180 data points).  


