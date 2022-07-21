# break / continue

# Break = คำสั่งหยุดการทำงาน หรือ จบการวนลูป
i = 1
while i <= 10:
    print("รอบที่:",i)
    # ถ้า i เท่ากับ 5 
    if i == 5:
    # จะทำให้คำสั่ง break ทำงาน และจะหยุดการทำงานทั้งหมด
     break
    i+=1
print("จบโปรแกรม ของคำสั่ง break While")

for i in range (1,11):
    if i == 6:
        break
    print("รอบที่:",i)
print("จบโปรแกรม ของคำสั่ง break For ")


# continue = คำสั่งกระโดดข้าม 1 บรรทัด
i = 0
while i <= 10:
    i+=1
    # ถ้า i เท่ากับ 5 
    if i%2 != 0:
        # จะทำให้คำสั่ง continue ทำงาน และจะกระโดดข้าม  print("รอบที่:",i)  1 ครั้ง
       continue
    print("รอบที่:",i)
print("จบโปรแกรม ของคำสั่ง continue While")

for i in range (1,11):
    if i%2 == 0:
        continue
    print("รอบที่:",i)
print("จบโปรแกรม ของคำสั่ง continue For ")

