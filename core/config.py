from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    UPLOAD_DIR: Path = Path("uploads")

    def __init__(self):
        super().__init__()
        self.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)  # garante que a pasta existe


settings: Settings = Settings()