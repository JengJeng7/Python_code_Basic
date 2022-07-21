# หาผลรวม และ ค่าเฉลี่ย

Start = 1
Stop = 3
Sum = 0


while (Start<= Stop):
    Number = int(input("ป้อนตัวเลขของคุณ: "))
    Sum+=Number #บวกเลขที่ป้อนในแต่ละรอบ
    Start += 1

Avg = Sum/Stop #ค่าเฉลี่ย
print("ผลรวมเลขที่ป้อนเข้ามา:",Sum)
print("ค่าเฉลี่ยของเลขที่ป้อนเข้ามา:",Avg)

# แบบไม่ระบุจำนวนรอบที่จัดเจน

Sum = 0
while Sum <= 220:
    Number = int(input("ป้อนตัวเลขของคุณ: "))
    Sum+=Number #บวกเลขที่ป้อนในแต่ละรอบ
    print("ผลรวมเลขที่ป้อนเข้ามา While:",Sum)

Sum = 0
while True:
    Number = int(input("ป้อนตัวเลขของคุณ: "))
    Sum+=Number #บวกเลขที่ป้อนในแต่ละรอบ
    if Sum>=200:
        break
    print("ผลรวมเลขที่ป้อนเข้ามา While True:",Sum)


