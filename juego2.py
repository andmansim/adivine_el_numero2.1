
i = 1
j = 2
result = []
for n in range(i):
    a = [0]*j
    result.append(a)
  
result2=list()

def game_level():
    nivel_sencillo = 0
    nivel_medio = 1
    nivel_avanzado = 2
    nivel_experto = 3
    levels = ["Game levels:" + "nivel_sencillo: " + str(nivel_sencillo), "nivel_medio: " + str(nivel_medio), "nivel_avanzado: " + str(nivel_avanzado), "nivel_experto: " + str(nivel_experto)]
    print(levels)
    user = int(input("Choose one level for the game: "))
    return user

def pedir_numero(value_min, value_max, attempts):
    import random
    number = random.randint(value_min, value_max)
    print(number)
    print("Choose an integrer between:" + str(value_min) + " and " + str(value_max))
    valor_usuario = int(input())
    rest_attempts = attempts - 1
    while valor_usuario != number and rest_attempts > 0:
        if valor_usuario > value_max:
            print("Choose another number between " + str(value_min) + " and " + str(value_max))
        else:
            if valor_usuario > number:
                print("Too far from the number, it's smaller. The number is between:" + str(value_min) + " and " + str(valor_usuario))
            else:
                print("Too far from the number, it's smaller. The number is between:" + str(valor_usuario) + " and " + str(value_max))
        rest_attempts = rest_attempts - 1
        valor_usuario = int(input())
    if valor_usuario == number:
        print("¡Congratulations!, you have completed the level")
        print(("Put your name: "))
        name = str(input())
        #b = [name] * [0]
        #result.append(b)
       
        index=-1 
        for m in range (len(result)):
            if result[m][0]== name:
                index=m
                        
        print(index)
        if index == -1:
            a = [0]*2
            
            result.append(a)
            
            element=len(result)
            result[element-1][0]=name
            result[element-1][1]=1
            
        else:
            result[index][0]=name
            result[index][1]=result[index][1]+1
              
    
    if rest_attempts == 0 and valor_usuario != number:
        print("Game over")

def jugar():
    user_choice = game_level()
    continue_playing = True 
    while continue_playing == True:
        
        if user_choice == 0:
            pedir_numero(0,100,5)
        elif user_choice == 1:
            pedir_numero(0,1000,20)
        elif user_choice == 2:
            pedir_numero(0,1000000,50)
        elif user_choice == 3:
            pedir_numero(0,1000000000000,100)
        print("Do you want to continue playing? Yes/No")
        new_intent = str(input())
        
        if new_intent != str('Yes'):
            continue_playing = False
                
jugar()
print(result)
                
    

