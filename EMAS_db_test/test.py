import random;
import psycopg2;
import schedule;
import json;
import time;
from datetime import datetime;
from PIL import Image, ImageFont, ImageDraw;
import os;

index = datetime.now()
text = f"testing text, 4 birds, \n'{index}'"
im = Image.new("RGB", (320,320), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 14)
dr.text((10, 5), text, font=font, fill="#000000")
im.show()
current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
file_name = f"image_{current_time}.jpg"
path = os.path.join(os.getcwd(), "images", file_name)
im.save(path,'JPEG')