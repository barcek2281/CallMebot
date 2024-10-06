from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str

class DataBase:
    def __init__(self, db_host: str, db_name: str, db_password: str, db_port: str, db_user: str):
        self.db_host = db_host
        self.db_name = db_name
        self.db_password = db_password
        self.db_port = db_port
        self.db_user = db_user
        # Generate db_url dynamically
        self.db_url = f'postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'

@dataclass
class Config:
    tg_bot: TgBot
    db: DataBase


def load_config(path: str | None= None) -> Config:
    env: Env = Env()
    env.read_env

    tgBot = TgBot(env('BOT_TOKEN'))

    db = DataBase(env("DB_HOST"),
                  env("DB_NAME"),
                  env("DB_PASSWORD"),
                  env("DB_PORT"),
                  env("DB_USER"))

    return Config(tg_bot=tgBot, db=db)
