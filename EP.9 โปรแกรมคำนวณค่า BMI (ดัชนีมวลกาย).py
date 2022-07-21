 # โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนวสูง ()

# input ถ้าจะรับตัวเลขเข้ามาทำงานต้องแปลงจาก String เป็น Integer
weight = int (input("ป้อนน้ำหนัก (kg) :"))
hight = int (input("ป้อนส่วนสูง (cm) :"))

# process = กระบวนการ
#ต้องแปลง cm เป็น m ก่อนด้วยการเอา 100 มาหารส่วนสูง
hight/= 100
#คำนวณ
bmi = weight//(hight*hight) 

#output
print("BMI = ",bmi)

if bmi <= 18:
    result = ('ต่ำกว่าเกณฑ์')
elif bmi >= 18.5 and bmi <= 22.9:
    result = ('สมส่วน')
elif bmi >= 23 and bmi <= 24.9:
    result = ('น้ำหนักเกิน')
elif bmi >= 25 and bmi <=29.9:
    result = ('โรคอ้วนระดับ 1')
elif bmi<30:
    result = ('โรคอ้วนระดับอันตราย')
else:
    result = ('ไม่ทราบค่าที่ชัดเจน')
print('ผลคือ',result)
    