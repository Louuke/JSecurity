from fastapi import APIRouter, HTTPException, status
from jsecurity_api.model.request import LoginRequest
from jsecurity_service.dependencies import get_settings

router = APIRouter()

SECRET_KEY = get_settings().SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES = get_settings().ACCESS_TOKEN_EXPIRE_MINUTES
ALGORITHM = 'HS256'


@router.post('/login')
async def login(request: LoginRequest):
    username = request.username
    password = request.password

    if not await authenticate_user(username, password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return {'message': 'Login successful'}


async def authenticate_user(username: str, password: str) -> bool:
    return True
