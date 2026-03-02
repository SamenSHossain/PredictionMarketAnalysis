# Polymarket Efficiency Analysis: A Quantitative Evaluation of Prediction Markets

## 📌 Project Overview
This project is a comprehensive data engineering and quantitative analysis platform designed to evaluate the market efficiency of **Polymarket**, the world's largest decentralized prediction market. By analyzing millions of historical price points, order book snapshots, and resolved contracts, this project seeks to answer a fundamental question: *Are prediction market prices unbiased, well-calibrated forecasts that efficiently incorporate available information?*

The analysis audits both internal consistency (rationality of price paths) and information assimilation (accuracy over time) using advanced statistical frameworks, ultimately presented through an interactive web dashboard. 

## 🛠 Tech Stack & Tools
* **Languages:** Python
* **Data Manipulation:** Pandas, NumPy
* **Database / Data Engineering:** SQLite3, SQL 
* **Data Visualization:** Plotly, Seaborn, Matplotlib
* **Web / Dashboarding:** Dash (`dash`, `dash_table`, `html`)

## 📊 Core Methodologies & Analytical Frameworks
This project relies on a dual-framework approach to test market rationality:

### 1. Doob Martingale Framework
Tests for structural market biases by modeling price paths as Doob martingales. In an efficient market, the price sequence of a binary option should theoretically form a Doob martingale, where the current price is the exact conditional expectation of the final settlement given all currently available information.
* **Mechanism:** Isolates contracts that eventually resolved at 0% (failed outcomes) and records their maximum historical prices, comparing these peaks against theoretical bounds derived from Doob's Maximal Inequality. 
* **Insight:** By analyzing how frequently outcomes rise to high implied probabilities (e.g., 80%) before ultimately crashing to zero, we quantify the structural **"Hype Premium"**—identifying market segments that systematically misprice *possibility* as *probability* and violate martingale properties.

### 2. The SciCast & Calibration Frameworks
Evaluates market accuracy through static and temporal lenses using actual resolution vectors.
* **Reliability Diagrams (Static):** Bins price observations (e.g., 0.05–0.15) to compare market-implied probabilities against empirical win rates, explicitly testing for systemic overconfidence or underconfidence.
* **Temporal Learning Curve (SciCast):** Scores every historical price against the binary ground truth using the **Brier Score**. By plotting the average error against the time-to-resolution, the project visualizes the market's learning curve (an efficient market exhibits a steep downward slope as the resolution date approaches).

## 🗄 Data Architecture & Feature Engineering
Rather than relying on a curated subset of data, this analysis leverages a robust local SQLite database (`polymarket.db`) capturing the full Polymarket dataset to avoid selection bias. 

* **Relational Database Design:** Managed tables including `events`, `markets`, `tokens`, `price_history`, `order_book_levels`, `order_book_snapshots`, and `sync_metadata`.
* **Feature Engineering:** Developed SQL and Pandas workflows to merge tokens, history, and market context natively. Isolated 'Yes' tokens to prevent double-counting and standardized all timestamps to UTC.

## 🧠 Key Challenges & Solutions
**The Oracle Resolution Gap:** During development, a significant gap emerged in understanding how Polymarket settles distinct outcome tokens. Because trading halts *prior* to the official on-chain oracle resolution, the "Last Traded Price" is an imperfect indicator of the final result (e.g., a winning market might halt at 98¢). 
* **Solution:** Engineered custom threshold logic to bridge the gap between market-implied probabilities and actual on-chain settlement. By applying a mathematical settlement threshold (`> 0.50` implied probability at the market close), the pipeline successfully establishes a definitive, consistent binary ground truth (0% or 100%) across all contracts without relying purely on raw oracle metadata.

## 📈 Dashboard & Visualization
The analytical outputs are served via a local web application built with **Dash** and **Plotly** (running on `localhost:8050`). The dashboard provides interactive visualizations of:
* The Market Learning Curve (Brier Scores over time)
* Calibration/Reliability Diagrams
* The distribution of "Hype Peaks" across failed markets evaluated through martingale bounds.

## 🚀 How to Run
1. Clone the repository and ensure you have the required dependencies: `pip install -r requirements.txt` (requires `pandas`, `numpy`, `dash`, `plotly`, `seaborn`, `matplotlib`).
2. Ensure the SQLite database `polymarket.db` is present in the root directory and fully synced.
3. Open the `predictionmarketanalysis.ipynb` notebook to view the step-by-step data extraction and exploratory data analysis.
4. Run the Dash application to launch the interactive dashboard:
```bash
python app.py
