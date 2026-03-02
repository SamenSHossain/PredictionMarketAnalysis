
Then aggregated per token:

- Mean squared error  
- Maximum volume  
- Final outcome  

#### Findings

Higher-volume markets exhibit:

- Lower average squared error  
- Stronger calibration  

This supports:

> Liquidity improves accuracy through collective information aggregation.

---

### 6. Cross-Sector Comparison

Markets were categorized by keywords into:

- Politics  
- Crypto  
- Economics  
- Sports  
- Other  

#### Findings

- Sports and Politics are best calibrated.  
- Lower-visibility or niche categories exhibit greater mispricing.  
- Longshot bias appears across all sectors but is strongest in speculative categories (e.g., Crypto).  

---

## Overall Conclusions

Polymarket markets are:

✔ Directionally efficient  
✔ Well-calibrated at high probabilities  
✔ Improved by liquidity  

But exhibit:

✘ Longshot bias  
✘ Tail overconfidence  
✘ Structural hype premiums  
✘ Excess volatility in low-volume markets  

In summary:

> Prediction markets function as strong aggregators of information but are not perfectly efficient in the tails.

---

## Gaps & Limitations

- Settlement logic differs from last traded price  
- Final oracle resolution is strictly 0 or 100  
- Late trading halts can distort final implied probabilities  
- Volume data may not perfectly represent liquidity depth  
- No causal inference — purely observational  

Future improvements:

- Incorporate order book depth  
- Compare across multiple platforms  
- Introduce event-type fixed effects  
- Test dynamic learning rates  

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- SQLite  
- Dash (optional visualization)  

---

## How to Run

1. Place `polymarket.db` in the root directory.  
2. Open `predictionmarketanalysis.ipynb`.  
3. Run all cells sequentially.  

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn dash plotly
