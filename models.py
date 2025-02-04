from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float, Boolean, ForeignKey, text, create_engine


engine = create_engine("sqlite:///context_db.db", echo=True)


class Base(DeclarativeBase):
  pass


class UserLogin(Base):
  __tablename__ = "user_login"

  id: Mapped[int] = mapped_column(primary_key=True)
  date: Mapped[str] = mapped_column(String(70))
  time: Mapped[str] = mapped_column(String(30))
  username: Mapped[str] = mapped_column(String(30))
  password: Mapped[str] = mapped_column(String(150))
  disabled: Mapped[bool] = mapped_column(Boolean())


class UserRequests(Base):
  __tablename__ = "user_requests"

  id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[int] = mapped_column(ForeignKey("user_login.id"))
  request_url: Mapped[str] = mapped_column(String(150))
  response_description: Mapped[str] = mapped_column(String(150)) 


Base.metadata.create_all(engine)