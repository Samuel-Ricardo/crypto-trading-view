from fastapi import FastAPI, APIRouter
from routes._ import user_router, crypto_routes
app = FastAPI()
router = APIRouter()

@router.get('/')
def home():
    return 'Hello world'

app.include_router(router)
app.include_router(user_router)
app.include_router(crypto_routes)