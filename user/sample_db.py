from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, load_only, mapped_column

CONNECTION_STRING = "postgresql+psycopg2://admin:admin@localhost/fastapi"

engine = create_engine(CONNECTION_STRING, echo=False)

"""
session.query(User).filter_by(active=True).all() ==> [generated in 0.00021s]
SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users."firstName" AS "users_firstName", users."lastName" AS "users_lastName", users.password AS users_password, users.age AS users_age, users.active AS users_active 
FROM users 
WHERE users.active = true

session.scalars(select(User).where(User.active.is_(True))).all() ==> [generated in 0.00017s]
SELECT users.id, users.username, users.email, users."firstName", users."lastName", users.password, users.age, users.active 
FROM users 
WHERE users.active IS true
"""


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    firstName: Mapped[str]
    lastName: Mapped[str]
    password: Mapped[Optional[str]]
    age: Mapped[int]
    active: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return (
            f"<User(id={self.id}, username={self.username}, email={self.email}, active={self.active}, "
            f"firstName={self.firstName}, lastName={self.lastName})>"
        )


Base.metadata.create_all(engine)

with Session(engine) as session:
    # stmt = select(User).where(User.active.is_(True))
    # users = session.scalars(stmt).all()
    # for user in users:
    #     print(user)

    stmt = select(User).where(User.firstName.in_(["Azu", "Khan"]))
    result: Sequence[User] = session.scalars(stmt).all()
    for user in result:
        user.active = False
    session.commit()

    res = session.scalars(select(User).where(User.active.is_(False))).all()

    for user in res:
        print(user)
