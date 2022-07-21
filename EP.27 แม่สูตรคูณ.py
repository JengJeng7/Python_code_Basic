# แม่สูตรคูณ

# แสดงแม่สูตรคูณ 2,3,4,5....
# 2x1......2x12 , 3x1.....3x12.......

Start = int(input('ป้อนสูตรคูณเริ่มต้น:'))
Stop = int(input('ป้อนสูตรคูณสุดท้าย:'))

for x in range(Start,Stop+1):
    print('แม่:',x)
    for y in range(1,13):
        print(x,'x',y,'=',x*y)


