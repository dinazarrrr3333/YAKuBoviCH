point = [0,0,0]
player = ["Алёша Попович","Добрыня Никитич","Илья Муромец"]
count = 0
secret= input("""ведите слово """)
print("\033[2J")
win = False
all_letters= []
true_letters = []
while win == False: 
    letter = input(f"""\n отгадайте слово,{player[count]}
список: {all_letters}
твой ответ: """)
    print(f"{point[count]} очк ")
    if letter in all_letters:
        print("этот символ вы уже писали")
        continue
    elif letter in secret:
        print("ты угадал букву!!!!!!!")
        point[count] += 10
        true_letters.append(letter)
    else:
        print("куропатка")    
    all_letters.append(letter)
    count += 1
    win = True
    for symbol in secret:
        if symbol in true_letters:
            print(symbol,end="")
        else:
            print("*", end="")
            win = False
    if count == 3:
        count = 0
for index in range(3):
    print(f"\n игрок {player[index]} набрал {point[index]} очков" )

