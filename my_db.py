from sqlalchemy import create_engine, String, Integer, Float, Boolean, ForeignKey, text
from sqlalchemy.orm import Session
from datetime import date, time, datetime
from models import UserLogin


engine = create_engine("sqlite:///context_db.db", echo=True)


with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM user_login;"))
  print(result.all())


with Session(engine) as session:
  year_month_day = str(datetime.date(datetime.now()))
  user = UserLogin(id=1, date=year_month_day, time=str(datetime.time(datetime.now())), username="Svajunas", password="koncius")
  session.add(user)
  session.commit()



