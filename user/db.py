from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

conn = "postgresql://username:password@localhost:5432/dbname"

# CONNECTION_STRING = "postgresql+psycopg2://admin:admin@localhost:5432/fastapi"
# CONNECTION_STRING = "postgresql://admin:admin@localhost:5432/fastapi"
CONNECTION_STRING = "postgresql+psycopg2://admin:admin@localhost/fastapi"

engine = create_engine(CONNECTION_STRING)


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, genre={self.genre})>)"


Base.metadata.create_all(engine)
books = [
    Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction"),
    Book(title="1984", author="George Orwell", genre="Dystopian"),
    Book(title="Pride and Prejudice", author="Jane Austen", genre="Romance"),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Classic"),
    Book(title="The Catcher in the Rye", author="J.D. Salinger", genre="Coming-of-Age"),
    Book(title="The Hobbit", author="J.R.R. Tolkien", genre="Fantasy"),
    Book(title="Fahrenheit 451", author="Ray Bradbury", genre="Science Fiction"),
    Book(title="Moby-Dick", author="Herman Melville", genre="Adventure"),
    Book(title="Jane Eyre", author="Charlotte Brontë", genre="Gothic"),
    Book(title="Brave New World", author="Aldous Huxley", genre="Dystopian"),
]
with Session(bind=engine) as session:
    # session.add_all(books)
    # for book in books:
    #     session.add(book)
    # session.commit()
    # book = Book(title="Brave New World - 2", author="Aldous Huxley", genre="Dystopian")
    # session.add(book)
    # session.commit()
    book = session.query(Book).filter_by(genre="Dystopian").first()
    # book.title = "1994"
    # session.commit()
    # for book in query:
    print(f"ID: {book.book_id} Title: {book.title} Author: {book.author} Genre: {book.genre}")

    book = session.query(Book).filter_by(title="Jane Eyre").first()
    session.delete(book)
    session.commit()

    print()
    query = session.query(Book).all()
    print("All books: ")
    for book in query:
        print(f"ID: {book.book_id} Title: {book.title} Author: {book.author} Genre: {book.genre}")
