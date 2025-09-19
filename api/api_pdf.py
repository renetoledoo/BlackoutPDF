from fastapi import APIRouter,  Request
from schemas.pdf_schema import PdfBody, PdfResponse
from fastapi.responses import FileResponse
from core.config import settings
from services.load_pdf import tarjar_pdf, download_pdf
from pathlib import Path

router = APIRouter()


@router.post("/", description="Receber PDF parequest: Requestra processamento", response_model=PdfResponse)
async def processing_pdf(body: PdfBody,request: Request ):

    url_arq = body.path

    path_arq = download_pdf(url_arq)
    pdf = tarjar_pdf(path_arq)

    if pdf is None:
        return PdfResponse(url=None, status=False)
    
    filename = pdf
    file_url = f"{request.base_url}v1/files/{filename}"
    response = PdfResponse(url=file_url, status=True)
    
    return response


@router.get("/files/{filename}")
async def get_file(filename: str):
    file_path = settings.UPLOAD_DIR / filename
    if file_path.exists():
        return FileResponse(file_path)
    return {"error": "File not found"}