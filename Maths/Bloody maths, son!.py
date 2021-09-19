upper = 0
lower = 0
digit = 0
num = 0
space = 0
spaceU = 0
res = "si"
res2 = "si"
nombre = {}
#Function that prompts the user for his or her name
def nombre_u():
    
    global nombre
    
    name = input("\nIntroduce your name: ")
    nombre = name
    print("\nFuck, what a great name")
    
    usuario()
    
#Function that requests a user and validates that it has no spaces.
def usuario():
    #function to repeat the cycle if the user is invalid
    def repite():
        global res2
        while res2 == "yes":
            autentica()
            imprime()
        
        contraseña()
#Function that request the user    
    def pide_usuario():
        
        usu = input("Introduce an user: ")
        
        return usu
#function que autentica que no tenga espacios
    def autentica():
        
        global spaceU
        
        user = pide_usuario ()
        
        luser = len(user)
        
        for pos  in range (0,luser):
            if user[pos].isspace() == True:
                spaceU += 1
#function that warns if it has spaces
    def imprime():
        
        global spaceU
        global res2

        if spaceU == 0:
            print ("Valid User")
            res2 = "no"
        else:
                print("There are spaces")
            print("Invalid user")
            spaceU -= spaceU
                    
    repite()
#function requesting and authenticating the password
def contraseña():
#function to repeat the cycle if the password is invalid    
    def repite():
        global res
        while res == "yes":
            autentica()
            imprime()
        
        respuesta_n()
#Function asking for password        
    def pide_contraseña():
        
        print('''
Remember that your password must contain at least
                                - a capital letter
                                - a lower case letter
                                - a number
                                - a symbol
                                - minimum 8 digits
                                ''')
        
        cont = input("Introduce a password: ")
        
        return cont
#function that authenticates the password
    def autentica():
        
        global upper
        global lower
        global digit
        global num
        global space
        
        psw = pide_contraseña ()
        
        lpsw = len(psw)
        
        if lpsw >=8:
            for pos  in range (0,lpsw):
                if psw[pos].isupper() == True:
                    upper += 1
                elif psw[pos].islower() == True:
                    lower += 1
                elif psw[pos].isalnum() == True:
                    num += 1
                elif psw[pos].isspace() == True:
                    space += 1
                else:
                    digit += 1
        else:
            print("There's no enough characters")
#function that warns if the password is wrong
    def imprime():
        global upper
        global lower
        global digit
        global num
        global space
        global res
        
        if upper >= 1:
            if lower >= 1:
                if digit >=1:
                    if num >=1:
                        if space == 0:
                            print ("Valid Password")
                            res = "no"
                        else:
                            print("There's spaces")
                            print("Invalid password")
                    else:
                        print("There's no numbers")
                        print ("Invalid password")
                else:
                    print("There's no symbols")
                    print ("Invalid password")
            else:
                print("There's no lower case")
                print ("Invalid password")
        else:
            print("There's no upper case")
            print ("Invalid password")
    repite()
#welcoming function
def bienvenida_total():
    
    print('''
!Bloody Math, Son!
''')
    
    print('''
Welcome to bloody maths, son, a game in which you will not only learn about math.
We hope you have fun! But first...''')
    
    nombre_u()
#function to stop or end the program
def respuesta_n():
    
    respuesta = "yes"
    while respuesta == "yes":
        menu()
        respuesta = input("Wanna play again?: ")
    print("See you soon!")
    input("Press ENTER to exit")
    respuesta = "no"
#function prompting the user for the menu option
def menu():
    print('''
Now, to decide...

1) Review division with decimal point.
2) Review division of fractions
3) Go straight to levels
''')
    
    opc = int(input("What option would you like to choose?: "))
    
    if opc == 1 or opc == 2 or opc == 3:
        desvio(opc)
    
    else:
        print("Invalid number")
        respuesta_n()
