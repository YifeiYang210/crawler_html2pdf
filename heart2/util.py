import cv2

# grey_img = cv2.imread("./tongtong2.png", 0)
# cv2.imshow("g", grey_img)
# ret, binary = cv2.threshold(grey_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
#
# cv2.imshow("d", binary)
# cv2.imwrite("./tongtong3.jpg",binary)
# cv2.waitKey(0)

import numpy as np

img = cv2.imread('./tongtong3.jpg')

suofanghou = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

# None是输出图像的尺寸大小，fx和fy是缩放因子
# cv2.INTER_CUBIC 是插值方法，一般默认为cv2.INTER_LINEAR
cv2.imwrite("./tongtong4.jpg",suofanghou)
# while (1):
#     cv2.imshow('suofanghou', suofanghou)
#     cv2.imshow('img', img)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()
