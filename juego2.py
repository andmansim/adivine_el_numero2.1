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
                
    

