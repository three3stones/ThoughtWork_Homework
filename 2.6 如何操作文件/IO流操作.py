import requests
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

src = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
r = requests.get(src)   # 下载图片
img = Image.open(BytesIO(r.content))        # BytesIO读取图片内容
plt.imshow(img)         # 显示图片
plt.axis('off')         # 不显示坐标轴
plt.show()
