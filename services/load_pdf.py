import fitz
import requests
import os

from urllib.parse import urlparse
from core.config import settings

from ner.Reconhecimento import DetectorSimples


def download_pdf(pdf_url: str, filename: str = "arquivo.pdf") -> bool:
    try:
            # Extrai o nome do arquivo a partir da URL
            parsed_url = urlparse(pdf_url)
            filename = os.path.basename(parsed_url.path)

            if not filename:  # fallback se URL não tiver nome
                filename = "arquivo.pdf"

            # Caminho final dentro da pasta de upload
            file_path = settings.UPLOAD_DIR / filename

            # Baixa o PDF
            response = requests.get(pdf_url, timeout=30)
            response.raise_for_status()

            with open(file_path, "wb") as f:
                f.write(response.content)

            return file_path

    except Exception as e:
            print(f"Erro ao baixar PDF: {e}")
            return None
    


def tarjar_pdf(pdf_path: str) -> bool | None:

    if not pdf_path.exists():
        return None

    analyzer = DetectorSimples()
    doc_ref = None

    try:
        doc_ref = fitz.open(pdf_path)

        for page in doc_ref:
            try:
                texto = page.get_text()
            except Exception:
                continue  # pula página se não conseguir extrair texto

            try:
                result = analyzer.analyze(text=texto, entities=["CPF", "PERSON"], language='pt')
                print(result)
            except Exception:
                continue  # pula página se NER falhar

            for ner in result:
                if ner.score >= 0.85:
                    try:
                        nome = texto[ner.start:ner.end]
                        rects = page.search_for(nome)
                        for rect in rects:
                            page.draw_rect(rect, color=(0,0,0), fill=(0,0,0))
                    except Exception:
                        continue  # pula entidade se falhar

        settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        dir_final = settings.UPLOAD_DIR / f"tajardo_{pdf_path.name}"

        doc_ref.save(dir_final)
        return f"tajardo_{pdf_path.name}"

    except Exception:
        return None

    finally:
        if doc_ref is not None:
            doc_ref.close()