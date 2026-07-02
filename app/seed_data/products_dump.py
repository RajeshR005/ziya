# seed_products.py

from app.deps import SessionLocal
from app.models.product import Product

db=SessionLocal()
def seed_products(db):

    # products = [

    #     # Smartphones
    #     Product(
    #         product_name="Samsung Galaxy M35 5G",
    #         brand="Samsung",
    #         category="Smartphone",
    #         description="6.6-inch AMOLED display, 6000mAh battery, Exynos processor.",
    #         price=18999,
    #         stock_quantity=50
    #     ),

    #     Product(
    #         product_name="Samsung Galaxy S24",
    #         brand="Samsung",
    #         category="Smartphone",
    #         description="Premium flagship smartphone with Galaxy AI.",
    #         price=74999,
    #         stock_quantity=20
    #     ),

    #     Product(
    #         product_name="iPhone 15",
    #         brand="Apple",
    #         category="Smartphone",
    #         description="A16 Bionic chip and advanced dual-camera system.",
    #         price=69999,
    #         stock_quantity=15
    #     ),

    #     Product(
    #         product_name="iPhone 16",
    #         brand="Apple",
    #         category="Smartphone",
    #         description="Latest Apple smartphone with improved AI features.",
    #         price=79999,
    #         stock_quantity=12
    #     ),

    #     Product(
    #         product_name="OnePlus Nord CE 4",
    #         brand="OnePlus",
    #         category="Smartphone",
    #         description="120Hz AMOLED display with 100W fast charging.",
    #         price=24999,
    #         stock_quantity=40
    #     ),

    #     Product(
    #         product_name="Realme P3 5G",
    #         brand="Realme",
    #         category="Smartphone",
    #         description="Affordable 5G smartphone with powerful battery.",
    #         price=16999,
    #         stock_quantity=35
    #     ),

    #     Product(
    #         product_name="Redmi Note 14 Pro",
    #         brand="Xiaomi",
    #         category="Smartphone",
    #         description="200MP camera and AMOLED display.",
    #         price=21999,
    #         stock_quantity=30
    #     ),

    #     Product(
    #         product_name="Nothing Phone 3A",
    #         brand="Nothing",
    #         category="Smartphone",
    #         description="Unique transparent design with clean Android.",
    #         price=27999,
    #         stock_quantity=18
    #     ),

    #     # Headphones

    #     Product(
    #         product_name="Boat Rockerz 450",
    #         brand="Boat",
    #         category="Headphones",
    #         description="Wireless headphones with deep bass.",
    #         price=1499,
    #         stock_quantity=100
    #     ),

    #     Product(
    #         product_name="Sony WH-CH520",
    #         brand="Sony",
    #         category="Headphones",
    #         description="Bluetooth headphones with 50-hour battery.",
    #         price=4499,
    #         stock_quantity=40
    #     ),

    #     Product(
    #         product_name="JBL Tune 760NC",
    #         brand="JBL",
    #         category="Headphones",
    #         description="Noise cancelling wireless headphones.",
    #         price=5999,
    #         stock_quantity=25
    #     ),

    #     Product(
    #         product_name="Sennheiser HD 450BT",
    #         brand="Sennheiser",
    #         category="Headphones",
    #         description="Premium wireless headphones with ANC.",
    #         price=9999,
    #         stock_quantity=15
    #     ),

    #     # Earbuds

    #     Product(
    #         product_name="Boat Airdopes 311",
    #         brand="Boat",
    #         category="Earbuds",
    #         description="Budget TWS earbuds with ENC.",
    #         price=1299,
    #         stock_quantity=120
    #     ),

    #     Product(
    #         product_name="OnePlus Buds 3",
    #         brand="OnePlus",
    #         category="Earbuds",
    #         description="ANC-enabled premium earbuds.",
    #         price=5499,
    #         stock_quantity=50
    #     ),

    #     Product(
    #         product_name="Apple AirPods Pro 2",
    #         brand="Apple",
    #         category="Earbuds",
    #         description="Premium ANC earbuds with spatial audio.",
    #         price=23999,
    #         stock_quantity=12
    #     ),

    #     Product(
    #         product_name="Samsung Galaxy Buds FE",
    #         brand="Samsung",
    #         category="Earbuds",
    #         description="Comfortable fit and active noise cancellation.",
    #         price=6999,
    #         stock_quantity=30
    #     ),

    #     # Laptops

    #     Product(
    #         product_name="Dell Inspiron 15",
    #         brand="Dell",
    #         category="Laptop",
    #         description="Intel Core i5 productivity laptop.",
    #         price=58999,
    #         stock_quantity=18
    #     ),

    #     Product(
    #         product_name="HP Victus Gaming",
    #         brand="HP",
    #         category="Laptop",
    #         description="RTX-powered gaming laptop.",
    #         price=79999,
    #         stock_quantity=10
    #     ),

    #     Product(
    #         product_name="Lenovo LOQ",
    #         brand="Lenovo",
    #         category="Laptop",
    #         description="Ryzen gaming laptop with RTX graphics.",
    #         price=72999,
    #         stock_quantity=14
    #     ),

    #     Product(
    #         product_name="Apple MacBook Air M3",
    #         brand="Apple",
    #         category="Laptop",
    #         description="Thin and lightweight laptop powered by Apple M3.",
    #         price=114999,
    #         stock_quantity=8
    #     )
    # ]
    # seed_products_extra.py

    products = [

        # ========================= SMARTPHONES (new) =========================
        Product(product_name="Samsung Galaxy S24 Ultra", brand="Samsung", category="Smartphone",
                description="200MP camera, Snapdragon 8 Gen 3, built-in S Pen.",
                price=129999, stock_quantity=10),
        Product(product_name="iPhone 16 Pro Max", brand="Apple", category="Smartphone",
                description="A18 Pro chip, titanium body, and pro-grade camera system.",
                price=144999, stock_quantity=8),
        Product(product_name="OnePlus 12", brand="OnePlus", category="Smartphone",
                description="Snapdragon 8 Gen 3 flagship with Hasselblad cameras.",
                price=64999, stock_quantity=22),
        Product(product_name="Realme 13 Pro Plus", brand="Realme", category="Smartphone",
                description="Sony telephoto camera and curved AMOLED display.",
                price=32999, stock_quantity=28),
        Product(product_name="Xiaomi 14 Civi", brand="Xiaomi", category="Smartphone",
                description="Leica-tuned cameras with slim premium design.",
                price=42999, stock_quantity=20),
        Product(product_name="Google Pixel 8", brand="Google", category="Smartphone",
                description="Tensor G3 chip with best-in-class computational photography.",
                price=59999, stock_quantity=16),
        Product(product_name="Vivo V40 Pro", brand="Vivo", category="Smartphone",
                description="ZEISS optics and 3D curved AMOLED display.",
                price=41999, stock_quantity=24),
        Product(product_name="Motorola Edge 50 Pro", brand="Motorola", category="Smartphone",
                description="Curved pOLED display with 125W charging.",
                price=31999, stock_quantity=26),

        # ========================= LAPTOPS (new) =========================
        Product(product_name="Dell XPS 13", brand="Dell", category="Laptop",
                description="Premium ultrabook with InfinityEdge display.",
                price=124999, stock_quantity=9),
        Product(product_name="HP Pavilion 14", brand="HP", category="Laptop",
                description="Slim everyday laptop with Intel Core i5.",
                price=62999, stock_quantity=20),
        Product(product_name="Lenovo IdeaPad Slim 5", brand="Lenovo", category="Laptop",
                description="Ryzen 7 thin-and-light laptop for productivity.",
                price=64999, stock_quantity=17),
        Product(product_name="Apple MacBook Pro 14 M4", brand="Apple", category="Laptop",
                description="Pro-grade laptop with M4 Pro chip and Liquid Retina XDR.",
                price=199999, stock_quantity=6),
        Product(product_name="ASUS Vivobook 15", brand="Asus", category="Laptop",
                description="Intel Core i5 everyday laptop with slim design.",
                price=54999, stock_quantity=22),
        Product(product_name="ASUS Zenbook 14 OLED", brand="Asus", category="Laptop",
                description="Lightweight premium ultrabook with a stunning OLED display.",
                price=89999, stock_quantity=12),
        Product(product_name="ASUS ExpertBook B1", brand="Asus", category="Laptop",
                description="Durable business laptop with strong security features.",
                price=67999, stock_quantity=14),
        Product(product_name="ASUS ROG Strix G16", brand="Asus", category="Laptop",
                description="Intel Core i7 with RTX 4060 and 165Hz display.",
                price=134999, stock_quantity=8),
        Product(product_name="ASUS TUF Gaming F15", brand="Asus", category="Laptop",
                description="Military-grade durable gaming laptop with RTX 4050.",
                price=84999, stock_quantity=13),
        Product(product_name="ASUS ROG Zephyrus G14", brand="Asus", category="Laptop",
                description="Compact powerhouse with Ryzen 9 and RTX 4070.",
                price=164999, stock_quantity=6),
        Product(product_name="Acer Nitro 5", brand="Acer", category="Laptop",
                description="Affordable gaming laptop with RTX graphics and fast refresh.",
                price=76999, stock_quantity=15),
        Product(product_name="Acer Predator Helios Neo 16", brand="Acer", category="Laptop",
                description="High-performance gaming laptop with RTX 4070.",
                price=139999, stock_quantity=7),
        Product(product_name="MSI Katana 15", brand="MSI", category="Laptop",
                description="Intel Core i7 gaming laptop with RTX 4060.",
                price=109999, stock_quantity=9),
        Product(product_name="Lenovo Legion Pro 5", brand="Lenovo", category="Laptop",
                description="Ryzen 7 gaming beast with RTX 4070 and 240Hz display.",
                price=159999, stock_quantity=6),

        # ========================= HEADPHONES (new) =========================
        Product(product_name="Sony WH-1000XM5", brand="Sony", category="Headphones",
                description="Industry-leading noise cancellation and premium sound.",
                price=29999, stock_quantity=18),
        Product(product_name="Bose QuietComfort 45", brand="Bose", category="Headphones",
                description="Legendary comfort with world-class noise cancellation.",
                price=26999, stock_quantity=12),

        # ========================= EARBUDS (new) =========================
        Product(product_name="Nothing Ear (a)", brand="Nothing", category="Earbuds",
                description="Transparent design earbuds with rich ANC.",
                price=7999, stock_quantity=35),
        Product(product_name="Sony WF-C700N", brand="Sony", category="Earbuds",
                description="Compact noise cancelling earbuds with long battery.",
                price=8999, stock_quantity=28),

        # ========================= TABLETS =========================
        Product(product_name="Apple iPad Air M2", brand="Apple", category="Tablet",
                description="Powerful M2 tablet with 11-inch Liquid Retina display.",
                price=59999, stock_quantity=14),
        Product(product_name="Samsung Galaxy Tab S9", brand="Samsung", category="Tablet",
                description="AMOLED display tablet with S Pen included.",
                price=72999, stock_quantity=12),
        Product(product_name="OnePlus Pad 2", brand="OnePlus", category="Tablet",
                description="Snapdragon 8 Gen 3 tablet with 12.1-inch display.",
                price=39999, stock_quantity=18),
        Product(product_name="Xiaomi Pad 6", brand="Xiaomi", category="Tablet",
                description="144Hz display tablet for entertainment and productivity.",
                price=28999, stock_quantity=22),

        # ========================= SMARTWATCHES =========================
        Product(product_name="Apple Watch Series 10", brand="Apple", category="Smartwatch",
                description="Advanced health tracking with a larger display.",
                price=46999, stock_quantity=15),
        Product(product_name="Samsung Galaxy Watch 7", brand="Samsung", category="Smartwatch",
                description="Comprehensive health sensors with Wear OS.",
                price=31999, stock_quantity=18),
        Product(product_name="Noise ColorFit Pro 5", brand="Noise", category="Smartwatch",
                description="Affordable smartwatch with AMOLED display.",
                price=3499, stock_quantity=60),
        Product(product_name="Fire-Boltt Phoenix Pro", brand="Fire-Boltt", category="Smartwatch",
                description="Budget smartwatch with Bluetooth calling.",
                price=1999, stock_quantity=80),

        # ========================= MONITORS =========================
        Product(product_name="LG UltraGear 27", brand="LG", category="Monitor",
                description="27-inch 165Hz gaming monitor with 1ms response.",
                price=22999, stock_quantity=20),
        Product(product_name="Samsung Odyssey G5", brand="Samsung", category="Monitor",
                description="Curved QHD gaming monitor with 144Hz refresh.",
                price=25999, stock_quantity=16),
        Product(product_name="Dell UltraSharp U2723QE", brand="Dell", category="Monitor",
                description="4K IPS monitor with excellent color accuracy.",
                price=54999, stock_quantity=10),
        Product(product_name="ASUS TUF Gaming VG249Q", brand="Asus", category="Monitor",
                description="24-inch 165Hz IPS gaming monitor.",
                price=16999, stock_quantity=24),

        # ========================= KEYBOARDS & MICE =========================
        Product(product_name="Logitech MX Keys S", brand="Logitech", category="Keyboard",
                description="Wireless productivity keyboard with backlighting.",
                price=10999, stock_quantity=30),
        Product(product_name="Keychron K2 Mechanical", brand="Keychron", category="Keyboard",
                description="Compact wireless mechanical keyboard.",
                price=7999, stock_quantity=25),
        Product(product_name="Logitech G502 Hero", brand="Logitech", category="Mouse",
                description="High-performance gaming mouse with 25K DPI sensor.",
                price=3999, stock_quantity=45),
        Product(product_name="Razer DeathAdder V3", brand="Razer", category="Mouse",
                description="Ergonomic esports gaming mouse.",
                price=5499, stock_quantity=32),

        # ========================= GAMING CONSOLES =========================
        Product(product_name="Sony PlayStation 5", brand="Sony", category="Gaming Console",
                description="Next-gen console with ultra-high-speed SSD.",
                price=54990, stock_quantity=10),
        Product(product_name="Microsoft Xbox Series X", brand="Microsoft", category="Gaming Console",
                description="4K gaming console with 1TB storage.",
                price=52990, stock_quantity=9),
        Product(product_name="Nintendo Switch OLED", brand="Nintendo", category="Gaming Console",
                description="Hybrid console with vibrant 7-inch OLED screen.",
                price=34999, stock_quantity=15),

        # ========================= SPEAKERS =========================
        Product(product_name="JBL Flip 6", brand="JBL", category="Speaker",
                description="Portable waterproof Bluetooth speaker.",
                price=9999, stock_quantity=35),
        Product(product_name="Boat Stone 1200", brand="Boat", category="Speaker",
                description="Powerful outdoor Bluetooth speaker with RGB lights.",
                price=4499, stock_quantity=40),
        Product(product_name="Marshall Emberton II", brand="Marshall", category="Speaker",
                description="Iconic design portable speaker with rich sound.",
                price=16999, stock_quantity=14),

        # ========================= POWER BANKS =========================
        Product(product_name="Anker PowerCore 20000", brand="Anker", category="Power Bank",
                description="20000mAh power bank with fast charging.",
                price=3999, stock_quantity=50),
        Product(product_name="Mi Power Bank 3i 20000", brand="Xiaomi", category="Power Bank",
                description="Triple-port 20000mAh power bank with 18W output.",
                price=2199, stock_quantity=70),

        # ========================= TELEVISIONS =========================
        Product(product_name="Sony Bravia 55 4K", brand="Sony", category="Television",
                description="55-inch 4K Google TV with vivid picture quality.",
                price=79999, stock_quantity=8),
        Product(product_name="Samsung Crystal 4K 50", brand="Samsung", category="Television",
                description="50-inch 4K UHD smart TV with Tizen OS.",
                price=44999, stock_quantity=12),
        Product(product_name="LG OLED evo C4 55", brand="LG", category="Television",
                description="55-inch OLED TV with stunning contrast and webOS.",
                price=139999, stock_quantity=5),
        Product(product_name="Mi QLED TV 4K 55", brand="Xiaomi", category="Television",
                description="55-inch QLED smart TV with Dolby Vision.",
                price=52999, stock_quantity=10),

        # ========================= CAMERAS =========================
        Product(product_name="Canon EOS R50", brand="Canon", category="Camera",
                description="Mirrorless camera ideal for content creators.",
                price=64999, stock_quantity=10),
        Product(product_name="Sony Alpha ZV-E10", brand="Sony", category="Camera",
                description="Vlogging-focused mirrorless camera with 4K video.",
                price=58999, stock_quantity=11),
        Product(product_name="GoPro Hero 12 Black", brand="GoPro", category="Camera",
                description="Action camera with 5.3K video and HyperSmooth.",
                price=41999, stock_quantity=16),
    ]

   
    db.add_all(products)
    db.commit()

    print(f"{len(products)} products inserted successfully")

seed_products(db)