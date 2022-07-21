# การต่อ Sttring หรือ ข้อความ = (Concatinate)

Fname = 'Teerapong'
Lname = 'Charoenram'
Age = '21'

#เชื่อมต่อ String 
Fullname = Fname + Lname + Age
print(Fullname)

# การต่อ String กับ String สามารถใช่เครื่องหมายบวกต่อกันได้
print('ชื่อต้น:'+Fname,'นามสกุล:'+Lname,'อายุ:'+Age)

# การต่อข้อความด้วย .format
text = 'ชื่อต้น :{0}\tนามสกุล :{1}\tอายุ :{2}' #{} = ระบุตำแหน่ง
print(text.format(Fname,Lname,Age))

# ต่อชื่อด้วยคำสั่ง ( .format )
print("ชื่อของฉัน {} {} ".format (Fname,Lname)) 
# อีกแบบ
print(f"My Name is",(Fname +  Lname))

# นับจำนวนคำในประโยคหรือคำที่ซ้ำกัน
Fruit = 'งงมาก ทำไม แลกเงินห้าบาท ได้แบงค์ร้อยมา ห้าใบ แบงค์ยี่สิบ ห้าใบ'
# คำสั่งคำ หรือ ประโยคซ้ำ
print(Fruit.count('ใบ'))
Bame = 'นายสุดท้าย สะดุดล้ม หัวฟาดกล้วย?'
# คำสั่งเช็คคำขึ้นต้น .startswith('คำที่เราจะเช็คในตัวแปลว่าคำขึ้นต้นคือคำนี้ใช่ไหม')
print('เช็คว่า นายสุดท้ายเป็นคำขึ้นต้นหรือไม่:',Bame.startswith('นายสุดท้าย'))

# นาย เป็นคำขึ้นต้นในตัวแปลBame หรือไม่
if Bame.startswith('นาย'):
    # yes
    print('ความเป็นชาย')
    # no
else:
    print('ระบุเพศไม่ได้?')

#คำสั่งเช็คคำลงท้าย .endswith('คำที่เราจะเช็คในตัวแปลว่าคำลงท้ายคือคำนี้ใช่ไหม')
print('เช็คว่า กล้วย?เป็นคำลงท้ายหรือไม่:',Bame.endswith('กล้วย?'))
# กล้วย? เป็นคำลงท้ายในตัวแปลBame หรือไม่
if Bame.endswith('กล้วย?'):
    # yes
    print('น่าจะเป็นกล้วย')
    # no
else:
    print('มันเป็นกล้วยจริงๆหรอ')