# โปรแกรมแลกธนบัตร
# แลกเงินและหาจำนวนของแบงค์

# 2000 => 1000 => สองใบ
# 1500 => 1000 => หนึ่งใบ, 500 => หนึ่งใบ

Number = int(input('ป้อนจำนวนเงินของคุณ :'))

if Number >= 1000:
    print('1000 บาท',Number//1000,'ใบ')
    Number = Number % 1000 # 1500 % 1000 หารเอาเศษ = 500
if Number >=500:
    print('500บาท',Number//500,'ใบ') # % = หารเอาเศษ
    Number = Number % 500
if Number >= 100:
    print('100 บาท',Number//100,'ใบ')
    Number = Number % 100
if Number >= 50:
    print('50 บาท',Number//50,'ใบ')
    Number = Number % 50
if Number >= 20:
    print('20 บาท',Number//20,'ใบ')
    Number = Number % 20
