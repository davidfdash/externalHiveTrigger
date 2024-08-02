# import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://dave:test@localhost/querytest?charset=utf8mb4")
query = "select truefalse from testtable where truefalse = 1;"
data = pd.read_sql(query, con=engine)
print(data)
