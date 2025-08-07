from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Column, ForeignKey, String, Table
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

    # Bi-directional One-to-One Relationship, ForeignKey will still be there and `uselist` is optional
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship("User", back_populates="address", uselist=False)

    def __repr__(self):
        return (
            f"<Address(id: {self.id}, street: {self.street}, city: {self.city}, state: {self.state}, zip: {self.zip})>"
        )


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

    # Bi-directional One-to-One relationship (uselist=Fase)
    address: Mapped[Address] = relationship(
        "Address", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )

    # Bi-direction One-to-Many relationship (uselist=True)
    orders: Mapped[list["Order"]] = relationship(
        "Order", back_populates="user", uselist=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(Id: {self.id}, username: {self.username}, email: {self.email}, gender: {self.gender}, status: {self.status})>"


# Many-to-Many between Order and Products
order_product = Table(
    "order_products",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
)


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(default=0.0)
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    # ForeignKey as Order table is child for User table
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship("User", back_populates="orders")

    # Many-to-Many with Products
    products: Mapped[list["Product"]] = relationship("Product", secondary=order_product, back_populates="orders")

    def __repr__(self):
        return f"<Order(Id: {self.id}, amount: {self.amount}, status: {self.status})>"


# Many-to-Many requires separate table
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

    # Many-to-Many relationship wit Tag
    tags: Mapped[list["Tag"]] = relationship("Tag", secondary=product_tag, back_populates="products")

    # Many-to-Many with Orders
    orders: Mapped[list["Order"]] = relationship("Order", secondary=order_product, back_populates="products")

    def __repr__(self):
        return f"<Product(id: {self.id}, name: {self.name}, price: {self.price}, quantity: {self.quantity})>"


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(unique=True)

    # Many-to-Many relationship with Product
    products: Mapped[list["Product"]] = relationship("Product", secondary=product_tag, back_populates="tags")

    def __repr__(self):
        return f"<Tag(Id: {self.id}, label: {self.label})>"
