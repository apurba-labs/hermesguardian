from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GEMINI_API_KEY: str = "your_gemini_api_key_here"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_BASE_URL: str = "http://localhost:8000"
    DT_ENVIRONMENT: str = "your_dynatrace_environment_url_here"
    DT_PERSONAL_ACCESS_TOKEN: str = "your_dynatrace_personal_access_token_here"

    # This replaces load_dotenv() and manages env priorities cleanly
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore" # Prevents crashing if extra vars exist in .env
    )

settings = Settings()
