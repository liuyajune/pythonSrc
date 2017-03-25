from PIL import Image,ImageFont,ImageDraw
import random

msgNum = str(int(random.randint(1,99)))
print(msgNum)

img1 = Image.open('img1.jpg')
w,h = img1.size
wdraw = w * 0.8
hdraw = h * 0.5
draw = ImageDraw.Draw(img1)  #创建图像
font = ImageFont.truetype('tahoma.ttf', 20) #载入数值的字体及大小
draw.text((wdraw, hdraw), msgNum,font= font, fill=(255, 33, 33))
img1.save('img2.png','png')
img1.show()