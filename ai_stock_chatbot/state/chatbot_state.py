import reflex as rx
from typing import List
from ai_stock_chatbot.backend.core.chatbot_engine import generate_stock_analysis


class ChatbotState(rx.State):
    """Frontend state logic for the AI stock chatbot."""

    user_input: str = ""
    messages: List[str] = []
    is_loading: bool = False

    def clear_chat(self):
        """Clear chat history."""
        self.messages = []

    def send_message(self):
        symbols = [
            s.strip().upper() for s in self.user_input.split(",") if s.strip()
        ]

        if not symbols:
            self.messages.append(
                "Please enter at least one valid stock symbol.")
            return

        self.messages.append(f"You asked for: {', '.join(symbols)}")
        self.user_input = ""
        self.is_loading = True
        yield

        try:
            response = generate_stock_analysis(symbols)
            self.messages.append(f"{response}")
        except Exception as e:
            self.messages.append(f"Error: {e}")
        finally:
            self.is_loading = False  #  Hide spinner
            yield