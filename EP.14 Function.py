

# นี้คือฟังก์ชั่นที่เช็คว่า Number ที่ป้อนเข้ามาเลขคู่ หรือ เลขคี่
def Even_Odd(Number):
   # Number = int(input("ป้อนตัวเลข:"))
    if Number % 2 == 0:
        print(Number,"= Even")
    else:
        print(Number,"= Odd")
print("ฟังชั่นนี้คือฟังก์ชั่นที่เช็คว่า Number ที่ป้อนเข้ามาเลขคู่ หรือ เลขคี่")
Even_Odd(52) # => 52 = Number

# ฟังก์ชั่นเช็คดอกเบี้ยต่อเดือนของ Number 
def interest_per_month(Number):
    if Number >= 1000000:
        Sum = Number * 5 / 100
        print("ดอกเบี้ย 5% ของ",Number,"ต่อเดือน =>",Sum)
    elif Number >= 50000 and Number < 1000000:
        Sum = Number*3/100
        print("ดอกเบี้ย 3% ของ",Number,"ต่อเดือน =>",Sum)
    elif Number >= 10000 and Number < 50000:
        Sum = Number*1/100
        print("ดอกเบี้ย 1% ของ",Number,"ต่อเดือน =>",Sum)
    else: 
        Sum = Number*0.5/100
        print("ดอกเบี้ย 0.5% ของ",Number,"ต่อเดือน =>",Sum)
    x = 50 + 50
print("\nฟังชั่น เช็คดอกเบี้ยต่อเดือนของ Number")
interest_per_month(10000)

# ฟังชั่น ยอดรวมสินค้า
def get_product_information(unit,price,member):
    #unit = int(input("จำนวนสินค้า:"))
    #price = float(input("ราคาต่อหน่วย:"))
    #member = input("ํY หรือ N:")
    total = unit * price
    discount = 0
    amount = 0
    if member == "y":
        if total <= 500:
            discount = total * 10 / 100
        elif total > 500 and total < 1000:
            discount = total * 15 / 100
        else:
            discount = total * 20 / 100
        
    elif member == "n":
        if total <= 500:
            discount = total * 5 / 100
        elif total > 500 and total < 1000:
            discount = total * 10 / 100
        else:
            discount = total * 15 / 100
    amount = total - discount
    print("Total %.2f"% total)
    print("Discount %.2f"% discount)
    print("Amount %.2f"%amount)
unit = 5
price = 500.00
string = "n"
string1 = "y"
print("\nฟังชั่น ยอดรวมสินค้า")
get_product_information(unit,price,string1)

# ฟังชั่น เปรียบเทียบวันเกิด ว่าใครเกิดก่อนกัน
def Compare_day_month_year(year,month,day,year2,month2,day2):
    #day,month,year = [int(i) for i in input("ป้อน วัน เดือน ปี ของคุณ:").split()]
    #day2,month2,year2 = [int(i) for i in input("ป้อน วัน เดือน ปี ของคุณ:").split()]
    if year <= year2 or month > month2 or day > day2:
        print("คนแรกอายุมากกว่าคนที่สอง")    
    else:
        print("คนที่สองอายุมากกว่าคนแรก")
print("\nฟังชั่น เปรียบเทียบวันเกิด ว่าใครเกิดก่อนกัน")
Compare_day_month_year(2545,10,10,2546,10,10)



