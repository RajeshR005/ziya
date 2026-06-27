# seed_products.py

from app.deps import SessionLocal
from app.models.product import Product

db=SessionLocal()
def seed_products(db):

    products = [

        # Smartphones
        Product(
            product_name="Samsung Galaxy M35 5G",
            brand="Samsung",
            category="Smartphone",
            description="6.6-inch AMOLED display, 6000mAh battery, Exynos processor.",
            price=18999,
            stock_quantity=50
        ),

        Product(
            product_name="Samsung Galaxy S24",
            brand="Samsung",
            category="Smartphone",
            description="Premium flagship smartphone with Galaxy AI.",
            price=74999,
            stock_quantity=20
        ),

        Product(
            product_name="iPhone 15",
            brand="Apple",
            category="Smartphone",
            description="A16 Bionic chip and advanced dual-camera system.",
            price=69999,
            stock_quantity=15
        ),

        Product(
            product_name="iPhone 16",
            brand="Apple",
            category="Smartphone",
            description="Latest Apple smartphone with improved AI features.",
            price=79999,
            stock_quantity=12
        ),

        Product(
            product_name="OnePlus Nord CE 4",
            brand="OnePlus",
            category="Smartphone",
            description="120Hz AMOLED display with 100W fast charging.",
            price=24999,
            stock_quantity=40
        ),

        Product(
            product_name="Realme P3 5G",
            brand="Realme",
            category="Smartphone",
            description="Affordable 5G smartphone with powerful battery.",
            price=16999,
            stock_quantity=35
        ),

        Product(
            product_name="Redmi Note 14 Pro",
            brand="Xiaomi",
            category="Smartphone",
            description="200MP camera and AMOLED display.",
            price=21999,
            stock_quantity=30
        ),

        Product(
            product_name="Nothing Phone 3A",
            brand="Nothing",
            category="Smartphone",
            description="Unique transparent design with clean Android.",
            price=27999,
            stock_quantity=18
        ),

        # Headphones

        Product(
            product_name="Boat Rockerz 450",
            brand="Boat",
            category="Headphones",
            description="Wireless headphones with deep bass.",
            price=1499,
            stock_quantity=100
        ),

        Product(
            product_name="Sony WH-CH520",
            brand="Sony",
            category="Headphones",
            description="Bluetooth headphones with 50-hour battery.",
            price=4499,
            stock_quantity=40
        ),

        Product(
            product_name="JBL Tune 760NC",
            brand="JBL",
            category="Headphones",
            description="Noise cancelling wireless headphones.",
            price=5999,
            stock_quantity=25
        ),

        Product(
            product_name="Sennheiser HD 450BT",
            brand="Sennheiser",
            category="Headphones",
            description="Premium wireless headphones with ANC.",
            price=9999,
            stock_quantity=15
        ),

        # Earbuds

        Product(
            product_name="Boat Airdopes 311",
            brand="Boat",
            category="Earbuds",
            description="Budget TWS earbuds with ENC.",
            price=1299,
            stock_quantity=120
        ),

        Product(
            product_name="OnePlus Buds 3",
            brand="OnePlus",
            category="Earbuds",
            description="ANC-enabled premium earbuds.",
            price=5499,
            stock_quantity=50
        ),

        Product(
            product_name="Apple AirPods Pro 2",
            brand="Apple",
            category="Earbuds",
            description="Premium ANC earbuds with spatial audio.",
            price=23999,
            stock_quantity=12
        ),

        Product(
            product_name="Samsung Galaxy Buds FE",
            brand="Samsung",
            category="Earbuds",
            description="Comfortable fit and active noise cancellation.",
            price=6999,
            stock_quantity=30
        ),

        # Laptops

        Product(
            product_name="Dell Inspiron 15",
            brand="Dell",
            category="Laptop",
            description="Intel Core i5 productivity laptop.",
            price=58999,
            stock_quantity=18
        ),

        Product(
            product_name="HP Victus Gaming",
            brand="HP",
            category="Laptop",
            description="RTX-powered gaming laptop.",
            price=79999,
            stock_quantity=10
        ),

        Product(
            product_name="Lenovo LOQ",
            brand="Lenovo",
            category="Laptop",
            description="Ryzen gaming laptop with RTX graphics.",
            price=72999,
            stock_quantity=14
        ),

        Product(
            product_name="Apple MacBook Air M3",
            brand="Apple",
            category="Laptop",
            description="Thin and lightweight laptop powered by Apple M3.",
            price=114999,
            stock_quantity=8
        )
    ]

    db.add_all(products)
    db.commit()

    print(f"{len(products)} products inserted successfully")

seed_products(db)