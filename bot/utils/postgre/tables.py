from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import BigInteger, Integer
from sqlalchemy import String
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class B(Base):
    __tablename__ = "testte"
    id = Column(Integer, primary_key=True)
    data = Column(String)


class Guilds(Base):
    __tablename__ = "guilds"
    guild_id = Column(BigInteger, primary_key=True)
    prefix = Column(String)