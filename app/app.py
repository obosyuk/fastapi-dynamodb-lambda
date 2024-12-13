import uvicorn

from fastapi import FastAPI, Request
from mangum import Mangum
from app.api.v1 import users, orders, products, secure_routes
from app.core.logging import setup_logging

logger = setup_logging()

app = FastAPI()

# @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
# async def catch_all(request: Request, path: str):
#     """
#     Catch-all endpoint to capture all requests and return metadata.
#     """
#     return {
#         "method": request.method,
#         "path": path,
#         "headers": dict(request.headers),
#         "query_params": dict(request.query_params),
#         "body": (await request.body()).decode("utf-8") if request.method in ["POST", "PUT", "PATCH"] else None,
#         "client": request.client.host
#     }

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(secure_routes.router, prefix="/secure")


@app.get("/", tags=["Hello"])
async def health_check():
    logger.info(f"Hello endpoint has been requested")
    return {"detail": "Hello from FastAPI"}


handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
