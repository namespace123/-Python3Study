from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表结构
    __tablename__ = 'user'

    # 表名字
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 初始化数据库连接
    engine = create_engine('mysql + mysqlconnector://root:password@localhost:3306/test')

