import random # random = การสุ่มคำ หรือ สุ่มค่าต่างๆ
from tkinter import * # import ทุกอย่างใน tkinter มาใช้
'''
Tkinter เป็นโมดูลที่พัฒนามาจาก Tk GUI Toolkit 
ซึ่งทางานอยู่บนระบบปฏิบัติการยูนิกซ์มาก่อน 
ไพธอนได้เลือกโมดูลนี้ในการพัฒนากราฟิกบนไพธอนเป็นหลัก
'''
import time # import คำสั่งที่เกี่ยวกับเวลา
# ในที่นี้คือ window = จอนะครับ
# สร้าง app window
window = Tk() 
# ตั้งชื่อเกมส์
window.title('Name Guessing Game')
# ความกว้างของหน้าจอเกม หรือขนาดของหน้าจอเกม
window.geometry('700x780')
# สถานะเกม
game_finished = False # เริ่มต้นเกมยังไม่จบ
Score = 0
lives = 3

# แสดง score และ lives บน window
status_str = StringVar() # StringVar() มาจาก tkinter
status_str.set("Score: "+str(Score)+'|'+"Lives: " + "❤️"*lives)
show_status = Label(window, textvariable = status_str)
show_status.pack(pady = 20)

# สร้าง (words = คำ) (category = ประเภท) (hints = คำใบ้)
# {} = Dict 
word_dict = {
    "banana":
        {"category": "ผลไม้",
        "hint": ["1.มีดอกเป็นช่อ ห้อยลงมาเป็นเคลือ จะมีปลีออกที่ปลายยอด","2.มีลักษณะกลมทรงรี ","3.ผลสุกแก่เปลือกจะมีสีเหลือง ข้างในจะมีเนื้อสีขาวเหลือง",'4.ขึ้นต้นด้วยตัว B']
        },
    'watermelon':
        {'category': 'ผลไม้',
        'hint': ['1.ลักษณะทรงกลม หรือทรงกระบอก มีเปลือกแข็ง มีสีเขียวหรือสีเหลือง','2.ภายในจะมีหลายเมล็ดในผล','3.มีเนื้อสีแดงหรือสีเหลือง','4.ขึ้นต้นด้วย W']
        },
    'apple':
        {'category': 'ผลไม้',
        'hint': ['1.ลักษณะทรงกลม มีร่องบุ๋มที่ขั้ว และก้นผล หรือกลมแบนเล็กน้อย','2.เนื้อมีสีเหลืองนวล เป็นทรายละเอียด เนื้อกรอบ ให้รสหวานอมเปรี้ยว','3.ตรงกลางผลเป็นที่อยู่ของเมล็ด มีลักษณะเป็นโพรงอากาศ''4.ขึ้นต้นด้วย A',]
        },
    'orenge':
        {'category': 'ผลไม้',
        'hint': ['1.ลักษณะกลมแป้น ผิวเปลือกนอกเรียบ ผลอ่อนมีสีเขียว เมื่อผลสุกจะเปลี่ยนเป็นสีเหลือง ','2. ข้างในจะมีเนื้อเป็นถุงน้ำเล็กๆ มีสีเหลือง อยู่เบียดกันแน่น ','3.มีรสชาติเปรี้ยวหรือหวาน','4.ขึ้นต้นด้วย O']
        },
    'strawberry':
        {'category': 'ผลไม้',
        'hint': ['1.เป็นผลเดี่ยว มีก้านผลยาวแทงออกจากลำต้นมีลักษณะทรงกลมรี คล้ายรูปหัวใจ','2.มีเสี้ยนเล็กๆบางๆอยู่ทั่วผล ผลอ่อนสีขาว ','3.ผลสุกจะมีสีแดง หรือสีแดงอมส้ม มีเนื้อสีแดง เนื้อนุ่มฉ่ำน้ำ มีรสชาติเปรี้ยวหรือหวาน','4.ขึ้นต้นด้วย S']
        },
}

# สร้าง การดึง key ของ words
words = list(word_dict.keys())

# สร้างฟังก์ชั่นสุ่มคำและสร้าง clue ['?','?','?']
def get_new_secret_word():
    random.shuffle(words) # สลับคำ
    secret_word = words.pop() 
    clue = list("?"*len(secret_word))
    return secret_word, clue
