from aip import AipOcr
"""此处使用的是百度的api 登录为手机验证码登录，首先将pdf转成jpeg格式使用wand或者pdf2image 然后将图片传到zpi指定url等待返回结果，然后根据要求将传回文字存入数据库"""
""" 你的 APPID AK SK """
APP_ID = '17554399'
API_KEY = 'IBBRGZGGSzXtmwxM2UjeA7uf'
SECRET_KEY = 'IrQdqfCgl1zBsZOgdswGsEeqQl5vTUBw'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# image = get_file_content('F:/桌面简历等重要文件/简历旧版面001.pdf')
image = get_file_content('d:/ok.jpg')
""" 调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
a = client.basicGeneral(image, options)
#
# url = "http//www.x.com/sample.jpg"
#
# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# a = client.basicGeneralUrl(url, options)
# use baidu api tell pdf
print(a)
"# nothing important" 
