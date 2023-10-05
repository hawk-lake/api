from fastapi import FastAPI
# from router import *
from router.test import router as test

app = FastAPI()
# app.include_router(func.router)
# app.include_router(func.router)
app.include_router(test)

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host='0.0.0.0', port=9000)
    uvicorn.run(app='main:app', host='0.0.0.0', port=9000)