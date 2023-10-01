from fastapi import FastAPI
from routers import *

app = FastAPI()
app.include_router(func.router)
app.include_router(func.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=9000)
