import numpy as np
# Function ของ Array

# 1D
Array1D = np.array([1,2,3,4])  #[] = ถ้ามี 1 =  1D
print('สร้างอาร์เรย์ 1 มิติ  = \n',Array1D) # คำสั่ง \n = ตัวที่อยู๋หลังคำสั่ง \n จะขึ้นบรรทัดใหม่

# 2D
Array2D = np.array([[1,2,3],[4,5,6]])  # [[]] = ถ้ามี 2 = 2D
print('สร้างอาร์เรย์ 2 มิติ = \n',Array2D) # คำสั่ง \n = ตัวที่อยู๋หลังคำสั่ง \n จะขึ้นบรรทัดใหม่

#3D = ก็เหมือนเอา อาร์เรย์ 2 มิติ มาประกบกัน ด้านหน้ากับ ด้านหลัง 
Array3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])  #[[[]]] = ถ้ามี 3 = 3D 
print('สร้างอาร์เรย์ 3 มิติ = \n',Array3D) # คำสั่ง \n = ตัวที่อยู๋หลังคำสั่ง \n จะขึ้นบรรทัดใหม่


# Shape = ใช้สำหรับแสดงรูปร่างของ อาร์เรย์ จะบอกเป็น แถว และ คอลัมน์
# 1D
Array1D = np.shape([1,2,3,4])  
# index[1][2]  (   index[1][2] =  แถว[1]  = คอลัมน์[2]   )
# 2D
Array2D = np.shape([[1,2,3],[4,5,6]])  
print('รูปร่างอาร์เรย์ 2 มิติ =',Array2D) 


# Size  = หาช่องของและจำนวนสมาชิก  แถว x คอลัมน์
# 1D  
Array1D = np.size([1,2,3,4]) 
print('จำนวนสมาชิกอาร์เรย์ 1 มิติ =',Array1D)
# 2D
Array2D = np.size([[1,2,3],[4,5,6]])  
print('จำนวนสมาชิกอาร์เรย์ 2 มิติ =',Array2D)


# .ndim = แสดงจำนวนมิติของ Array 
# บอกมิติของ Array  ( .ndim = คำสั่งบอกมิติของ Array )
Array1D = np.ndim([1,2,3,4]) 
print('Array1D = มิติที่ :',Array1D) 

Array2D = np.ndim([[1,2,3],[4,5,6]]) 
print('Array2D = มิติที่',Array2D)



# Array1D = np.arange(จำนวนข้อมูล)
# Arange = คือคำสั่งกำหนดช่วงเริ่มต้น
# np.arange (start(จุดเริ่มต้น),stop(หยุด),step(เพิ่มค่าหรือลดค่าที่ละกี่ครั้ง),dtype)
# reshape = ใช้กำหนดรูปร่างของ อาร์เรย์  .reshape(แถว,คอลัมน์)
Array1D = np.arange(12)
print('การเรียงอาร์เรย์ 1 มิติ = \n',Array1D)

# Array2D = np.arange(จำนวนข้อมูล).reshape(แถว,คอลัมน์)
Array2D = np.arange(12).reshape(3,4)
print('การเรียงอาร์เรย์ 2 มิติ = \n',Array2D)



# คำสั่ง dtype แสดง ชนิดข้อมูลและหน่วยของข้อมูล
Array1D = np.array([1,2,3,4],dtype='float')
print('ชนิดข้อมูลและหน่วยของข้อมูลของ Array1D = ',Array1D.dtype)
Array2D = np.array([[1,2,3],[4,5,6]],dtype='int') 
print('ชนิดข้อมูลและหน่วยของข้อมูลของ Array2D = ',Array2D.dtype)

# สร้างชนิดข้อมูลของ Array
Array1D = np.array([1,2,3,4,5,6,7,8,9],dtype='int')
print('Int','สร้างชนิดข้อมูลของ Array\n',Array1D)
Array2D = np.array([[1,2,3],[4,5,6]],dtype='float')
print('float','สร้างชนิดข้อมูลของ Array2D\n',Array2D)



