from PIL import Image
import numpy as np
image = Image.open('C:/Users/10920/Desktop/image.jpg') 
# image.show()    
image_array = np.array(image)

# 将彩色图像转为灰度图片
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [1/3, 1/3, 1/3])

h_list = rgb2gray(image_array)
m_mat = np.array(h_list)
f = m_mat.reshape(image_array.shape[0],image_array.shape[1])

img = Image.fromarray(f.astype('uint8')).convert('L')
img.show()