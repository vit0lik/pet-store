from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "pet store"
    debug: bool = True
    database_url: str = "sqlite:///./store_db"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8000"
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"
    
    model_config = SettingsConfigDict(env_file=".env")
        
settings = Settings()