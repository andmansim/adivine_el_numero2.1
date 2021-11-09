def game_level():
    nivel_sencillo = 0
    nivel_medio = 1
    nivel_avanzado = 2
    nivel_experto = 3
    levels = ["Game levels:" + "nivel_sencillo: " + str(nivel_sencillo), "nivel_medio: " + str(nivel_medio), "nivel_avanzado: " + str(nivel_avanzado), "nivel_experto: " + str(nivel_experto)]
    print(levels)
    user = int(input("Choose one level for the game: "))
    return user


