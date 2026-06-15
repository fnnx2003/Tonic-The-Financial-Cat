from sqlalchemy.orm import Session, scoped_session
from sqlalchemy import create_engine
from models import User, Transactions, init_db
username = input("Enter a username:\n")
email = input("Enter your Email:\n")
password = input("Enter a password:\n")
initail_balance = float(input("Enter your starting balance:\n"))
def get_user():
    with Session(init_db) as session:
        with session.begin():
            user_id = User.id
            user_username = User(username=username)
            session.add(user_username)
            user_email = User(email=email)
            session.add(user_email)
            user_password = User(password=password)
            session.add(user_password)
            user_initial_balance = User(initail_balance=initail_balance)
            session.add(user_initial_balance)
db = scoped_session(get_user)
engine = create_engine(init_db, echo=True)
get_user.metadata.create_all(engine)
result = get_user.query(User).all()
if __name__ == "__main__":
    get_user
    print(result)
