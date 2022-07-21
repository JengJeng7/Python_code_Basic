# ตัวเลขแบบขั้นบรรได
'''
ตัวอย่าง
input = 10
ถ้าป้อนเป็นเลข 10 มันจะทำ 10 รอบแบบขั้นบรรได เช่น
1
12
123 
1234
12345
123456
1234567
12345678
123456789
12345678910
'''
 
Last = int(input("ป้อนตัวเลข:"))
for Row in range(Last+1):
    for Column in range(1,Row+1):
      print(Column,end=' ') #  end= คือ ทำให้แสดงผลในแนวนอน
    print('')


'''
input = 3 เท่ากับให้วนตัวแปร Row 3 รอบ
รอบที่1 
Row = 1
Coulum = 1,Row+1
    print (Column, end=' ') 
print (' ') คือ แสดงผลColumn ให้อยู่ในแนวนอน
ผลลัพธ์ = 1

รอบที่ 2 
Row = 2 
Column = 1,Row+1
 print (Column, end=' ') 
print (' ') 
ผลลัพธ์ = 1
         1 2

รอบที่ 3
Row = 3 
Column = 1,Row+1
 print (Column, end=' ') 
print (' ') 
ผลลัพธ์ = 1
         1 2
         1 2 3
'''
