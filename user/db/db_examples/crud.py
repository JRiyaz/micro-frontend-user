from typing import Sequence

from sqlalchemy import create_engine, or_, select
from sqlalchemy.orm.session import Session

# from table_data import user
from tables_bidirectional import Address, Base, Order, Product, Tag, User, product_tag

CONNECTION_STRING = "postgresql+psycopg2://admin:admin@localhost/fastapi"

engine = create_engine(CONNECTION_STRING, echo=True)

# Base.metadata.create_all(engine)

with Session(engine) as session:
    # stmt = select(User).where(User.username == "johndoe")
    # user: User = session.scalar(stmt)
    # print(user)
    #
    # print()
    # stmt = select(Product).where(Product.price > 500).order_by(Product.quantity.desc())
    # products: Sequence[Product] = session.scalars(stmt).all()
    #
    # for product in products:
    #     print(product)
    #
    # print()
    # print()

    # stmt = select(Product).join(Product.tags).where(Tag.label == "On Sale")
    stmt = (
        select(Product)
        # .distinct()
        .join(product_tag, product_tag.c.product_id == Product.id)
        .join(Tag, product_tag.c.tag_id == Tag.id)
        .where(or_(Tag.label.like("Electronic%"), Tag.label == "On Sale"))
        .group_by(Product.id)
        .order_by(Product.id)
    )
    products = session.scalars(stmt).all()
    print()
    for product in products:
        print(product)
    print()
