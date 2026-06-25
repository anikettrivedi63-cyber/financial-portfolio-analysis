"""
Financial Analysis & Stock Dashboard
======================================
MBA Project | Finance + FinTech
Author: [Your Name]
Description: Portfolio analysis, stock performance, risk metrics,
             and valuation using Python — simulating real market behavior.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────
# STYLE
# ─────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': '#0D1117',
    'axes.facecolor': '#161B22',
    'axes.labelcolor': '#8B949E',
    'xtick.color': '#8B949E',
    'ytick.color': '#8B949E',
    'text.color': '#E6EDF3',
    'axes.titlecolor': '#E6EDF3',
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'grid.color': '#21262D',
    'grid.linewidth': 0.5,
})

STOCK_COLORS = {
    'RELIANCE': '#F78166',
    'TCS':      '#79C0FF',
    'INFY':     '#56D364',
    'HDFC':     '#D2A8FF',
    'ITC':      '#FFA657',
}

# ─────────────────────────────────────────
# 1. GENERATE REALISTIC STOCK DATA
# ─────────────────────────────────────────
np.random.seed(2024)

def generate_stock(name, start_price, annual_return, volatility, days=504):
    """Geometric Brownian Motion — the standard financial model for stock prices."""
    dt = 1/252  # trading days per year
    daily_return = annual_return / 252
    daily_vol    = volatility / np.sqrt(252)

    prices = [start_price]
    for _ in range(days - 1):
        shock = np.random.normal(daily_return, daily_vol)
        prices.append(prices[-1] * (1 + shock))
    return np.array(prices)

# 2 years of trading data (504 days)
start_date   = datetime(2022, 7, 1)
trading_days = pd.bdate_range(start=start_date, periods=504)

stocks_config = {
    'RELIANCE': {'start': 2400, 'return': 0.14, 'vol': 0.22},
    'TCS':      {'start': 3200, 'return': 0.11, 'vol': 0.18},
    'INFY':     {'start': 1450, 'return': 0.09, 'vol': 0.20},
    'HDFC':     {'start': 1550, 'return': 0.16, 'vol': 0.25},
    'ITC':      {'start': 320,  'return': 0.20, 'vol': 0.19},
}

prices = pd.DataFrame(index=trading_days)
for name, cfg in stocks_config.items():
    prices[name] = generate_stock(name, cfg['start'], cfg['return'], cfg['vol'])

prices.index.name = 'Date'

# ─────────────────────────────────────────
# 2. PORTFOLIO CONSTRUCTION
# ─────────────────────────────────────────
weights = np.array([0.30, 0.25, 0.20, 0.15, 0.10])  # Portfolio weights
portfolio_value = 1_000_000  # ₹10 Lakh initial investment

# Normalized returns
norm_prices   = prices / prices.iloc[0]
daily_returns = prices.pct_change().dropna()

# Portfolio daily return
port_daily = daily_returns.dot(weights)
port_cumulative = (1 + port_daily).cumprod()

# Benchmark: Nifty 50 (simulated)
np.random.seed(99)
nifty_returns = np.random.normal(0.0004, 0.012, len(daily_returns))
nifty_cumulative = np.cumprod(1 + nifty_returns)

# ─────────────────────────────────────────
# 3. RISK METRICS
# ─────────────────────────────────────────
def calc_metrics(returns, name="Portfolio"):
    ann_return  = returns.mean() * 252
    ann_vol     = returns.std()  * np.sqrt(252)
    sharpe      = ann_return / ann_vol
    max_dd      = (returns.cumsum() - returns.cumsum().cummax()).min()
    var_95      = np.percentile(returns, 5)
    return {
        'Name':            name,
        'Annual Return':   f"{ann_return*100:.1f}%",
        'Annual Volatility': f"{ann_vol*100:.1f}%",
        'Sharpe Ratio':    f"{sharpe:.2f}",
        'Max Drawdown':    f"{max_dd*100:.1f}%",
        'VaR (95%)':       f"{var_95*100:.2f}%",
    }

port_metrics = calc_metrics(port_daily, "Portfolio")
stock_metrics = {s: calc_metrics(daily_returns[s], s) for s in prices.columns}

# ─────────────────────────────────────────
# 4. VALUATION — P/E MODEL
# ─────────────────────────────────────────
valuation_data = {
    'Stock':       ['RELIANCE', 'TCS', 'INFY', 'HDFC', 'ITC'],
    'Current P/E': [22.4, 28.1, 23.7, 18.9, 24.5],
    'Sector P/E':  [20.0, 30.0, 25.0, 22.0, 22.0],
    'EPS Growth':  [12, 15, 11, 18, 22],
    'PEG Ratio':   [1.87, 1.87, 2.15, 1.05, 1.11],
}
valuation = pd.DataFrame(valuation_data)
valuation['Signal'] = valuation.apply(
    lambda r: '🟢 Undervalued' if r['Current P/E'] < r['Sector P/E'] else '🔴 Overvalued', axis=1)

# ─────────────────────────────────────────
# 5. BUILD DARK-THEME FINANCIAL DASHBOARD
# ─────────────────────────────────────────
print("🎨 Building financial dashboard...")

fig = plt.figure(figsize=(22, 15), facecolor='#0D1117')
gs  = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35,
                         top=0.90, bottom=0.06, left=0.05, right=0.97)

# Header
fig.text(0.5, 0.96, '💹 FINANCIAL ANALYSIS & PORTFOLIO DASHBOARD',
         ha='center', fontsize=22, fontweight='bold', color='#E6EDF3')
fig.text(0.5, 0.92, 'NSE Top 5 Holdings  |  Portfolio Value: ₹10,00,000  |  Period: Jul 2022 – Jun 2024',
         ha='center', fontsize=11, color='#8B949E')

# ── KPI BAR ────────────────────────────────────────────────────────────────
kpi_ax = fig.add_axes([0.04, 0.87, 0.93, 0.038])
kpi_ax.set_xlim(0, 5); kpi_ax.set_ylim(0, 1); kpi_ax.axis('off')
kpi_ax.set_facecolor('#0D1117')

total_return = (port_cumulative.iloc[-1] - 1) * 100
kpis = [
    ('Portfolio Return', f'+{total_return:.1f}%', '#56D364'),
    ('Sharpe Ratio',     port_metrics['Sharpe Ratio'], '#79C0FF'),
    ('Ann. Volatility',  port_metrics['Annual Volatility'], '#FFA657'),
    ('Max Drawdown',     port_metrics['Max Drawdown'], '#F78166'),
    ('VaR 95%',          port_metrics['VaR (95%)'], '#D2A8FF'),
]
for i, (label, val, color) in enumerate(kpis):
    x = i + 0.5
    kpi_ax.add_patch(mpatches.FancyBboxPatch(
        (i+0.04, 0.05), 0.90, 0.88,
        boxstyle='round,pad=0.02', fc='#161B22', ec=color, lw=1.5))
    kpi_ax.text(x, 0.70, val,   ha='center', va='center', fontsize=15,
                fontweight='bold', color=color)
    kpi_ax.text(x, 0.25, label, ha='center', va='center', fontsize=8.5, color='#8B949E')

# ── 1. Portfolio vs Nifty ──────────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0, :2])
ax1.set_facecolor('#161B22')
ax1.plot(daily_returns.index, port_cumulative.values * 100 - 100,
         color='#56D364', lw=2, label='Our Portfolio')
ax1.plot(daily_returns.index, nifty_cumulative * 100 - 100,
         color='#8B949E', lw=1.5, linestyle='--', label='Nifty 50')
ax1.fill_between(daily_returns.index, port_cumulative.values * 100 - 100,
                 alpha=0.08, color='#56D364')
ax1.axhline(0, color='#21262D', lw=1)
ax1.set_title('Portfolio Cumulative Return vs Nifty 50 Benchmark', pad=8)
ax1.set_ylabel('Return (%)', fontsize=9)
ax1.legend(fontsize=9, facecolor='#161B22', edgecolor='#30363D')
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=20, labelsize=8)

# ── 2. Portfolio Allocation Donut ─────────────────────────────────────────
ax2 = fig.add_subplot(gs[0, 2])
ax2.set_facecolor('#161B22')
colors_list = list(STOCK_COLORS.values())
wedges, texts, autotexts = ax2.pie(
    weights * 100,
    labels=list(STOCK_COLORS.keys()),
    colors=colors_list,
    autopct='%1.0f%%',
    pctdistance=0.80,
    startangle=90,
    wedgeprops={'width': 0.5, 'edgecolor': '#0D1117', 'linewidth': 2},
    textprops={'fontsize': 9, 'color': '#E6EDF3'}
)
for at in autotexts:
    at.set_fontsize(8); at.set_fontweight('bold')
ax2.set_title('Portfolio Allocation', pad=8)

# ── 3. Individual Stock Performance ──────────────────────────────────────
ax3 = fig.add_subplot(gs[1, :2])
ax3.set_facecolor('#161B22')
for stock, color in STOCK_COLORS.items():
    normalized = (prices[stock] / prices[stock].iloc[0] - 1) * 100
    ax3.plot(prices.index, normalized, color=color, lw=1.5, label=stock, alpha=0.9)
ax3.axhline(0, color='#21262D', lw=1)
ax3.set_title('Individual Stock Returns (Normalized to 0)', pad=8)
ax3.set_ylabel('Return (%)', fontsize=9)
ax3.legend(fontsize=8, facecolor='#161B22', edgecolor='#30363D', ncol=5, loc='upper left')
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
ax3.grid(True, alpha=0.3)
ax3.tick_params(axis='x', rotation=20, labelsize=8)

# ── 4. Correlation Heatmap ────────────────────────────────────────────────
ax4 = fig.add_subplot(gs[1, 2])
ax4.set_facecolor('#161B22')
corr = daily_returns.corr()
im = ax4.imshow(corr.values, cmap='RdYlGn', vmin=-1, vmax=1, aspect='auto')
ax4.set_xticks(range(len(corr.columns))); ax4.set_xticklabels(corr.columns, fontsize=8, rotation=45)
ax4.set_yticks(range(len(corr.index)));   ax4.set_yticklabels(corr.index,   fontsize=8)
for i in range(len(corr)):
    for j in range(len(corr.columns)):
        ax4.text(j, i, f'{corr.values[i,j]:.2f}', ha='center', va='center',
                 fontsize=7.5, color='#0D1117', fontweight='bold')
ax4.set_title('Return Correlation Matrix', pad=8)
plt.colorbar(im, ax=ax4, shrink=0.8)

# ── 5. Risk-Return Scatter ────────────────────────────────────────────────
ax5 = fig.add_subplot(gs[2, 0])
ax5.set_facecolor('#161B22')
for stock, color in STOCK_COLORS.items():
    r = daily_returns[stock]
    ann_ret = r.mean() * 252 * 100
    ann_vol = r.std()  * np.sqrt(252) * 100
    ax5.scatter(ann_vol, ann_ret, color=color, s=120, zorder=5)
    ax5.annotate(stock, (ann_vol, ann_ret), textcoords='offset points',
                 xytext=(6, 4), fontsize=8, color=color)
# Portfolio point
p_ret = port_daily.mean() * 252 * 100
p_vol = port_daily.std()  * np.sqrt(252) * 100
ax5.scatter(p_vol, p_ret, color='white', s=200, marker='*', zorder=6, label='Portfolio')
ax5.annotate('Portfolio', (p_vol, p_ret), textcoords='offset points',
             xytext=(6, 4), fontsize=8, color='white')
ax5.set_title('Risk-Return Scatter', pad=8)
ax5.set_xlabel('Annual Volatility (%)', fontsize=9)
ax5.set_ylabel('Annual Return (%)', fontsize=9)
ax5.grid(True, alpha=0.3)

# ── 6. P/E Valuation ─────────────────────────────────────────────────────
ax6 = fig.add_subplot(gs[2, 1])
ax6.set_facecolor('#161B22')
x = np.arange(len(valuation))
w = 0.35
bars1 = ax6.bar(x - w/2, valuation['Current P/E'], w, label="Stock P/E",  color='#79C0FF', alpha=0.9)
bars2 = ax6.bar(x + w/2, valuation['Sector P/E'],  w, label="Sector P/E", color='#F78166', alpha=0.9)
ax6.set_xticks(x); ax6.set_xticklabels(valuation['Stock'], fontsize=8)
ax6.set_title('P/E Ratio: Stock vs Sector', pad=8)
ax6.set_ylabel('P/E Ratio', fontsize=9)
ax6.legend(fontsize=8, facecolor='#161B22', edgecolor='#30363D')
ax6.grid(True, alpha=0.2, axis='y')

# ── 7. Monthly Returns Heatmap ────────────────────────────────────────────
ax7 = fig.add_subplot(gs[2, 2])
ax7.set_facecolor('#161B22')
monthly_ret = port_daily.copy()
monthly_ret.index = pd.to_datetime(monthly_ret.index)
monthly_grouped = monthly_ret.resample('ME').sum() * 100
years  = monthly_grouped.index.year.unique()
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
matrix = np.full((len(years), 12), np.nan)
for dt, val in zip(monthly_grouped.index, monthly_grouped.values):
    yi = list(years).index(dt.year)
    matrix[yi, dt.month - 1] = val
im2 = ax7.imshow(matrix, cmap='RdYlGn', aspect='auto', vmin=-5, vmax=5)
ax7.set_xticks(range(12)); ax7.set_xticklabels(months, fontsize=7, rotation=45)
ax7.set_yticks(range(len(years))); ax7.set_yticklabels(years, fontsize=8)
for i in range(len(years)):
    for j in range(12):
        if not np.isnan(matrix[i, j]):
            ax7.text(j, i, f'{matrix[i,j]:.1f}%', ha='center', va='center',
                     fontsize=6.5, color='#0D1117', fontweight='bold')
ax7.set_title('Monthly Portfolio Returns (%)', pad=8)

fig.text(0.5, 0.02,
         'MBA Finance Project  •  Data: Simulated via Geometric Brownian Motion  •  Tools: Python, Pandas, NumPy, Matplotlib',
         ha='center', fontsize=8, color='#4A5568')

plt.savefig('/home/claude/financial-analysis/outputs/financial_dashboard.png',
            dpi=150, bbox_inches='tight', facecolor='#0D1117')
print("   ✅ Financial dashboard saved!\n")

# ─────────────────────────────────────────
# PRINT SUMMARY
# ─────────────────────────────────────────
print("=" * 58)
print("       💹 PORTFOLIO PERFORMANCE SUMMARY")
print("=" * 58)
print(f"\n📈 Portfolio Total Return:  +{total_return:.1f}%")
print(f"📊 Sharpe Ratio:            {port_metrics['Sharpe Ratio']}")
print(f"📉 Max Drawdown:            {port_metrics['Max Drawdown']}")
print(f"⚠️  Value at Risk (95%):    {port_metrics['VaR (95%)']} per day")

print(f"\n{'Stock':<12} {'Ann Return':>12} {'Volatility':>12} {'Sharpe':>8}")
print("-" * 48)
for s, m in stock_metrics.items():
    print(f"{s:<12} {m['Annual Return']:>12} {m['Annual Volatility']:>12} {m['Sharpe Ratio']:>8}")

print(f"\n📌 VALUATION SIGNALS:")
for _, row in valuation.iterrows():
    print(f"   {row['Stock']}: P/E {row['Current P/E']} vs Sector {row['Sector P/E']} → {row['Signal']}")

print("\n✅ All outputs saved to /outputs/")
