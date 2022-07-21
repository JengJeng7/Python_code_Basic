#บังคับลูปอย่างเดียว หรือ ลูปตลอดเวลา

count = 0
while True:
    Num = int(input("ป้อนตัวเลข :"))  
    if Num == 0:
        print("จบโปรแกรม")
        break
    count+=1
    print("รอบที่ :",count)