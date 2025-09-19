from fastapi import FastAPI
from api import api_pdf
from services.load_pdf import tarjar_pdf
app = FastAPI()

app.include_router(api_pdf.router, prefix="/v1")


if __name__ == '__main__':

    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    