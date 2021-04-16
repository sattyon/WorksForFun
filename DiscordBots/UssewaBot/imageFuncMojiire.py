from PIL import ImageDraw
from PIL import ImageFont

def add_text_to_image(img, text, font_path, font_size, font_color, height, width, max_length=740):
    position = (width, height)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    draw.text(position, text, font_color, font=font)
    return img