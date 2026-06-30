from app.api import login,register_user,all_products,one_product,filter_products,category_api,brands_api,top_rated,add_cart,show_orders,get_reviews,cart_update,chat
from fastapi import APIRouter

api_router=APIRouter(prefix='/ziya')

api_router.include_router(register_user.router)
api_router.include_router(login.router)
api_router.include_router(all_products.router)
api_router.include_router(one_product.router)
api_router.include_router(filter_products.router)
api_router.include_router(category_api.router)
api_router.include_router(brands_api.router)
api_router.include_router(top_rated.router)
api_router.include_router(add_cart.router)
api_router.include_router(show_orders.router)
api_router.include_router(get_reviews.router)
api_router.include_router(cart_update.router)
api_router.include_router(chat.router) 