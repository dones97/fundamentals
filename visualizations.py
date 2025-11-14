import plotly.graph_objects as go
import streamlit as st
import re

def parse_financial_data(analysis_text):
    """
    Parse the financial analysis text to extract revenue and cost data
    Returns structured data for Sankey diagram
    """
    # This is a simple parser - you may need to adjust based on actual output
    data = {
        'revenues': [],
        'costs': [],
        'gross_profit': 0,
        'operating_profit': 0,
        'net_income': 0
    }

    # Look for revenue items (lines with $ amounts)
    lines = analysis_text.split('\n')
    for line in lines:
        # Extract dollar amounts
        amounts = re.findall(r'\$[\d,]+\.?\d*[BMK]?', line)
        if amounts and ('revenue' in line.lower() or 'sales' in line.lower()):
            data['revenues'].append({
                'name': line.split(':')[0].strip() if ':' in line else 'Revenue',
                'amount': amounts[0]
            })

    return data

def create_sankey_diagram(revenues, costs, gross_profit=None, operating_profit=None):
    """
    Create a Sankey diagram showing revenue flows to costs

    Args:
        revenues: List of dicts with 'name' and 'amount' keys
        costs: List of dicts with 'name' and 'amount' keys
        gross_profit: Optional gross profit amount
        operating_profit: Optional operating profit amount
    """

    # Color schemes
    revenue_color = 'rgba(34, 139, 34, 0.6)'  # Green
    cost_color = 'rgba(220, 20, 60, 0.6)'      # Red/Pink
    profit_color = 'rgba(65, 105, 225, 0.6)'   # Blue

    # Build nodes
    labels = []
    colors = []

    # Add revenue nodes
    revenue_start_idx = 0
    for rev in revenues:
        labels.append(rev['name'])
        colors.append(revenue_color)

    # Add intermediate node (Total Revenue)
    total_revenue_idx = len(labels)
    labels.append('Total Revenue')
    colors.append(revenue_color)

    # Add cost nodes
    cost_start_idx = len(labels)
    for cost in costs:
        labels.append(cost['name'])
        colors.append(cost_color)

    # Add profit node if applicable
    if gross_profit:
        gross_profit_idx = len(labels)
        labels.append('Gross Profit')
        colors.append(profit_color)

    if operating_profit:
        operating_profit_idx = len(labels)
        labels.append('Operating Profit')
        colors.append(profit_color)

    # Build links
    sources = []
    targets = []
    values = []
    link_colors = []

    # Revenue sources to Total Revenue
    for i, rev in enumerate(revenues):
        sources.append(revenue_start_idx + i)
        targets.append(total_revenue_idx)
        values.append(parse_amount(rev['amount']))
        link_colors.append(revenue_color)

    # Total Revenue to Costs
    for i, cost in enumerate(costs):
        sources.append(total_revenue_idx)
        targets.append(cost_start_idx + i)
        values.append(parse_amount(cost['amount']))
        link_colors.append(cost_color)

    # Total Revenue to Gross Profit
    if gross_profit:
        sources.append(total_revenue_idx)
        targets.append(gross_profit_idx)
        values.append(parse_amount(gross_profit))
        link_colors.append(profit_color)

    # Create the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color=colors
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors
        )
    )])

    fig.update_layout(
        title="Business Model: Revenue & Cost Flow",
        font=dict(size=12),
        height=600,
        margin=dict(l=0, r=0, t=40, b=0)
    )

    return fig

def parse_amount(amount_str):
    """Convert string amount like '$5.2B' to numeric value in millions"""
    # Remove $ and commas
    amount_str = amount_str.replace('$', '').replace(',', '').strip()

    # Extract number and multiplier
    multipliers = {'B': 1000, 'M': 1, 'K': 0.001, 'T': 1000000}

    for suffix, multiplier in multipliers.items():
        if suffix in amount_str:
            number = float(amount_str.replace(suffix, ''))
            return number * multiplier

    # If no suffix, assume it's already in millions or raw number
    try:
        return float(amount_str)
    except:
        return 0

