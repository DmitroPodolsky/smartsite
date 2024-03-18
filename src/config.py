from pathlib import Path
from pydantic_settings import BaseSettings

project_dir = Path(__file__).parent

class Settings(BaseSettings):
    """
    Class for storing app settings.
    """
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_PATH: Path = project_dir / "db"

    class Config:
        """
        Configuration class for settings.
        """

        env_file = ".env"
        case_sensitive = True
        extra = 'allow'

settings = Settings()