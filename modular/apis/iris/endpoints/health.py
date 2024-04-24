


from fastapi import APIRouter
from ml_ops_24.modular.core.logger import logger

router = APIRouter()

@router.get('/status')
async def get_health():
    logger.info(f"Fetching user with ID: {23}")
    return {'status': 'ok'}


@router.get('/version')
async def get_version():
    return {'version': '0.1.0'}