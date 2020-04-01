import cv2
import numpy as np
from urllib.request import urlopen, Request
import io

def process_image(avatar_url,readFlag=cv2.IMREAD_COLOR):
    # req = Request('https://cdn.discordapp.com/avatars/163352834572681216/e17aca9ec772c87ab12918b203a16c7f.webp', headers = {"User-Agent": "Mozilla/5.0"})
    # resp = urlopen(req)
    resp = urlopen('http://hotdog.tylerchase.sexy/static/img/e865059.png')
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)
    response,buffer = cv2.imencode(".jpg",image)
    # decode_img = cv2.imdecode(np.frombuffer(io_buff.getbuffer(), np.uint8),-1)
    # img = np.ones((100, 100), np.uint8)

    # is_success, buffer = cv2.imencode(".jpg", img)
    io_buf = io.BytesIO(buffer)
    # decode
    # decode_img = cv2.imdecode(np.frombuffer(io_buf.getbuffer(), np.uint8), -1)
    
    return io_buf
