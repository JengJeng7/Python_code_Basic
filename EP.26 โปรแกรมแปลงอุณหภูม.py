# โปรแกรมแปลงอุหภูมิ
#Celsius & Fahrenheit

#แปลง อุณหภูมิ
Temp = (input('ป้อนอุณหภูมิ(องศา):'))
Degree = int(Temp[:-1]) # เอาเฉพาะตัวเลข
Unit = Temp[-1].upper() # เอาเฉพาะสัญลักษณ์องศา

if Unit == 'C':
    #แปลง Celsius เป็น Celsius
    #F = (C*9/5)+32
    result = (Degree*9/5)+32
    Unit_result = 'ฟาเรนไฮน์'
if Unit == 'F':
    # แปลง  Fahrenheit เป็น Celsius
    #C = (F-32)*5/9
    result = (Degree-32)*5/9
    Unit_result = 'เซลเซียส'
print('อุณหภูมิ:',result,'องศา',Unit_result)