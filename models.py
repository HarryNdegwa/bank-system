from sqlalchemy import Column,Date,String,Integer
from sqlalchemy.ext.declarative import declarative_base


# create base class from which models will inherit from
Base=declarative_base()


class Client(Base):

	__tablename__='clients'
	id=Column(Integer,primary_key=True)
	name=Column(String)
	id_no=Column(Integer)
	D_o_B=Column(Date)
	phone=Column(Integer)
	pin=Column(Integer)
	balance=Column(Integer)

	def __repr__(self):
		return f"This is {self.name} account with a balance of Kshs.{self.balance} with an account number {self.id}"

