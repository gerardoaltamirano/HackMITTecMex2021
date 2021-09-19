#!/usr/bin/env python
# coding: utf-8

# ## Hangman Code
# 

# In[ ]:


import random
Hangman= ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

print("Welcome to Hangman Orthography Trainer!")

print("In this game a random word will be selected from our library and you will have to guess it letter by letter.")

print("But be careful because if the drawing fills up, you lose!")

print("Good luck!")

words = 'teacher programmer rating food game rocket impossible variable flying head player gaze writer ticket pen cell phone value free magazine disk volleyball star ring'.split()
 
def buscarPalabraAleat(listaPalabras):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]
 
def displayBoard(Hangman, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(Hangman[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Reemplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")
 
def elijeLetra(algunaLetra):
    # Devuelve la letra que el jugador ingresó. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Guess a letter:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce just one letter') 
        elif letra in algunaLetra:
            print ('You have already selected this word, what if you try another one?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Insert a letter.')
        else:
            return letra
 
def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('Do you want to play again? (Yes or No)')
    return input().lower().startswith('y')
 
print ('Hangman')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(Hangman, letraIncorrecta, letraCorrecta, palabraSecreta)
    # El usuario elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('Great! The secret word is "' + palabraSecreta + '"! ¡You won!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(Hangman) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('You have run out of letters!\nDespues de ' + str(len(letraIncorrecta)) + ' wrong letters y ' + str(len(letraCorrecta)) + ' wrong letters, the word was "' + palabraSecreta + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            break

