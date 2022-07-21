# สร้างตัวเลข 4 เหลี่ยมจตุรัส
'''
เหลี่ยมจตุรัส  = ด้าน x ด้าน
เช่น 
3x3
xxx
xxx
xxx

4x4
xxxx
xxxx
xxxx
xxxx

'''

Number = int(input('ป้อนขนาด :'))
for Row in range(Number):
    for Column in range(Number):
        print('X',end=" ")
    print(' ')