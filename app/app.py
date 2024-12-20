import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.api.v1 import orders, products, secure_routes, users
from app.core.logging import setup_logging

logger = setup_logging()

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(secure_routes.router, prefix="/secure")


@app.get("/", tags=["Hello"])
async def health_check():
    logger.info("Hello endpoint has been requested")
    return {"detail": "Hello from FastAPI"}


handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
