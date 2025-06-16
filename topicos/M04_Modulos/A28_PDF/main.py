from pathlib import Path
from PyPDF2 import PdfReader
from PIL import Image
import io

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdf_original'
PASTA_NOVOS = PASTA_RAIZ / 'pdf_novo'

RELATORIO = PASTA_ORIGINAIS / 'focus.pdf'
PASTA_NOVOS.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO)
count = 0

for i, page in enumerate(reader.pages):
    for j, img in enumerate(page.images):
        try:
            image_bytes = img.data
            image_stream = io.BytesIO(image_bytes)
            pil_img = Image.open(image_stream)

            # Força a conversão, sem piedade
            pil_img = pil_img.convert("RGBA")

            output_file = PASTA_NOVOS / f"pagina_{i}_imagem_{j}.png"
            pil_img.save(output_file)
            count += 1

        except Exception as e:
            print(f"Falha na imagem {j} da página {i}: {e}")

print(f"Total de imagens salvas: {count}")
