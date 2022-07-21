# สร้างตารางหมากฮอต
# 8 x 8
# X = สีน้ำตาล
# O = สีขาว 
Number = int(input('ป้อนขนาด :'))
for Row in range(Number):
    for Column in range(Number):
        if (Row+Column) % 2 == 0:
            print('X',end=" ")
        else:
            print('O',end=" ")
    print(' ')

'''
input = 5 
5 x 5
รอบที่ 1 
Row = 0 + Column = 0 = 0
Row = 0 + Column = 1 = 1
Row = 0 + Column = 2 = 2
Row = 0 + Column = 3 = 3 
Row = 0 + Column = 4 = 4

รอบที่ 2
Row = 1 + Column = 0 = 1
Row = 1 + Column = 1 = 2
Row = 1 + Column = 2 = 3
Row = 1 + Column = 3 = 4 
Row = 1 + Column = 4 = 5

รอบที่ 3
Row = 2 + Column = 0 = 2
Row = 2 + Column = 1 = 3
Row = 2 + Column = 2 = 4
Row = 2 + Column = 3 = 5 
Row = 2 + Column = 4 = 6
'''
'''
รอบที่ 1 
X O X O X 
รอบที่ 2 
O X O X O
รอบที่ 3 
X O X O X
'''