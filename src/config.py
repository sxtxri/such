from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    API_KEY: str

    POSTRGES_DB_PORT: int
    POSTRGES_DB_NAME: str
    POSTRGES_DB_USER: str
    POSTRGES_DB_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file='.env'
    )

    def get_db_url(self):
        return f"postgresql://{self.POSTGRES_DB_USER}:{self.POSTGRES_DB_PASSWORD}@{self.POSTGRES_DB_HOST}/{self.POSTGRES_DB_NAME}"
