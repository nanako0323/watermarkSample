import cv2
import numpy as np

#グレースケールで読み込み
src = cv2.imread('./img/src.png', 0)
sign = cv2.imread('./img/sign.png', 0)

origin = list()

#元画像から最下位ビット成分を除去
for col in src:
    row = list()
    for comp in col:
        if comp%2:
            row.append(comp -1)
        else:
            row.append(comp)
    origin.append(row)

output = list()

#元画像の最下位ビットに追加画像の画素値を加算
for col, originCol in zip(sign, origin):
    newRow = list()
    for row, originRow in zip(col, originCol):
        if row == 0:
            newRow.append(originRow + 1)
        else:
            newRow.append(originRow)
    output.append(newRow)    
    
img = np.array(output)

cv2.imwrite('result.png', img)