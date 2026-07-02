# from app.db.session import SessionLocal
# from app.models.review import Review
# from app.models.product import Product
# import random

# db = SessionLocal()

# # Category-specific review pools (kept short to save space)
# review_pools = {
#     "Smartphone": [
#         "Battery easily lasts a full day.",
#         "Camera quality is excellent in daylight.",
#         "Smooth performance, no lag at all.",
#         "Display is bright and vibrant.",
#         "Great phone for the price.",
#         "Fast charging is a lifesaver.",
#     ],
#     "Laptop": [
#         "Handles multitasking effortlessly.",
#         "Build quality feels premium.",
#         "Great performance for work and study.",
#         "Display is crisp and clear.",
#         "Battery backup is impressive.",
#         "Runs cool even under load.",
#     ],
#     "Headphones": [
#         "Sound quality is rich and balanced.",
#         "Noise cancellation works really well.",
#         "Very comfortable for long sessions.",
#         "Battery life is fantastic.",
#         "Bass is deep and punchy.",
#         "Great build and premium feel.",
#     ],
#     "Earbuds": [
#         "Perfect fit and very comfortable.",
#         "Crisp audio with solid bass.",
#         "ANC is surprisingly effective.",
#         "Case is compact and pocket-friendly.",
#         "Battery lasts through the day.",
#         "Great value for the sound quality.",
#     ],
#     "Tablet": [
#         "Display is perfect for streaming.",
#         "Smooth and responsive to use.",
#         "Great for note-taking and reading.",
#         "Battery lasts really long.",
#         "Lightweight and easy to carry.",
#         "Excellent performance for the price.",
#     ],
#     "Smartwatch": [
#         "Health tracking is accurate.",
#         "Display is bright and clear.",
#         "Battery lasts several days.",
#         "Comfortable to wear all day.",
#         "Great range of watch faces.",
#         "Notifications work seamlessly.",
#     ],
#     "Monitor": [
#         "Colors are vivid and accurate.",
#         "High refresh rate feels buttery smooth.",
#         "Great for both work and gaming.",
#         "Slim bezels look premium.",
#         "No dead pixels, crisp display.",
#         "Excellent value for the specs.",
#     ],
#     "Keyboard": [
#         "Typing feels smooth and satisfying.",
#         "Build quality is solid.",
#         "Keys are responsive and quiet.",
#         "Backlighting looks great.",
#         "Comfortable for long typing sessions.",
#         "Connects instantly every time.",
#     ],
#     "Mouse": [
#         "Tracking is precise and smooth.",
#         "Very comfortable grip.",
#         "Buttons feel responsive.",
#         "Great for both work and gaming.",
#         "Build quality is excellent.",
#         "Battery/connection is reliable.",
#     ],
#     "Gaming Console": [
#         "Games load incredibly fast.",
#         "Graphics are stunning.",
#         "Controller feels great in hand.",
#         "Setup was quick and easy.",
#         "Runs quiet and cool.",
#         "Best gaming experience so far.",
#     ],
#     "Speaker": [
#         "Sound is loud and clear.",
#         "Bass is powerful for the size.",
#         "Battery lasts for hours.",
#         "Build feels rugged and durable.",
#         "Perfect for outdoor use.",
#         "Great value for the audio quality.",
#     ],
#     "Power Bank": [
#         "Charges my devices quickly.",
#         "Compact yet high capacity.",
#         "Holds charge for a long time.",
#         "Build quality is sturdy.",
#         "Multiple ports are very handy.",
#         "Reliable and worth the money.",
#     ],
#     "Television": [
#         "Picture quality is stunning.",
#         "Colors are vivid and lifelike.",
#         "Smart features work smoothly.",
#         "Great sound out of the box.",
#         "Slim design looks premium.",
#         "Excellent value for a 4K TV.",
#     ],
#     "Camera": [
#         "Image quality is outstanding.",
#         "Autofocus is fast and accurate.",
#         "Great for video and photos.",
#         "Compact and easy to carry.",
#         "Battery life is decent.",
#         "Perfect for content creation.",
#     ],
# }

# # Fallback pool for any category not listed above
# default_pool = [
#     "Excellent product for the price.",
#     "Works exactly as advertised.",
#     "Very satisfied with this purchase.",
#     "Great value for money.",
#     "Highly recommended.",
#     "Reliable and well-built.",
# ]

# REVIEWS_PER_PRODUCT = 3


# def seed_reviews():
#     reviews = []

#     products = db.query(Product.id, Product.category).all()

#     for product_id, category in products:
#         pool = review_pools.get(category, default_pool)
#         # pick distinct reviews (won't exceed pool size)
#         texts = random.sample(pool, min(REVIEWS_PER_PRODUCT, len(pool)))

#         for text in texts:
#             reviews.append(Review(
#                 product_id=product_id,
#                 user_id=1,  # dummy user
#                 rating=round(random.uniform(3.8, 5.0), 1),
#                 review_text=text
#             ))

#     db.add_all(reviews)
#     db.commit()
#     print(f"{len(reviews)} reviews inserted successfully")


# if __name__ == "__main__":
#     seed_reviews()

from app.db.session import SessionLocal
from app.models.product import Product
from app.models.review import Review
from sqlalchemy import func

db = SessionLocal()

products = db.query(Product).all()

for product in products:

    avg_rating = (
        db.query(func.avg(Review.rating))
        .filter(Review.product_id == product.id)
        .scalar()
    )

    product.average_rating = round(float(avg_rating), 1)

db.commit()

print("Average ratings updated successfully")