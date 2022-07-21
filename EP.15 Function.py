# Function = กระบวนการที่เปลี่ยน input ให้เป็น output ที่ต้องการ
# การนิยาม Function ด้วย define ย่อมาเป็น def
# return = คืนค่า 
#      def Game (HHHH):
 #   (ฟังก์ชั่น) (ชื่อ) (อันนี้เหมือนเราใส่ฟังก์ชั่น input เข้าไป เพื่อรับค่าผ่านทางคีย์บอร์ด ใส่อะไรเข้าไปก็ได้)



#การสร้าง Function แบบไม่ใช่อะไรในวงเล็บ
def game ():
    print("ยกตัวอย่างการสร้างฟังก์ชั่น")
#เรียกใช้ Function ออกทางจอภาพ
game()

#การสร้าง Function แบบใส่ input เข้าไป
def Game (HHHH):
    print("Hello World",HHHH)
#เรียกใช้ Function ออกทางจอภาพ
Game("Teerapong")

#การสร้าง Function แบบใส่ return เข้าไป
def Multiplication (x,y):
    return x*y
#เรียกใช้ Function ออกทางจอภาพ
X = Multiplication (5,5)
print("x*y = ",X) # หรือ print(Multiplication (5,5))

