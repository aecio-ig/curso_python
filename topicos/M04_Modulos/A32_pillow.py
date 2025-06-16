## pillow é o photoshop do python
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORGINAL = ROOT_FOLDER/ 'transferir.jpg'
NEW_IMAGE = ROOT_FOLDER/ 'new.jpg'

pil_image = Image.open(ORGINAL)

width, heigth = pil_image.size

print(pil_image.size)

new_width  = 5
new_heigth = round(heigth * new_width / width)


new_image = pil_image.resize((new_width, new_heigth))
new_image.save(NEW_IMAGE)
