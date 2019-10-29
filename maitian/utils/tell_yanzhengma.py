import pytesseract
from PIL import Image

im = Image.open("D:/checkcodeimg/chinatimes/code0.gif")
# img.show()
# img.convert("RGB")
# img.show()
# while 1:
#     current = img.tell()
#     with open("D:/checkcodeimg/chinatimes/code0.jpg","wb") as f:
#         img.save(f)
#     print(img)
#     pytesseract.image_to_string(Image.open("D:/checkcodeimg/chinatimes/code0.jpg"),lang="eng")

try:
  while True:
    #保存当前帧图片
    current = im.tell()
    help(im.tell)
    im.save('d:/'+str(current)+'.png')
    #获取下一帧图片
    im.seek(current+1)
except EOFError:
    pass