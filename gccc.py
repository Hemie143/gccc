import requests
from io import open as iopen

url = 'http://geocheck.org/geo_inputchkcoord.php?gid=249971030fb-5db4-45f2-a4ec-2e2312ca63d9'

sess = requests.Session()
page = sess.get(url)

captcha = sess.get("http://geocheck.org/geocheck_captcha.php")
captcha_file = "C:/temp/cap.png"


with iopen(captcha_file, 'wb') as file:
    file.write(captcha.content)