secret_word , clue = get_new_secret_word()

# แสดง category และ clue บน window(หน้าจอ)
category_str = StringVar() # StringVar() มาจาก tkinter
category_str.set(word_dict[secret_word]['category'])
show_category = Label(window, textvariable = category_str, font = ('Angsana New',30))
show_category.pack(pady = 5)

clue_str = StringVar() # StringVar() มาจาก tkinter
clue_str.set(' | '.join(clue))
show_clue = Label(window, textvariable = clue_str, font = ('Angsana New',40))
show_clue.pack(padx = 10, pady = 30)

# แสดง hints
hints = word_dict[secret_word]['hint']
hint_text = StringVar()
hint_text.set('Hints')
hint_str = StringVar()
hint_str.set('\n'.join(hints)) # \n = เหมือนการเว้นวรรค

show_hint_text = Label(window, textvariable = hint_text, font = ('Angsana New',28))
show_hint_text.pack()
show_hints = Label(window, textvariable = hint_str, font = ('Angsana New',18))
show_hints.pack(pady = 10)

# กล่องให้กรอก Guess \ Entry = กล่องที่ให้เราพิมพ์ตัวอักษรได้ \ width = ความยาวของกล่อง \ borderwidth = ความหนาของขอบ
textentry = Entry(window, width = 10, borderwidth = 2,font = ('Angsana New', 20), justify = 'center')
textentry.pack()

# ปุ่มกด Submit พร้อมฟังก์ชั่นที่อัพเดต clue และสถานะของเกม

def update_clue(Guess, secret_word, clue):
    #Guess ไล่ไปที่ละตัวอักษรใน secret_word ว่ามีตรงไหนบ้างที่ทาย
    for i in range(len(secret_word)):
        #ถ้าทายตรงตัวไหนให้ update clue ตรงตำแหน่งนั้น
        if Guess == secret_word[i]:
            clue[i] = Guess
    clue_str.set(' | '.join(clue))
    # ทายเสร็จแล้วหรือไม่
    win = ''.join(clue) == secret_word
    return win #ทายจนไม่เหลือ "?" แล้ว -> True, ถ้ายังเหลือ -> False


def update_screen():
    # ประกาศด้านแปลพวกนี้ให้เป็น global เพื่อให้ฟังก์ชั่นนี้เข้าถึงตัวแปลนอก command ได้
    global game_finished, Score, lives, secret_word, clue, hints

    Guess = textentry.get().strip() # Strip = แถบลบช่องว่าง
    Guess = Guess.upper() # lower() = ตัวพิมพ์เล็ก

    if Guess in secret_word:
        win = update_clue(Guess, secret_word, clue)
        if win:
            print("ยินดีด้วยคุณทายคำ:",secret_word,"ถูก")
            Score = Score + 1
            print("Score :",Score)
            clue_str.set('Yay! Answer: '+ secret_word)
            window.update()
            time.sleep(2)  # ทำให้โปรแกรมค้างไว้ 2 วินาที

            if len(words) == 0:
                game_finished = True
                clue_str.set('Congrats!')
            else:
                secret_word, clue = get_new_secret_word()
                category_str.set(word_dict[secret_word]['category'])
                clue_str.set(' | '.join(clue))
                hints = word_dict[secret_word]['hint']
                hint_str.set('\n'.join(hints))
    else: # ที่ Guees มา ไม่อยู่ใน secret_word
            print('ผิด! เลือดลด')
            lives = lives - 1
            if lives == 0:
                clue_str.set('Game Over!')
                game_finished = True
    status_str.set("Score: "+str(Score)+'|'+"Lives: " + "❤️"*lives)
    textentry.delete(0,'end')

submit_btn = Button(window, text = 'Submit', command = update_screen)
submit_btn.pack()

# โปรแกรมหลักที่ เช็ค ว่าเกมจบแล้วหรือยัง
def main():
    if not game_finished:
        # print('Test Refresh')
        window.after(1000, main)
    else:
        submit_btn['state'] = 'disable'
        print('Quitting...')
        window.quit()
window.after(1000, main)
window.mainloop()
'''
words = ["banana",'watermelon','apple','orenge','strawberry']
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
'''