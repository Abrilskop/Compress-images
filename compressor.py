# Importamos la biblioteca
# pip install --upgrade Pillow

# Llamamos a la biblioteca
from PIL import Image

# Cargamos la img
image=Image.open("assets/img/car.jpg")

# Especificamos la calidad de compresion
quality = 50

# Guardamos la img con la calidad que detallamos
image.save("assets/img/car-compress.jpg", Optimized=True, quality=quality)