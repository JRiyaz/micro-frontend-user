from tables_bidirectional import Address, Order, Product, Tag, User

tag2 = Tag(label="On Sale")
tag3 = Tag(label="New Arrival")
tag4 = Tag(label="Best Seller")

# Create Products with tags
product1 = Product(name="Tablet", price=699.99, quantity=10, tags=[tag2])
product2 = Product(name="Headphones", price=199.99, quantity=5, tags=[])
product3 = Product(name="Laptop", price=1299.99, quantity=3, tags=[tag3])
product4 = Product(name="Keyboard", price=99.99, quantity=20, tags=[tag3, tag4])

# Create Orders with products
order1 = Order(amount=899.98, status=True, products=[product1, product2])
order2 = Order(amount=1399.99, status=False, products=[product3, product4])
order3 = Order(amount=199.99, status=True, products=[product2])

# Create Users with address and orders
user1 = User(
    username="alice",
    email="alice@example.com",
    first_name="Alice",
    last_name="Smith",
    gender="female",
    status=True,
    address=Address(street="456 Oak St", city="Springfield", state="Illinois", zip="62701", country="USA"),
    orders=[order1],
)

user2 = User(
    username="bob",
    email="bob@example.com",
    first_name="Bob",
    last_name="Johnson",
    gender="male",
    status=False,
    address=Address(street="789 Pine St", city="Riverside", state="California", zip="92501", country="USA"),
    orders=[order2, order3],
)
