from uuid import uuid4

from sqlalchemy import UUID, Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session

CONNECTION_STRING = "postgresql+psycopg2://admin:admin@localhost/fastapi"

engine = create_engine(CONNECTION_STRING, echo=False)


class Base(DeclarativeBase):
    __abstract__ = True


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = Column(UUID, primary_key=True, default=uuid4)
    username: Mapped[str] = Column(String(64), unique=True, nullable=False)
    email: Mapped[str] = Column(String(64), unique=True, nullable=False)
    firstName: Mapped[str] = Column(String(64), nullable=False)
    lastName: Mapped[str] = Column(String(64), nullable=False)
    password: Mapped[str] = Column(String(64))
    active: Mapped[bool] = Column(Boolean)
    age: Mapped[int] = Column(Integer)

    def __repr__(self):
        return (
            f"<User(id={self.id}, username={self.username}, email={self.email}, firstName={self.firstName}, "
            f"lastName={self.lastName}, active={self.active}, age={self.age})>"
        )


Base.metadata.create_all(engine)

with Session(bind=engine) as session:
    # session.add_all(users)
    # session.commit()

    users = session.query(User).all()
    for user in users:
        print(user)
