import cv2
import numpy as np

#グレースケールで読み込み
src = cv2.imread('./img/src.png', 0)
sign = cv2.imread('./img/sign.png', 0)

#元画像から最下位ビット成分を除去
for col in src:
    for comp in col:
        if comp%2:
            comp -= 1

#元画像の最下位ビットに追加画像の画素値を加算
for col, col1 in zip(src, sign):
    for comp, comp1 in zip(col, col1):
        if comp1!=0:
            comp += 1
            
cv2.imwrite('result.png', src)