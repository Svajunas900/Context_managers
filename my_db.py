from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from models import UserLogin
from main import engine
from passlib.context import CryptContext



def get_password_hash(password):
    return pwd_context.hash(password)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
with Session(engine) as session:
  # year_month_day = str(datetime.date(datetime.now()))
  # user = UserLogin(id=2, date=year_month_day, time=str(datetime.time(datetime.now())), username="Titas", password=get_password_hash("koncius"), disabled=False)
  # session.add(user)
  # session.commit()

  users = select(UserLogin)
  for user in session.scalars(users):
    print(user.username, user.password)