#Option that sends the user's answer to the menu        
def desvio(opcion):
    
    if opcion == 1:
        divisiones_con_decimales()
    elif opcion == 2:
        divisiones_con_fracciones2()
    else:
        nivel1()
#Function that activates the explanation of divisions with a decimal point.
def divisiones_con_decimales():
    #Function welcoming explanation
    def hola():
        hello = open("hola.txt","r",encoding="utf8")
        holi = hello.read()
        print(holi)
        
        cual()
    #function asking the user for the case he/she wants to see
    def cual():
        opcion = input("\nWhich case do you wanna see?: ")
        print("")
        casos(opcion)
    
    #Function to continue viewing cases
    def seguir():
        
        ans = input("Do you wish to continue checking cases?: ")
        if ans.lower() == "Yes" or ans == "yes":
            cual()
            
        else:
            print("Returning to main menu")
            menu()
        
    #Function that filters the option chosen by the user.    
    def casos(caso):
        if caso >= "1" and caso <= "5":
            if caso == "1":
                uno()
                        
            elif caso == "2":
                dos()
                            
            elif caso == "3":
                tres()
                            
            elif caso == "4":
                cuatro()
                            
            else:
                todo()
                        
        else:
            print("Invalid option, try again")
            cual()
    
    #Function explaining all cases
    def todo():
        expli = open("todos.txt","r",encoding="utf8")
        todoo = expli.read()
        print(todoo)
        seguir()
    
    #Function explaining the first case
    def uno():
        caso1 = open("uno.txt","r",encoding="utf8")
        unoo = caso1.read()
        print(unoo)
        seguir()
    
    #Function explaining the second case
    def dos():
        caso2 = open("dos.txt","r",encoding="utf8")
        doss = caso2.read()
        print(doss)
        seguir()
    
    #Function explaining the third case
    def tres():
        caso3 = open("tres.txt","r",encoding="utf8")
        tress = caso3.read()
        print(tress)
        seguir()
    
    #Function explaining the fourth case
    def cuatro():
        caso4 = open("cuatro.txt","r",encoding="utf8")
        cuatroo = caso4.read()
        print(cuatroo)
        seguir()
    
    hola()
#Function for the explanation of division of fractions
def divisiones_con_fracciones2():
    #function that welcomes, asks for the case to choose and filters it
    def divisiones_con_fracciones():
        
        welcome = open("bienvenida.txt", "r", encoding = "UTF8")
        bienvenida = welcome.read()
        print(bienvenida)
        
        options = open("opciones.txt", "r", encoding = "UTF8")
        opciones = options.read()
        print(opciones)
        
        opcion = int(input("\nWhich option do you wish to check? "))
        print("")
        
        if opcion == 1:
            multiplicacion_en_cruz()
            print(" ")
            continuar_o_niveles()
                
        elif opcion == 2:
            invertir_y_multiplicar()
            print(" ")
            continuar_o_niveles()
            
        elif opcion == 3:
            ambos_metodos()
            print("")
            continuar_o_niveles()
            
        else:
            print("That is not an option")
            print(" ")
            
    #show explanation for case1
    def multiplicacion_en_cruz():
        
        first = open("multiplicacionEnCruz.txt", "r", encoding = "UTF8")
        primera = first.read()
        print(primera)
        
    #show explanation for case2
    def invertir_y_multiplicar():
        
        second = open("invertirYMultiplicar.txt", "r", encoding = "UTF8")
        segunda = second.read()
        print(segunda)
        
    #show explanation for both cases
    def ambos_metodos():
        
        multiplicacion_en_cruz()
        invertir_y_multiplicar()

    #function to continue choosing cases or go to game levels
    def continuar_o_niveles():
        
        c = open("continuar.txt", "r", encoding = "UTF8")
        conti = c.read()
        print(conti)
        
        continuar = int(input("\nWhich option do you wanna choose?:  "))
        
        if continuar == 1:
            menu()
        
        elif continuar == 2:
            print("")
            divisiones_con_fracciones()
        
        elif continuar == 3:
            nivel1()
            
        else:
            print("That's not an option")
            print(" ")
    
    divisiones_con_fracciones()

