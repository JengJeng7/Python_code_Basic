'''คำสั่ง ''' ''' นี้ใช้แสดงคำอธิบาย
ข้อความยาวหลายบรรทัด'''
#คำสั่งที่แสดงทางจอภาพ
# คำสั่ง print ใช้สำปรับแสดงผลข้อความหรือแสดงผลข้อมูลออกทางจอภาพได้ทุกชนิด
print("Hello World")
print('Teerapong')
#String = ข้อความ ตัวอักษร จะทำงานภายใน, ' ' , " " รวมไปถึง '''
#number = integer(จำนวนเต็ม), float(ทศนิยม) 
#Boolean = True,False
#Single quote = (' ')  Double quote = (" ")
print("-1 + -1")  #มันคือข้อความ เพราะใส่ single quote หรือ double quote
print(10+1) #แต่อันนี้มันคือบวกกันเลย 
print(1)
print(True)
print(False)

# ตัว \t = ตัวเว้นระยะห่าง
# ตัว \n = ตัวขึ้นบรรทัดใหม่
print("Teerapong\t"+"Charoenram")
print("Teerapong \n"+ "Charoenram")

#การสร้างตัวแปล
# Data Type & Variable
# ชื่อตัวแปร = ค่าที่เก็บในตัวแปล เช่น X = 10
x = 10 #integer = จำนวนเต็ม,ตัวเลข
y = 3.99 #float = เลขทศนิยม
z = True #Boolean = เป็นจริงหรือเท็จ
print(y)
print(z)
print(str(x)) #แปลงค่า integer ให้เป็น String โดยใช้ str

#การหาค่าชนิดข้อมูลในตัวแปลหรือข้อมูลอื่นๆโดยใช้ type เช่น print(type(y))
print(type(x))
