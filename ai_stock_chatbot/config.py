# config.py
from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent

dotenv_path = PROJECT_ROOT / ".env"
if not find_dotenv(str(dotenv_path), raise_error_if_not_found=False):
    raise FileNotFoundError(f".env file not found at {dotenv_path}")
load_dotenv(dotenv_path=dotenv_path)

def get_settings():
    return {
        "openai": os.getenv("API_KEY_OPENAI"),
        "polygon": os.getenv("API_KEY_POLYGON"),
        "debug": os.getenv("DEBUG", "False").lower() == "true",
        "env": os.getenv("ENV", "development"),
    }

# Validate on import
settings = get_settings()

if not settings["openai"]:
    raise ValueError("OpenAI API key missing in .env")
if not settings["polygon"]:
    raise ValueError("Polygon API key missing in .env")