# ðŸ’¹ Financial Analysis & Stock Portfolio Dashboard
### NSE Portfolio Analytics, Risk Metrics & Valuation | MBA Finance Project

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Finance](https://img.shields.io/badge/Domain-Finance%20%2F%20FinTech-green)
![NumPy](https://img.shields.io/badge/NumPy-Quant%20Analysis-013243?logo=numpy)
![MBA](https://img.shields.io/badge/MBA-Finance%20Specialization-purple)

---

## ðŸŽ¯ Project Overview

This project simulates a **real-world equity portfolio analysis** for 5 NSE-listed stocks using quantitative finance techniques. It covers portfolio construction, risk-adjusted returns, correlation analysis, and fundamental valuation â€” the kind of analysis done by equity analysts, portfolio managers, and FinTech firms.

**Business Problem:** A â‚¹10 Lakh investment is split across 5 blue-chip Indian stocks. How did the portfolio perform vs Nifty 50? What are the risk metrics? Which stocks are fundamentally under/overvalued?

---

## ðŸ“Œ Portfolio Holdings

| Stock | Allocation | Sector |
|---|---|---|
| RELIANCE | 30% | Conglomerate / Energy |
| TCS | 25% | IT Services |
| INFY | 20% | IT Services |
| HDFC Bank | 15% | Banking / FinTech |
| ITC | 10% | FMCG |

---

## ðŸ“Š Key Results

| Metric | Portfolio | Nifty 50 (Benchmark) |
|---|---|---|
| Total Return (2 yrs) | +27.3% | ~18% |
| Sharpe Ratio | 1.25 | ~0.85 |
| Max Drawdown | -5.2% | -8.1% |
| Annual Volatility | 14.3% | 13.7% |
| VaR (95%) | -1.01%/day | -1.2%/day |

**Portfolio outperformed Nifty 50 with a better risk-adjusted return (Sharpe: 1.25 vs ~0.85)**

---

## ðŸ” Analysis Modules

### 1. Portfolio Performance vs Benchmark
- Compared cumulative returns against Nifty 50 index over 24 months
- Identified alpha generation and tracking error

### 2. Risk Metrics
- **Sharpe Ratio** â€” Return per unit of risk
- **Maximum Drawdown** â€” Worst peak-to-trough decline
- **Value at Risk (VaR)** â€” Daily loss at 95% confidence level
- **Annual Volatility** â€” Annualized standard deviation of returns

### 3. Correlation Matrix
- Identified diversification benefits across sectors
- IT stocks (TCS, INFY) showed high positive correlation â€” a concentration risk

### 4. P/E Valuation
Used Price-to-Earnings ratio vs sector average to identify:
- ðŸŸ¢ Undervalued: TCS, INFY, HDFC
- ðŸ”´ Overvalued: RELIANCE, ITC (relative to sector peers)

### 5. Monthly Returns Heatmap
- Visualized month-by-month portfolio performance
- Identified seasonal patterns and drawdown periods

---

## ðŸ“ˆ Dashboard Preview

![Financial Dashboard](outputs/financial_dashboard.png)

---

## ðŸ› ï¸ Tools & Concepts

| Tool / Concept | Purpose |
|---|---|
| Python + NumPy | Geometric Brownian Motion simulation |
| Pandas | Time-series data manipulation |
| Matplotlib | Dark-theme financial charts |
| Sharpe Ratio | Risk-adjusted return measurement |
| VaR | Downside risk quantification |
| P/E Ratio | Fundamental valuation |
| Correlation Matrix | Portfolio diversification analysis |

---

## ðŸš€ How to Run

```bash
git clone https://github.com/yourusername/financial-portfolio-analysis.git
cd financial-portfolio-analysis

pip install -r requirements.txt
python financial_analysis.py
```

---

## ðŸ“ Project Structure

```
financial-portfolio-analysis/
â”‚
â”œâ”€â”€ financial_analysis.py       # Main analysis script
â”œâ”€â”€ outputs/
â”‚   â””â”€â”€ financial_dashboard.png # Full dashboard
â”œâ”€â”€ requirements.txt
â””â”€â”€ README.md
```

---

## ðŸ’¡ Key Financial Insights

1. **Portfolio Alpha**: +9.3% excess return over Nifty 50 benchmark
2. **Best Performer**: TCS (+33.3% annualized) â€” driven by global IT demand
3. **Diversification Gap**: TCS & INFY correlation of 0.82 â€” sector concentration risk
4. **Valuation Opportunity**: HDFC Bank P/E (18.9) below sector average (22.0) â€” potential upside

---

## ðŸ“š Financial Concepts Applied

- Modern Portfolio Theory (MPT)
- Geometric Brownian Motion (stock price simulation)
- Sharpe Ratio, Sortino Ratio thinking
- Value at Risk (VaR)
- P/E and PEG Ratio analysis
- Correlation & Diversification

---

## ðŸ‘¤ Author

**[ANIKET]**
MBA â€” Marketing & Finance (Dual Specialization)

[![LinkedIn](https://www.linkedin.com/in/aniket-trivedi-94a8a0282?utm_source=share_via&utm_content=profile&utm_medium=member_ios)
[![GitHub](https://github.com/anikettrivedi63-cyber/)

---

> *"Risk comes from not knowing what you're doing." â€” Warren Buffett*

