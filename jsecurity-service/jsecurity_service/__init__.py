from fastapi import FastAPI
import jsecurity_service.router.login as main
import logging

__version__ = '0.0.1'
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title='JSecurity API', version=__version__)
app.include_router(main.router)
