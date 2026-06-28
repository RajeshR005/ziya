# from app.db.session import SessionLocal
# from app.models.review import Review
# import random

# db = SessionLocal()

# review_templates = [
#     "Excellent product for the price.",
#     "Battery life is impressive.",
#     "Performance exceeded expectations.",
#     "Build quality feels premium.",
#     "Would definitely recommend.",
#     "Value for money product.",
#     "Display quality is excellent.",
#     "Works exactly as advertised.",
#     "Very satisfied with the purchase.",
#     "Good quality and reliable.",
#     "Fast delivery and good packaging.",
#     "Worth every rupee spent.",
#     "Amazing experience so far.",
#     "Highly recommended for daily use.",
#     "Premium feel and great performance.",
#     "Customer support was helpful.",
#     "Looks stylish and modern.",
#     "Perfect for my requirements.",
#     "No issues after weeks of usage.",
#     "One of the best purchases I've made."
# ]


# def seed_reviews():

#     reviews = []

#     # 20 products
#     for product_id in range(1, 21):

#         # 5 reviews per product
#         for _ in range(5):

#             review = Review(
#                 product_id=product_id,
#                 user_id=1,  # dummy user
#                 rating=round(random.uniform(3.8, 5.0), 1),
#                 review_text=random.choice(review_templates)
#             )

#             reviews.append(review)

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