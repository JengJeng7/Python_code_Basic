# Type Conversion การแปลงชนิดข้อมูลหรือประเภทข้อมูล
x = 30
y = 3.14
z = "692"

print(type(x))
print(type(y))
print(type(z))

# การบวกเลขของตัวแปล
result = x+y
print(result)
# integer ไม่สามารถทำงานร่วมกับ String ได้ถ้ายังไม่แปลงก่อน 

# แปลง String เป็น integer 
# เช่น int(z)
result1 = x+int(z)
print(result1)

#แปลง integer เป็น String 
# เช่น str(x)
result2 = str(x)+ z
print (result2)

# แปลง String => Float
#เช่น float(z)
print (float(z))

#แปลง float => String
#เช่น str(y)
print (str(y))

#แปลง integer => float 
# เช่น float(x)
print (float(x))

#แปลง float => integer 
# เช่น int(y)
print (int(y))

# การกำหนดค่าอีกครั้ง
# เช่น x = 30 
# อยากเปลี่ยนเป็น String 
#  x = str(z)