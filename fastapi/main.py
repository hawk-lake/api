from fastapi import FastAPI
from router import load_datas, to_hdfs

app = FastAPI()
app.include_router(load_datas.router)
app.include_router(to_hdfs.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=4000)
