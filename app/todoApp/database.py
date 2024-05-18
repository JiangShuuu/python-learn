from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from app.config import env

# 設定資料庫連線資訊
database_url = f"postgresql://{env.db_username}:{env.db_password}@{env.db_host}:{env.db_port}/{env.db_name}"

# 建立連接引擎
engine = create_engine(database_url)

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

