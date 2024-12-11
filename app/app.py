import uvicorn

from fastapi import FastAPI
from mangum import Mangum
from app.api.v1 import users, orders, products
from app.core.logging import setup_logging

logger = setup_logging()

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(products.router, prefix="/products", tags=["Products"])


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    logger.info(f"Health check has been requested")
    return {"status": "healthy"}


handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)