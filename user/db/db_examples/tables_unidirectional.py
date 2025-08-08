from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    __abstract__ = True


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(64))
    city: Mapped[str] = mapped_column(String(64))
    state: Mapped[str] = mapped_column(String(64))
    zip: Mapped[str] = mapped_column(String(64))
    country: Mapped[str] = mapped_column(String(64))

    # Foreign Key as Address is dependent/child/many side table will hold the parent reference
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), unique=True)


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

    # Uni-direction One-to-One Relationship, so no back_populates is not used
    address: Mapped[Address] = relationship("Address", uselist=False, cascade="all, delete-orphan")

    # Uni-direction One-to-Many Relationship, so no back_populates is not used
    orders: Mapped[list["Order"]] = relationship("Order", uselist=True, cascade="all, delete-orphan")


# Many-to-Many between Order and Products
order_product = Table(
    "order_products",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
)


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(default=0.0)
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    # ForeignKey as Order table is child/many/dependent side table with One-to-Many so no unique values
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))

    # Many-to-Many
    products: Mapped[list["Product"]] = relationship("Product", secondary=order_product)


# Many-to-Many requires a separate table
product_tag = Table(
    "product_tags",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float] = mapped_column(default=0.0)
    quantity: Mapped[int] = mapped_column(default=1)

    # Many-to-Many Relationship
    tags: Mapped[list["Tag"]] = relationship("Tag", secondary=product_tag)


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(unique=True)
