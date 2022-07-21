import random
# random = การสุ่มคำ หรือ สุ่มค่าต่างๆ
Score = 0
lives = 3
words = ["Dog",'Cat','chicken','elephant','shark','zebra','snake']
def update_clue(Guess, secret_word, clue):
    #Guess ไล่ไปที่ละตัวอักษรใน secret_word ว่ามีตรงไหนบ้างที่ทาย
    for i in range(len(secret_word)):
        #ถ้าทายตรงตัวไหนให้ update clue ตรงตำแหน่งนั้น
        if Guess == secret_word[i]:
            clue[i] = Guess
    # ทายเสร็จแล้วหรือไม่
    win = ''.join(clue) == secret_word
    return win #ทายจนไม่เหลือ "?" แล้ว -> True, ถ้ายังเหลือ -> False

# ตราบใดที่ยังมีคำให้ทายอยู่ และ ชีวิตยังเหลือ -> เล่นต่อไป
while (len((words)) > 0 and ((lives) > 0)):
    # สุ่มคำจาก words แล้วดึงคำนั้นออกจาก list
    random.shuffle(words) # สลับคำ
    secret_word = words.pop() 
    clue = list("?"*len(secret_word)) #จำนวนเท่ากับตัวอักษร secret_word

    # ตราบใดที่ยังทายคำนี้ไม่เสร็จ หรือ ชีวิตยังไม่หมด
    while True:
        print(clue)
        print("ชีวิตที่เหลือ :",(lives))
        Guess = input("ทายตัวอักษร :")

        # เช็คว่าตัวอักษรที่ทายอยู่ใน clue หรือ secret_word หรือไม่
        if Guess in secret_word:
            win = update_clue(Guess, secret_word, clue)
            if win:
                print("ยินดีด้วยคุณทายคำ:",secret_word,"ถูก")
                Score = Score + 1
                print("Score :",Score)
                break  # break = คำสั่งหยุดการทำงานนะตรงนี้ 
        else: # ที่ Guees มา ไม่อยู่ใน secret_word
            print('ผิด! เลือดลด')
            lives = lives - 1
            if lives == 0:
                print("คุณแพ้แล้ว! คำนั้นคือ:",secret_word)
                break # ชีวิตหมด
print('Final Score: ',Score)
print('End game')
