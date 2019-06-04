import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager

from config import DATABASE_URI
from models import Client,Base

engine=create_engine(DATABASE_URI)
Session=sessionmaker(bind=engine)

Base.metadata.create_all(engine) # this method call creates only tables that do not exist
# it is not intended for migrations bt to create the initial structure in an empty db
# it must be bound to a db engine


@contextmanager
def session_scope():
	# setup
	s=Session()
	try:
		yield s
		s.commit()
	except Exception:
		s.rollback()
		raise
	finally:
		s.close()

if __name__ == "__main__":
	what_to_do=int(input("Enter; 1 to deposit,2 to withdraw,3 to check balance,4 to create an account:"))



	with session_scope() as s:
		if what_to_do == 4:
			name=str(input("Enter your full name: "))
			id_no=int(input("Enter you national id number maximum 5 digits: "))
			year=int(input("Enter your year of birth maximum 4 digits: "))
			month=int(input("Enter your month of birth maximum 2 digits : "))
			day=int(input("Enter your day of birth maximum 2 digits: "))
			phone=int(input("Enter a valid phone number 10 digits maximum: "))
			pin=int(input("Enter your pin maximum 4 digits: "))
			client=Client(
				name=name,
				id_no=id_no,
				D_o_B=datetime.date(year,month,day),
				phone=phone,
				pin=pin,
				balance=0
				)
			s.add(client)
			your_id=s.query(Client).count()
			print("Thankyou for creating an account with us.")
			print(f"Please note that your account no. is {your_id}.You will require the no. to do stuffs in your account.")
		elif what_to_do == 1:
			account_no=int(input("Enter your acount no.: "))
			client=s.query(Client).get(account_no)
			deposit=int(input("Enter the amount to deposit:"))
			client.balance+=deposit
			print("You successfully deposited ksh."+str(deposit))
			s.add(client)

		elif what_to_do == 2:
			account_no=int(input("Enter your acount no.: "))
			client=s.query(Client).get(account_no)
			withdraw=int(input("Enter the amount to withdraw:"))
			if withdraw >= client.balance:
				print("Insufficient funds.Exiting.......")
			else:
				client.balance-=withdraw
				print("You successfully made a withdrawal of ksh."+str(withdraw))
				s.add(client)

		elif what_to_do == 3:
			account_no=int(input("Enter your acount no.: "))
			client=s.query(Client).get(account_no)
			print("Your account balance is ksh."+ str(client.balance))

			
			
	






