
from general_agent.agent import callback


@callback.new(
    "Fetch historical stock data",
    dict,
    callback.new_arg("stock_ticker", str, "The abbreviated name of the stock"),
    callback.new_arg("timeframe", str, "The duration of each candle",
        enum=[
            "1m", "5m", "15m",
            "1h", "4h",
            "1d",
            "1w",
        ]
    )
)
def get_stock_data(stock_ticker: str, timeframe: str) -> dict:
    pass
