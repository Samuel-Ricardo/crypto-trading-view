from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get('/')
def home():
    return 'Hello world'

app.include_router(router)