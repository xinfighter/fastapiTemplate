from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mysql_host: str = '127.0.0.1'
    mysql_port: int = 3306
    mysql_db_name: str = ''
    mysql_user: str = 'root'
    mysql_password: str = ''

    timezone: str = 'Asia/Shanghai'

    SECRET_KEY: str = 'd7724d7a5a8bb49de32647e73e8b0f93b4637c827dd3ada2a4c07a640bf67390'
    ALGORITHM: str = 'HS256'
    EXPIRE: int = 60 * 24  # 单位：分钟

    class Config:
        env_file = '.env'


settings = Settings()
