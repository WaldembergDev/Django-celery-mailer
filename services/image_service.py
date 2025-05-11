from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import Path
from io import BytesIO

def save_image(name: str):
    # obtendo o first_name
    first_name = name.split(sep=' ')[0]
    # caminho da imagem
    path_image = Path('templates/image/convite.png')
    # caminho da fonte
    path_font = Path('templates/image/Pillow.otf')

    # abrindo a imagem e desenhando o texto
    image = Image.open(path_image)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(path_font, 20)
    draw.text((20, 75), first_name, font=font, fill='black')

    # salvando a imagem na memória
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    
    return buffer

