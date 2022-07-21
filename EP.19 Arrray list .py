# นำเข้าฟังก์ชั่น numpy
import numpy as np

 # Python จะเริ่มนับตั้งแต่  0   1  2  3  4  5  6  7  8  9   = 10
            #       -10 -9 -8 -7 -6 -5 -4 -3 -2 -1   = 10
# การสร้าง List
x = ['Teerapong','Charoenram',18]

# การสร้าง Array
arr = np.array(x)
print(arr)
# บอกมิติของ Array   ( .ndim = คำสั่งบอกมิติของ Array )
print('Array มิติที่ :',arr.ndim)   
# index = ฟังก์ชั่นที่เรียกข้อมูลใน Array, List ออกมาใช้งาน
print('x[0]:',x[0])

# หรือ

# 1D
Array1D = np.array([1,2,3,4]) #[] = ถ้ามี 1 =  1D
print(Array1D)
# บอกมิติของ Array  ( .ndim = คำสั่งบอกมิติของ Array )
print('Array มิติที่ :',Array1D.ndim) 
# index = ฟังก์ชั่นที่เรียกข้อมูลใน Array, List ออกมาใช้งาน
print('Array1D[1]:',Array1D[1])


# 2D
Array2D = np.array([[1,2,3],[4,5,6]]) # [[]] = ถ้ามี 2 = 2D
print(Array2D)
# บอกมิติของ Array  ( .ndim = คำสั่งบอกมิติของ Array )
print('Array มิติที่ :',Array2D.ndim)
# index = ฟังก์ชั่นที่เรียกข้อมูลใน Array, List ออกมาใช้งาน
print('Array2D[1][2]:',Array2D[1][2]) #index[1][2]  (index[1] = แถว[1] [2] = คอลัมน์[2])

# 3D
Array3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #[[[]]] = ถ้ามี 3 = 3D
print(Array3D)
# บอกมิติของ Array  ( .ndim = คำสั่งบอกมิติของ Array )
print('Array3D มิติที่ :',Array3D.ndim) 
print('Array3D[1][1][2]:',Array3D[1][1][2]) #index[0][1][2],(index[0] = ชั้น[0], [1] = แถว[1], [2] = คอลัมน์[2])



# ชนิดข้อมูลหลักๆ ที่ใช้ใน Numpy
'''
1. Integer = จำนวนเต็ม
2. Float = ทศนิยม
3. String = ข้อความ, ตัวอักษร
4. Boolean = True , Flase
5. Complex = เชิงซ้อน
6. Object =  วัตถุ
'''
# คำสั่งแสดง ชนิดข้อมูลและหน่วยของข้อมูล
Array1D = np.array([1,2,3,4])
print('ชนิดข้อมูลและหน่วยของข้อมูลของ Array1D = ',Array1D.dtype)
# สร้างชนิดข้อมูลของ Array
X = np.array([1,2,3,4,5,6,7,8,9],dtype='int')
print(X)
X = np.array([1,2,3,4,5,6,7,8,9],dtype='complex')
print(X)

