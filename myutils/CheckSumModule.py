#-*- coding:utf-8 -*-

from PIL import Image
from pytesser import *
from io import BytesIO
# import urllib.request as urllib2#
# headers = {}
# headers['User-Agent'] = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
# url = "https://jbt.sinoecare.net/getcaptcha.sl?temp=jbzvev8s"
#
# LoginRequest = urllib2.Request(url)
# try:
#     LoginResponse = urllib2.urlopen(LoginRequest)
# except urllib2.HTTPError as e:
#     LogModule.logger.error("timestamp >>" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#     LogModule.logger.error(url + "  was connected fail !")
#     LogModule.logger.error(e.code)
#     LogModule.logger.error(e.reason)
#
# # print (LoginResponse.read())
def CheckSum(img_url):
    # LoginResponse  = 验证码图片url
    im = Image.open(img_url)
    # im = Image.open(BytesIO(img_url))
    imgry = im.convert('L')  # 图片底色变灰
    # imgry.show()

    # 图片降噪
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    # out.show()

    checksum = image_to_string(out).strip()

    return checksum

# from PIL import Image
# import pytesser
# image = Image.open('E:\\workspace\\MyUtils\\getcaptcha.jpg')
# print (pytesser.image_file_to_string('E:\\workspace\\MyUtils\\getcaptcha.jpg'))
# print (pytesser.image_to_string(image))