import reflex as rx
from ai_stock_chatbot.state.chatbot_state import ChatbotState

@rx.page(route="/", title="AI Stock Chatbot")
def chatbot():
    return rx.container(
        rx.vstack(
            # App title
            rx.heading("AI Stock Chatbot", size="7"),

            # Subheading
            rx.text(
                "Ask for a stock recommendation by entering a stock symbol (e.g., AAPL, TSLA)",
                size="3",
                color="gray",
            ),

            # Chat area (with loading state)
            rx.box(
                rx.cond(
                    ChatbotState.is_loading,
                    rx.center(
                        rx.vstack(
                            rx.spinner(color="gray", thickness="4px", size="3", loading=True),
                            rx.text("Fetching stock data...", size="2", color="gray"),
                            spacing="3",
                        ),
                        height="100%",
                        width="100%",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.foreach(
                                ChatbotState.messages,
                                lambda msg: rx.text(msg, font_size="3", color="#333333"),
                            ),
                            rx.text("", id="scroll-anchor"),
                        ),
                        overflow_y="auto",
                        scrollbar="hover",
                        max_height="500px",
                        padding_right="2",
                        width="100%",
                    )
                ),
                border="1px solid #e2e8f0",
                border_radius="15px",
                padding_y="25px",
                padding_x="25px",
                background_color="white",
                shadow="md",
                width="100%",
                overflow="hidden",
            ),

            # Input form
            rx.form(
                rx.hstack(
                    rx.input(
                        placeholder="Enter stock symbol...(e.g., AAPL, TSLA)",
                        value=ChatbotState.user_input,
                        on_change=ChatbotState.set_user_input,
                        width="100%",
                    ),
                    rx.button("Analyze", type_="submit", color_scheme="violet", radius="large", size="2", variant="solid"),
                ),
                on_submit=ChatbotState.send_message,
                width="100%",
                padding_top="4",
            ),

            # Clear chat button
            rx.button("Clear Chat", on_click=ChatbotState.clear_chat, variant="soft", color_scheme="violet", radius="large", size="2"),

            spacing="4",
            align="start",
            width="100%",
            max_width="600px",
            padding_y="8",
        ),
        center_content=True,
        padding_top="10",
    )