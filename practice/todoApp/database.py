from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from config import env

# 設定資料庫連線資訊
database_url = f"postgresql://{env.db_username}:{env.db_password}@{env.db_host}:{env.db_port}/{env.db_name}"

# 建立連接引擎
engine = create_engine(database_url)

SessionLocal: sessionmaker = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()

async def connecnt_db():
    print('connect msg::')
    try:
        # 執行一個簡單的 SQL 查詢來測試連接
        with engine.connect() as connection:
            result = connection.execute(text("SELECT NOW()"))
            for row in result:
              return {"message": "Connection successful", "current_time": row[0]}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

