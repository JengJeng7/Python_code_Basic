# หาเลขคู่ กับ เลขคี่

Number = int(input('ป้อนตัวเลข:'))

# ถ้าหารสองลงตัว = คุ่
while Number != 0:
    Number = int(input('ป้อนตัวเลข:'))
    if Number % 2 ==0:
        print(Number,'เป็นเลขคู่')
    elif Number != 0:
        print(Number,'เป็นเลขคี่')
