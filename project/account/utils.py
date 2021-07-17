from django.core.files import File
from PIL import Image
from io import BytesIO
from pathlib import Path

image_types = {
    "jpg" : "JPEG",
    "jpeg" : "JPEG",
    "png" : "PNG"
}

def resize_image(image_field, width=300, height=300):
    """ Metóda na zmenu veľkosti obrázka """

    img = Image.open(image_field)
    if img.width > width or img.height > height:
        size = (width, height)
        img.thumbnail(size)

        img_filename = Path(image_field.file.name).name
        img_suffix = img_filename.split(".")[-1]
        img_format = image_types[img_suffix]

        # vytvorim si pomocny buffer do ktoreho ulozim obrazok
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        file_object = File(buffer)

        image_field.save(img_filename, file_object)
