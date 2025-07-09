import os

from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    # Flask conf
    DEBUG = os.environ.get("DEBUG", True)

    # CORS conf
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS").split(",")

    # Supabase conf
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