def create_sample_sankey():
    """Create a sample Sankey diagram based on the Warner Bros image"""
    labels = [
        'Studios', 'Networks', 'Streaming',  # Revenue sources (0, 1, 2)
        'Total Revenue',                      # Aggregation (3)
        'Cost of Revenue',                    # Costs (4)
        'Gross Profit',                       # Intermediate (5)
        'Operating Expenses', 'SG&A', 'Amortization', 'Other',  # More costs (6, 7, 8, 9)
        'Operating Profit',                   # Result (10)
        'Net Loss', 'Other Expenses'         # Final (11, 12)
    ]

    # Define colors
    revenue_green = 'rgba(50, 168, 82, 0.6)'
    cost_red = 'rgba(235, 87, 87, 0.6)'
    profit_blue = 'rgba(100, 149, 237, 0.6)'
    loss_dark_red = 'rgba(139, 0, 0, 0.6)'

    node_colors = [
        revenue_green, revenue_green, revenue_green,  # Revenue sources
        revenue_green,                                 # Total revenue
        cost_red,                                      # COGS
        profit_blue,                                   # Gross profit
        cost_red, cost_red, cost_red, cost_red,       # Operating expenses
        profit_blue,                                   # Operating profit
        loss_dark_red, cost_red                       # Net loss, other
    ]

    # Example based on WB diagram: Revenue ~$9B
    sources = [
        0, 1, 2,        # Studios, Networks, Streaming → Total Revenue
        3, 3,           # Total Revenue → COGS, Gross Profit
        5, 5, 5, 5, 5,  # Gross Profit → Operating Expenses, SG&A, Amortization, Other, Operating Profit
        10, 10          # Operating Profit → Net Loss, Other Expenses
    ]

    targets = [
        3, 3, 3,        # → Total Revenue
        4, 5,           # → COGS, Gross Profit
        6, 7, 8, 9, 10, # → Operating costs and Operating Profit
        11, 12          # → Net Loss, Other
    ]

    values = [
        3300, 3900, 2600,  # Revenue sources (total ~9.8B)
        4600, 4500,         # COGS and Gross Profit
        3900, 2480, 1400, 180, 600,  # Operating expenses breakdown
        100, 500            # Final split
    ]

    link_colors = [
        revenue_green, revenue_green, revenue_green,
        cost_red, profit_blue,
        cost_red, cost_red, cost_red, cost_red, profit_blue,
        loss_dark_red, cost_red
    ]

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=20,
            thickness=25,
            line=dict(color="white", width=2),
            label=labels,
            color=node_colors,
            customdata=[
                '$3.3B', '$3.9B', '$2.6B',
                '$9.0B',
                '$4.6B',
                '$4.5B',
                '$3.9B', '$2.4B', '$1.4B', '$0.2B',
                '$0.6B',
                '$0.1B', '$0.5B'
            ],
            hovertemplate='%{label}<br>%{customdata}<extra></extra>'
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors,
            hovertemplate='%{value:.1f}M<extra></extra>'
        )
    )])

    fig.update_layout(
        title={
            'text': "Business Model Map: Revenue & Cost Flow",
            'font': {'size': 20, 'color': '#1f1f1f'}
        },
        font=dict(size=11, family='Arial'),
        height=700,
        plot_bgcolor='rgba(240, 240, 240, 0.5)',
        paper_bgcolor='white',
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig

def display_sankey_with_data(revenue_data, cost_data, profit_data=None):
    """
    Display Sankey diagram with extracted financial data

    Args:
        revenue_data: Dict with revenue line items
        cost_data: Dict with cost line items
        profit_data: Optional dict with profit metrics
    """
    try:
        fig = create_sankey_diagram(
            revenues=revenue_data,
            costs=cost_data,
            gross_profit=profit_data.get('gross_profit') if profit_data else None,
            operating_profit=profit_data.get('operating_profit') if profit_data else None
        )
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.warning(f"Could not generate custom diagram: {e}")
        st.info("Showing example business model diagram:")
        fig = create_sample_sankey()
        st.plotly_chart(fig, use_container_width=True)
