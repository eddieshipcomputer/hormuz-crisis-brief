#!/usr/bin/env python3
"""Generate charts for the Strait of Hormuz oil crisis report."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Color palette
DARK = '#1a1a2e'
ACCENT = '#e94560'
BLUE = '#0f3460'
GOLD = '#f5a623'
GREEN = '#16c79a'
GREY = '#8d99ae'
LIGHT = '#f8f9fa'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.edgecolor': '#333',
    'axes.labelcolor': '#333',
    'xtick.color': '#555',
    'ytick.color': '#555',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': '#fafafa',
})


def chart1_hormuz_flows():
    """Bar chart: Strait of Hormuz throughput — pre-war vs current."""
    fig, ax = plt.subplots(figsize=(8, 4.5))

    categories = [
        'Pre-War\n(H1 2025)',
        'Peak Crisis\n(Mar–May 2026)',
        'Post-Ceasefire\n(Jul 2026)',
    ]
    hormuz_only = [14.5, 1.2, 8.5]
    pipelines = [0, 4.5, 6.5]
    # Total: ~14.5 pre, ~5.7 peak, ~15.0 now

    x = np.arange(len(categories))
    width = 0.5

    bars1 = ax.bar(x, hormuz_only, width, label='Strait of Hormuz (tankers)',
                   color=ACCENT, edgecolor='white', linewidth=1.5)
    bars2 = ax.bar(x, pipelines, width, bottom=hormuz_only,
                   label='Pipeline bypass (East-West + Fujairah)',
                   color=BLUE, edgecolor='white', linewidth=1.5)

    # Total labels
    totals = [h + p for h, p in zip(hormuz_only, pipelines)]
    for i, total in enumerate(totals):
        ax.text(i, total + 0.4, f'{total:.1f}M bpd', ha='center',
                fontsize=12, fontweight='bold', color=DARK)

    # Component labels
    for bar in bars1:
        h = bar.get_height()
        if h > 0.5:
            ax.text(bar.get_x() + bar.get_width()/2, h/2, f'{h:.1f}M',
                    ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    for i, bar in enumerate(bars2):
        h = bar.get_height()
        if h > 0.5:
            ax.text(bar.get_x() + bar.get_width()/2, hormuz_only[i] + h/2,
                    f'{h:.1f}M', ha='center', va='center', fontsize=9,
                    color='white', fontweight='bold')

    ax.set_ylabel('Million Barrels per Day (bpd)', fontsize=11, fontweight='bold')
    ax.set_title('Regional Oil Flow: Strait of Hormuz vs Pipeline Bypass',
                 fontsize=14, fontweight='bold', color=DARK, pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_ylim(0, 22)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.legend(loc='upper right', fontsize=9, framealpha=0.9)
    ax.axhline(y=20, color=GREY, linestyle='--', alpha=0.5, linewidth=1)
    ax.text(2.45, 20.3, 'Pre-war total ~20-25M', fontsize=8, color=GREY, ha='right')

    plt.tight_layout()
    plt.savefig('/home/stella/openclaw-workspace/stella/oil-crisis-report/charts/chart1_hormuz_flows.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ chart1_hormuz_flows.png")


def chart2_spr_drawdown():
    """SPR inventory over time."""
    fig, ax = plt.subplots(figsize=(8, 4.5))

    # Key data points (year-end unless noted)
    years_labels = [2010, 2015, 2017, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 'Feb\n2026', 'Jul\n2026']
    years_x = list(range(len(years_labels)))
    spr = [727, 695, 665, 635, 638, 595, 371, 352, 394, 411, 411, 320]

    colors = [BLUE]*10 + [ACCENT, ACCENT]
    ax.bar(years_x, spr, color=colors, edgecolor='white', linewidth=1.2, width=0.7)
    ax.set_xticks(years_x)
    ax.set_xticklabels(years_labels, fontsize=8.5)

    # Add value labels for the key transition points
    ax.text(10, 411 + 12, '411M', ha='center', fontsize=9, fontweight='bold', color=DARK)
    ax.text(11, 320 + 12, '320M', ha='center', fontsize=9, fontweight='bold', color=ACCENT)
    # Drawdown arrow
    ax.annotate('', xy=(11, 330), xytext=(10, 400),
                arrowprops=dict(arrowstyle='->', color=ACCENT, lw=2))
    ax.text(10.5, 375, '−91M\n(war\ndrawdown)', fontsize=8, color=ACCENT,
            fontweight='bold', ha='center')

    ax.set_ylabel('Million Barrels', fontsize=11, fontweight='bold')
    ax.set_title('U.S. Strategic Petroleum Reserve Inventory',
                 fontsize=14, fontweight='bold', color=DARK, pad=15)
    ax.set_ylim(0, 850)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(200))

    # 1983 low reference
    ax.axhline(y=308, color=GREY, linestyle=':', alpha=0.6)
    ax.text(0.5, 315, '1983 historical low (~308M)', fontsize=8, color=GREY)

    plt.tight_layout()
    plt.savefig('/home/stella/openclaw-workspace/stella/oil-crisis-report/charts/chart2_spr_drawdown.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ chart2_sorm_drawdown.png")


def chart3_global_reserves():
    """Global OECD reserves — the shrinking buffer."""
    fig, ax = plt.subplots(figsize=(8, 4.5))

    periods = ['Pre-War\n(Feb 2026)', 'End of May\n2026', 'Projected\n(Early 2027)']
    reserves = [2.4, 1.2, 0.0]
    colors_r = [BLUE, GOLD, ACCENT]

    bars = ax.barh(periods, reserves, color=colors_r, edgecolor='white',
                   linewidth=1.5, height=0.55)

    labels = ['2.4B barrels', '1.2B barrels', 'Exhausted']
    for bar, label in zip(bars, labels):
        w = bar.get_width()
        ax.text(w + 0.05, bar.get_y() + bar.get_height()/2, label,
                va='center', fontsize=11, fontweight='bold', color=DARK)

    ax.set_xlabel('Billion Barrels', fontsize=11, fontweight='bold')
    ax.set_title('Global IEA Emergency Oil Reserves — The Spent Buffer',
                 fontsize=14, fontweight='bold', color=DARK, pad=15)
    ax.set_xlim(0, 3)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))

    # 50% line
    ax.axvline(x=1.2, color=GREY, linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.savefig('/home/stella/openclaw-workspace/stella/oil-crisis-report/charts/chart3_global_reserves.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ chart3_global_reserves.png")


def chart4_chokepoints():
    """Risk matrix of maritime choke points."""
    fig, ax = plt.subplots(figsize=(8, 5))

    # Risk levels (x: likelihood, y: impact)
    points = {
        'Strait of Hormuz': (8.5, 9.5, 300, ACCENT),
        'Bab el-Mandeb': (7.0, 6.5, 200, GOLD),
        'Red Sea\n(Houthi zone)': (6.5, 5.5, 180, GOLD),
        'Gulf of Aden\n(Piracy)': (5.5, 4.0, 140, GREEN),
        'Suez Canal': (4.0, 7.0, 160, BLUE),
    }

    for label, (x, y, size, color) in points.items():
        ax.scatter(x, y, s=size, c=color, alpha=0.7, edgecolors='white',
                   linewidth=2, zorder=5)
        ax.annotate(label, (x, y), textcoords='offset points',
                    xytext=(0, -22 if '\n' in label else -18),
                    fontsize=8.5, ha='center', fontweight='bold', color=DARK)

    ax.set_xlabel('Likelihood of Disruption →', fontsize=11, fontweight='bold')
    ax.set_ylabel('Impact on Oil Supply →', fontsize=11, fontweight='bold')
    ax.set_title('Maritime Choke Point Risk Assessment (July 2026)',
                 fontsize=14, fontweight='bold', color=DARK, pad=15)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks(range(0, 11, 2))
    ax.set_yticks(range(0, 11, 2))

    # Quadrant lines
    ax.axhline(y=5, color=GREY, linestyle=':', alpha=0.3)
    ax.axvline(x=5, color=GREY, linestyle=':', alpha=0.3)

    # Quadrant labels
    ax.text(7.5, 9.5, 'CRITICAL', fontsize=8, color=ACCENT, alpha=0.4,
            fontweight='bold', ha='center')
    ax.text(2.5, 9.5, 'HIGH IMPACT\nLOW PROBABILITY', fontsize=7, color=GREY,
            alpha=0.5, ha='center')
    ax.text(7.5, 2, 'MONITOR', fontsize=8, color=GREY, alpha=0.4,
            fontweight='bold', ha='center')

    ax.grid(True, alpha=0.15)
    plt.tight_layout()
    plt.savefig('/home/stella/openclaw-workspace/stella/oil-crisis-report/charts/chart4_chokepoints.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ chart4_chokepoints.png")


def chart5_pipeline_capacity():
    """Pipeline bypass capacity vs utilization."""
    fig, ax = plt.subplots(figsize=(8, 4.5))

    pipelines = [
        'Saudi East-West\n(Petroline)',
        'UAE Habshan-\nFujairah (ADCOP)',
        'ADNOC West-East 1\n(under construction)',
    ]
    current = [2.5, 1.5, 0]
    max_capacity = [7.0, 1.8, 1.5]

    x = np.arange(len(pipelines))
    width = 0.35

    bars1 = ax.bar(x - width/2, current, width, label='Current Utilization',
                   color=GREEN, edgecolor='white', linewidth=1.5)
    bars2 = ax.bar(x + width/2, max_capacity, width, label='Max Capacity',
                   color=BLUE, edgecolor='white', linewidth=1.5)

    for bar in bars1:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.15, f'{h:.1f}M',
                    ha='center', fontsize=9, fontweight='bold', color=GREEN)
    for bar in bars2:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.15, f'{h:.1f}M',
                    ha='center', fontsize=9, fontweight='bold', color=BLUE)

    ax.set_ylabel('Million Barrels per Day (bpd)', fontsize=11, fontweight='bold')
    ax.set_title('Pipeline Bypass Capacity: Current vs Maximum',
                 fontsize=14, fontweight='bold', color=DARK, pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(pipelines, fontsize=9)
    ax.set_ylim(0, 8.5)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.legend(loc='upper right', fontsize=9, framealpha=0.9)

    plt.tight_layout()
    plt.savefig('/home/stella/openclaw-workspace/stella/oil-crisis-report/charts/chart5_pipeline_capacity.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ chart5_pipeline_capacity.png")


if __name__ == '__main__':
    chart1_hormuz_flows()
    chart2_spr_drawdown()
    chart3_global_reserves()
    chart4_chokepoints()
    chart5_pipeline_capacity()
    print("\nAll charts generated successfully.")
