def overlay_trades_plotly(position, fig):
    position = position.copy()

    trade = position.diff()
    buy_times = trade[trade == 1].index
    sell_times = trade[trade == -1].index

    for buy_time in buy_times: 
        fig.add_vline(x=buy_time, line_color="#7FFFD4", opacity=0.5)

    for sell_time in sell_times:
        fig.add_vline(x=sell_time, line_color="#FFB6C1", opacity=0.5)

    return fig
