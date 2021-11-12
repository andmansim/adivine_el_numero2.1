# iniciation of the matrix and the titles
result = [] 
a = [0]*2
result.append(a)
result[0][0]= "Player name"
result[0][1]= "Games won"
from tabulate import tabulate 


# player options
def game_level():
    easy_level = 0
    normal_level = 1
    advance_level = 2
    expert_level = 3
    level_IA = 4
    levels = ["Game levels:" + "nivel_sencillo: " + str(easy_level), "nivel_medio: " + str(normal_level), "nivel_avanzado: " + str(advance_level), "nivel_experto: " + str(expert_level), "maestro IA: " + str(level_IA)]
    print(levels)
    user = int(input("Choose one level for the game: "))
    return user

# start to play depending on the level
def ask_number(value_min, value_max, attempts):
    import random
    number = random.randint(value_min, value_max)
    print(number)
    print("Choose an integrer between:" + str(value_min) + " and " + str(value_max))
    user_value = int(input())
    rest_attempts = attempts - 1
    while user_value != number and rest_attempts > 0:
        if user_value > value_max:
            print("Choose another number between " + str(value_min) + " and " + str(value_max))
        else:
            if user_value > number:
                print("Too far from the number, it's smaller. The number is between:" + str(value_min) + " and " + str(user_value))
            else:
                print("Too far from the number, it's bigger. The number is between:" + str(user_value) + " and " + str(value_max))
        rest_attempts = rest_attempts - 1
        user_value = int(input())
    if user_value == number:
        print("¡Congratulations!, you have completed the level")
        print(("Put your name: "))
        name = str(input())
        #  looking for the name user in the matrix
        index=-1 
        
        for m in range (len(result)):
            if result[m][0]== name:
                index=m
                        
        if index == -1:
            a = [0]*2
            result.append(a)
            element=len(result)
            result[element-1][0]=name
            result[element-1][1]=1

                    
        else:
            result[index][0]=name
            result[index][1]=result[index][1]+1 
              
    # attempts finished the game stops
    if rest_attempts == 0 and user_value != number:
        print("Game over")
# conditions of the differents levels
def play():
    user_choice = game_level()
    if user_choice ==4:
        play_IA()
    else:
        continue_playing = True 
        while continue_playing == True:
        
            if user_choice == 0:
                ask_number(0,100,5)
            elif user_choice == 1:
                ask_number(0,1000,20)
            elif user_choice == 2:
                ask_number(0,1000000,50)
            elif user_choice == 3:
                ask_number(0,1000000000000,100)
       
            print("Do you want to continue playing? Yes/No")
            new_intent = str(input())
        
            if new_intent != str('Yes'):
                continue_playing = False
   # level of the ia    
def play_IA():
    import random
    low_value =0
    high_value = 100
    number = random.randint(0, 100)
    print("Computer number: " + str(number))
    user_value = int(random.randint(0, 100))
    print("IA number: " + str(user_value))
    while user_value != number:
        if user_value > number:
            high_value = user_value
            print("Too far from the number, it's smaller. The number is between:" + str(low_value) + " and " + str(high_value))
            
            user_value = random.randint(low_value, high_value)
            print("IA number: " + str(user_value))
        elif user_value < number:
            low_value = user_value
            print("Too far from the number, it's bigger. The number is between:" + str(low_value) + " and " + str(high_value))
            
            user_value = random.randint(low_value, high_value)
            print("IA number: " + str(user_value))
    if user_value == number:
        print("¡Congratulations!, you have completed the level")             
      
play()
print(tabulate(result))