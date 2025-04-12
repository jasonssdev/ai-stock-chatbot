from ai_stock_chatbot.config import settings
from openai import OpenAI
from ai_stock_chatbot.backend.prompts.prompt_templates import SYSTEM_PROMPT


client = OpenAI(api_key=settings["openai"])


def get_response(prices_text, model="gpt-4o-mini-2024-07-18"):
    input = [{
        "role": "system",
        "content": SYSTEM_PROMPT
    }, {
        "role": "user",
        "content": prices_text
    }]

    try:
        response = client.responses.create(
            model=model,
            input=input,
            temperature=1.1,
        )
        return response.output_text
    except Exception as e:
        print(f"[ERROR] Error in OpenAI API call: {e}")
        return None
