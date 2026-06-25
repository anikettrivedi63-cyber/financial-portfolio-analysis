💹 Financial Analysis & Stock Portfolio Dashboard
NSE Portfolio Analytics, Risk Metrics & Valuation | MBA Finance Project
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Finance](https://img.shields.io/badge/Domain-Finance%20%2F%20FinTech-green)
![NumPy](https://img.shields.io/badge/NumPy-Quant%20Analysis-013243?logo=numpy)
![MBA](https://img.shields.io/badge/MBA-Finance%20Specialization-purple)
---
🎯 Project Overview
This project simulates a real-world equity portfolio analysis for 5 NSE-listed stocks using quantitative finance techniques. It covers portfolio construction, risk-adjusted returns, correlation analysis, and fundamental valuation — the kind of analysis done by equity analysts, portfolio managers, and FinTech firms.
Business Problem: A ₹10 Lakh investment is split across 5 blue-chip Indian stocks. How did the portfolio perform vs Nifty 50? What are the risk metrics? Which stocks are fundamentally under/overvalued?
---
📌 Portfolio Holdings
Stock	Allocation	Sector
RELIANCE	30%	Conglomerate / Energy
TCS	25%	IT Services
INFY	20%	IT Services
HDFC Bank	15%	Banking / FinTech
ITC	10%	FMCG
---
📊 Key Results
Metric	Portfolio	Nifty 50 (Benchmark)
Total Return (2 yrs)	+27.3%	~18%
Sharpe Ratio	1.25	~0.85
Max Drawdown	-5.2%	-8.1%
Annual Volatility	14.3%	13.7%
VaR (95%)	-1.01%/day	-1.2%/day
Portfolio outperformed Nifty 50 with a better risk-adjusted return (Sharpe: 1.25 vs ~0.85)
---
🔍 Analysis Modules
1. Portfolio Performance vs Benchmark
Compared cumulative returns against Nifty 50 index over 24 months
Identified alpha generation and tracking error
2. Risk Metrics
Sharpe Ratio — Return per unit of risk
Maximum Drawdown — Worst peak-to-trough decline
Value at Risk (VaR) — Daily loss at 95% confidence level
Annual Volatility — Annualized standard deviation of returns
3. Correlation Matrix
Identified diversification benefits across sectors
IT stocks (TCS, INFY) showed high positive correlation — a concentration risk
4. P/E Valuation
Used Price-to-Earnings ratio vs sector average to identify:
🟢 Undervalued: TCS, INFY, HDFC
🔴 Overvalued: RELIANCE, ITC (relative to sector peers)
5. Monthly Returns Heatmap
Visualized month-by-month portfolio performance
Identified seasonal patterns and drawdown periods
---
📈 Dashboard Preview
![Financial Dashboard](outputs/financial_dashboard.png)
---
🛠️ Tools & Concepts
Tool / Concept	Purpose
Python + NumPy	Geometric Brownian Motion simulation
Pandas	Time-series data manipulation
Matplotlib	Dark-theme financial charts
Sharpe Ratio	Risk-adjusted return measurement
VaR	Downside risk quantification
P/E Ratio	Fundamental valuation
Correlation Matrix	Portfolio diversification analysis
---
🚀 How to Run
```bash
git clone https://github.com/yourusername/financial-portfolio-analysis.git
cd financial-portfolio-analysis

pip install -r requirements.txt
python financial_analysis.py
```
---
📁 Project Structure
```
financial-portfolio-analysis/
│
├── financial_analysis.py       # Main analysis script
├── outputs/
│   └── financial_dashboard.png # Full dashboard
├── requirements.txt
└── README.md
```
---
💡 Key Financial Insights
Portfolio Alpha: +9.3% excess return over Nifty 50 benchmark
Best Performer: TCS (+33.3% annualized) — driven by global IT demand
Diversification Gap: TCS & INFY correlation of 0.82 — sector concentration risk
Valuation Opportunity: HDFC Bank P/E (18.9) below sector average (22.0) — potential upside
---
📚 Financial Concepts Applied
Modern Portfolio Theory (MPT)
Geometric Brownian Motion (stock price simulation)
Sharpe Ratio, Sortino Ratio thinking
Value at Risk (VaR)
P/E and PEG Ratio analysis
Correlation & Diversification
---
👤 Author
[Your Name]
MBA — Marketing & Finance (Dual Specialization)
![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)
![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)
---
> *"Risk comes from not knowing what you're doing." — Warren Buffett*
