# models.py
from sqlalchemy import Column, BigInteger, SmallInteger, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    titleOfArticle = Column(String, nullable=False)
    targetOfApplication = Column(String, nullable=False)
    periodOfApplication = Column(String, nullable=False)
    contentOfArticle = Column(String, nullable=False)