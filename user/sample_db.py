from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import (
    ForeignKey,
    String,
    create_engine,
    delete,
    func,
    insert,
    select,
    update,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

CONNECTION_STRING = "postgresql+psycopg2://admin:admin@localhost/fastapi"

engine = create_engine(CONNECTION_STRING, echo=False)


class Base(DeclarativeBase):
    pass


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str]
    city: Mapped[str]
    zipcode: Mapped[int]

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship("User", back_populates="address")


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(String(64), unique=True)
    email: Mapped[str] = mapped_column(String(64), unique=True)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    gender: Mapped[str] = mapped_column(String(20))
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now)
    date_of_birth: Mapped[datetime]

    address: Mapped[Address] = relationship("Address", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User(id: {self.id}, username: {self.username}, email: {self.email}, gender: {self.gender}, status: {self.status}, created_at: {self.created_at})>"


class Tag(str, Enum):
    ELECTRONICS = "Electronics"
    BOOKS = "Books"
    CLOTHING = "Clothing"
    HOME = "Home"
    TOYS = "Toys"
    SPORTS = "Sports"
    BEAUTY = "Beauty"
    AUTOMOTIVE = "Automotive"
    GROCERY = "Grocery"
    FURNITURE = "Furniture"
    MUSIC = "Music"
    OFFICE = "Office Supplies"
    PETS = "Pet Supplies"
    GARDEN = "Garden"
    HEALTH = "Health"
    JEWELRY = "Jewelry"
    SHOES = "Shoes"
    BABY = "Baby Products"
    VIDEO_GAMES = "Video Games"
    MOVIES = "Movies & TV"
    OUTDOORS = "Outdoors"


class Product(Base):
    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(64))
    price: Mapped[float]
    quantity: Mapped[int]
    tags: Mapped[list[Tag]] = mapped_column(
        SQLAlchemyEnum(Tag, values_callable=lambda x: [e.value for e in x], default=[])
    )
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    users: Mapped["User"] = relationship(back_populates="products")


Base.metadata.create_all(engine)


with Session(bind=engine) as session:
    # stmt = insert(User).values(
    #     username="admin", email="admin@admin.com", first_name="admin", last_name="admin", gender="Male", status=True
    # )
    # session.execute(stmt)
    # session.commit()

    # stmt = update(User).where(User.username == "admin").values(last_name="panel")
    # session.execute(stmt)
    # session.commit()

    # stmt = delete(User).where(User.username == "vprovis0")
    # session.execute(stmt)
    # session.commit()

    # specific_date = datetime(2023, 1, 9)
    # res = session.scalars(
    #     # select(User).where(User.gender == "Male", User.status.is_(False), User.created_at < specific_date).limit(10)
    #     select(User)
    #     .where(User.gender == "Male", User.status.is_(False))
    #     .where(User.created_at < specific_date)
    #     .limit(10)
    # ).all()
    #
    # for user in res:
    #     print(user)

    stmt = select(func.count(User.id)).where(User.created_at > datetime(2023, 1, 1))
    result = session.execute(stmt)
    print(result.all())

    # print(session.scalar(select(User).where(User.username == "vprovis0")))
