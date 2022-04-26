import sqlalchemy
from sqlalchemy import create_engine, Table, Integer, String, Numeric, Boolean
from sqlalchemy import MetaData, select
from sqlalchemy.testing.schema import Column

engine = create_engine('sqlite+pysqlite:///my-test_copy.db')
metadata = MetaData()
tax_rates = Table('STAWKI_PODATKU', metadata, autoload=True, autoload_with=engine)
print(sqlalchemy.__version__)

cols = tax_rates.c

with engine.connect() as conn:
    query = select([tax_rates])
    rp = conn.execute(query)
    results = rp.all()
    for row in results:
        print(row)