#Level 1 of the game
def nivel1():
    
    #indications of the game
    def indicaciones():
    
        indications = open("indicaciones.txt", "r", encoding = "UTF8")
        indicaciones = indications.read()
        print(indicaciones)
        ejercicio1()
    
    #LEVEL 1
    def ejercicio1():
    
        print("\nNivel 1: \n(1/6)/(5/9)")
        respuesta1 = input("\nWhat is the result?: ")
            
        if respuesta1 == "9/30" or respuesta1 == "3/10":
            print("¡Correct!")
            nivel2()
        else:
            print("Incorrect answer")
            print("")
            ejercicio1()
    
    indicaciones()

#lEVEL 2
def nivel2():
    print("\nNivel 2: \n2.35/5")
    respuesta1 = float(input("\nWhat is the result?: "))
        
    if respuesta1 == .47:
        print("¡Correct!")
        nivel3()
        
    else:
        print("Incorrect answer")
        print("")
        nivel1()

#lEVEL 3
def nivel3():
    print("\n¡Nivel3!, You are halfway there\n(347/38)/(255/32): ")
    resp = input("What is the simplified resultant fraction?: ")
    
    if resp == "5552/4845":
        print("HERO")
        nivel4()
    
    else:
        print("Nooooo, comeee baaaackkk")
        nivel2()
    
#LEVEL 4
def nivel4():
    print("\nYA NIVEL 4 WUUUU\n345.654/32.987")
    resp = float(input("What is the result of the division? Round to 3 decimal places: "))
                        
    if resp == 10.478 or resp == 10.479:
        print("HERO")
        nivel5()
        
    else:
        print("Noooooo, comeee baaackk")
        nivel3()
    
#LEVEL 5
def nivel5():
    #Displays the level problem
    def cinco():
        print("\nNIVEL 5")
        notanfeo = open("decimalnotanfeo.txt","r",encoding="utf8")
        notanfeoo = notanfeo.read()
        print(notanfeoo)
        
        cincoans()
    
    #asks for level response and filters it
    def cincoans():
        respues = float(input("Introduce your answer: "))
        
        #correct answer: 344.38
        if respues == 344.38:
            print("\n¡Correct, You go to next level :)\n")
            nivel6()
            
            #Send this level to Call
            
        else:
            print("\nInvalid answer.\nyou return to the previous level.\n")
            
            #And here it returns to the previous level
            nivel4()
    
    cinco()

#LEVEL 6
def nivel6():
    
    #Displays the level problem
    def seis():
        print("\nNIVEL 6")
        feo = open("decimalfeo.txt","r",encoding="utf8")
        feoo = feo.read()
        print(feoo)
        
        seisans()
    
    #ask and filter the answer 
    def seisans():
        respuest = float(input("Introduce your answer: "))
        
        #correct answer: 49.81
        if respuest == 49.81:
            print("\n¡Correct! You have completed Bloody maths, son! :)\n")
            
            #CERTIFICATE
            certificado()
            
        else:
            print("\nWrong answer. You return to the previous leveL.\n")
            #And here it returns it to the previous level
            nivel5()
    seis()
    
#function that provides a certificate to the user
def certificado():
    global nombre
    input("Press ENTER to view your certificate")
    print(f'''
--------------------------------------------------------------------------------


                                        DIPLOMA
                            
                            
             Bloody Maths, son! is proud to award this diploma to:
                
                                {nombre}
                                
                    for having successfully completed all 6 levels of the game.
                    
                                    MANY CONGRATULATIONS
                                    
                                    And never forget...
                                
                                    Bloody Maths, SON!


                                    
                                    
--------------------------------------------------------------------------------
''')
#End of the program


#Calling to function
bienvenida_total()
