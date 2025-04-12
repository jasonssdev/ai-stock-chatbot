import httpx
from ai_stock_chatbot.config import settings
from datetime import datetime, timedelta, timezone

API_KEY = settings["polygon"]

BASE_URL = "https://api.polygon.io"

def get_stock_data(tickers: list[str]) -> dict:
    """Fetch last 3 days of stock prices (closing) from Polygon for each ticker."""
    result = {}

    # Compute the last 3 days (market open days assumed)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)  # Extra buffer to catch 3 market days

    for ticker in tickers:
        url = f"{BASE_URL}/v2/aggs/ticker/{ticker.upper()}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=desc&limit=3&apiKey={API_KEY}"
        try:
            response = httpx.get(url)
            response.raise_for_status()
            data = response.json()

            if "results" in data:
                # Take the last 3 results sorted by date ascending
                prices = sorted(data["results"], key=lambda x: x["t"])[-3:]
                result[ticker] = [
                    {
                        "date": datetime.fromtimestamp(p["t"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d"),
                        "close": round(p["c"], 2),
                    }
                    for p in prices
                ]
            else:
                result[ticker] = []

        except Exception as e:
            print(f"[ERROR] Failed to fetch {ticker}: {e}")
            result[ticker] = []

    return result