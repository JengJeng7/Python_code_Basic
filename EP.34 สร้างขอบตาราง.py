# สร้างขอบตาราง 
'''
ตัวอย่าง 

xxxxx
x   x
x   x
x   x
x   x
xxxxx  

'''
Number = int(input('ป้อนขนาด :'))
for Row in range(Number):
    for Column in range(Number):
        if Row == 0 or Row == Number-1 or Column == 0 or Column == Number-1:
            print('X',end=" ")
        else:
            print(' ',end=" ")
    print(' ')


'''
input = 3
รอบที่ 1 
Row = 0 Column = 0,3
ถ้า Row == 0 หรือ Row == 3-1 หรือ Column == 0 หรือ Column == 3-1
ให้แสดงผล XXXXX

รอบที่ 2 
Row = 1 Column = 0,5
ถ้า Row == 0 หรือ Row == 5-1 หรือ Column == 0 หรือ Column == 5-1
ให้แสดงผล X   X

รอบที่ 3
Row = 2 Column = 0,5
ถ้า Row == 0 หรือ Row == 5-1 หรือ Column == 0 หรือ Column == 5-1
ให้แสดงผล XXXXX
'''
