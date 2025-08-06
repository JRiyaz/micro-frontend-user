from sqlalchemy import (
    VARCHAR,
    Column,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
    create_engine,
    text,
)

"""
Docker command to setup postgres

docker run --name postgres -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=admin -e POSTGRES_DB=fastapi -v $(pwd)/postgres-db:/var/lib/postgresql/data -p 5432:5432 -d postgres:17-alpine

docker exec -it postgres psql -U admin -d fastapi
"""
# CONNECTION_STRING = "postgresql+psycopg2://admin:admin@localhost:5432/fastapi"

# DEFINE THE DATABASE CREDENTIALS
user = "admin"
password = "admin"
host = "127.0.0.1"
port = 5432
database = "fastapi"


# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database), echo=True)


engine = get_connection()

meta = MetaData()

people = Table(
    "people",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)

books = Table(
    "books",
    meta,
    Column("book_id", Integer, primary_key=True),
    Column("book_price", Numeric),
    Column("genre", VARCHAR),
    Column("book_name", VARCHAR),
)

meta.create_all(engine)

conn = engine.connect()

# insert_stmt = people.insert().values(name="John", age=22)
# result = conn.execute(insert_stmt)
# conn.commit()

# select_stmt = people.select()
# res = conn.execute(select_stmt)
# for row in res.fetchall():
#     print(row)

# update_stmt = people.update().where(people.c.name == "John").values(age=50)
# conn.execute(update_stmt)
# conn.commit()

# statement1 = books.insert().values(book_price=12.2, genre="fiction", book_name="Old age")
# statement2 = books.insert().values(book_price=13.2, genre="non-fiction", book_name="Saturn rings")
# statement3 = books.insert().values(book_price=121.6, genre="fiction", book_name="Supernova")
# statement4 = books.insert().values(book_price=100, genre="non-fiction", book_name="History of the world")
# statement5 = books.insert().values(book_price=1112.2, genre="fiction", book_name="Sun city")
#
# # execute the insert records statement
# conn.execute(statement1)
# conn.execute(statement2)
# conn.execute(statement3)
# conn.execute(statement4)
# conn.execute(statement5)
# conn.commit()

# data = (
#     {"book_price": 400, "genre": "fiction", "book_name": "yoga is science"},
#     {"book_price": 800, "genre": "non-fiction", "book_name": "alchemy tutorials"},
# )
#
# insert_stmt = text("INSERT INTO books (book_price, genre, book_name) VALUES (:book_price, :genre, :book_name)")
# conn.execute(insert_stmt, data)
# conn.commit()
# # raw_sql = text("SELECT * FROM books WHERE books.book_price > 100")
# raw_sql = text("SELECT * FROM books")
# result = conn.execute(raw_sql)
# print(result.all())

raw_sql = text("SELECT book_id, book_price, genre, book_name FROM books")
result = conn.execute(raw_sql).fetchall()
for row in result:
    print(f"{row.book_id}, {row.book_price}, {row.genre}, {row.book_name}")

conn.close()
