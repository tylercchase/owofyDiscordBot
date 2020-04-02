import cv2
import numpy as np
from urllib.request import urlopen, Request
import io
from random import choice
def process_image(avatar_url,readFlag=cv2.IMREAD_COLOR):
    #get and download image to memory
    req = Request(avatar_url, headers = {"User-Agent": "Mozilla/5.0"})
    resp = urlopen(req)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)
    image = cv2.resize(image, (110,110))

    #Add pink overlay
    overlay = image.copy()
    cv2.rectangle(overlay,(0,0),(200,200),(221, 50, 230),-1)
    opacity = 0.5
    cv2.addWeighted(overlay,opacity,image, 1 - opacity, 0, image)

    petals = cv2.imread("petals.png")
    petals = cv2.resize(petals, (110,110))
    final = cv2.addWeighted(image,1,petals,0.5,1)
    
    response, buffer = cv2.imencode(".png",final)

    io_buf = io.BytesIO(buffer)

    return io_buf

def owoify_text(text):
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω´・)', '(´・ω・`)']
    words = text.split()
    first_letter = words[0][0]
    letter_stutter = f"{first_letter}-{first_letter.lower()}-{first_letter.lower()}"
    if len(words[0]) > 1:
        words[0] = letter_stutter + words[0][1:]
    else:
        words[0] = letter_stutter
    text = " ".join(words)
    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')
    text = '! {}'.format(choice(smileys)).join(text.rsplit('!', 1))
    text = '? OwO'.join(text.rsplit('?', 1))
    text = '. {}'.format(choice(smileys)).join(text.rsplit('.', 1))
    text = f"{text} desu"
    for v in ['a', 'o', 'u', 'A', 'O', 'U']:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))
    return text