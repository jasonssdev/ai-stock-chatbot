# backend/core/chatbot_engine.py

from typing import List
from ai_stock_chatbot.backend.services.polygon_service import get_stock_data
from ai_stock_chatbot.backend.services.openai_service import get_response

def generate_stock_analysis(tickers: List[str]) -> str:
    """
    Generates stock analysis reports for one or more tickers.
    """
    stock_data = get_stock_data(tickers)

    results = []

    for ticker in tickers:
        if not stock_data.get(ticker):
            results.append(f"Unable to retrieve data for the symbol: {ticker.upper()}")
            continue

        # Format prices into a readable string for OpenAI
        prices_text = f"Stock: {ticker.upper()}\nPrices:\n"
        for item in stock_data[ticker]:
            prices_text += f"- {item['date']}: ${item['close']}\n"

        # Call OpenAI for recommendation
        analysis = get_response(prices_text)

        results.append(f"{ticker.upper()} analysis:\n{analysis or 'OpenAI failed to respond.'}")

    return "\n\n".join(results)