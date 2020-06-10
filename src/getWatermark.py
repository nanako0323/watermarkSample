import cv2
import numpy as np

#グレースケールで読み込み
src = cv2.imread('result.png', 0)

rect = list()

# #元画像から最下位ビット成分を取得
for col in src:
    newRow = list()
    for row in col:
        if row%2:
            newRow.append(0)
        else:
            newRow.append(255)
    
    rect.append(newRow)

img = np.array(rect)
    
cv2.imwrite('watermark.png', img)
