import time
import base64
import rsa
import binascii
import requests
import re
import random#微博涉及加密解密的一些 问题
try:
    from PIL import Image
except:
    pass
try:
    from urllib.parse import quote_plus
except:
    from urllib import quote_plus