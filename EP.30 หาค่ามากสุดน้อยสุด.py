# หาค่ามากสุดและน้อยสุด 

Min,Max = 99999,0

while True:
    Number = int(input('ป้อนตัวเลข:'))
    # ออกจาก Loop
    if Number < 0:
        break
    if Number>Max:
        Max = Number
    if Number<Min:
        Min = Number
print('ค่าสูงสุด',Max)
print('ค่าต่ำสุด',Min)