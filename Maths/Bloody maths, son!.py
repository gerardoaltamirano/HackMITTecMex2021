upper = 0
lower = 0
digit = 0
num = 0
space = 0
spaceU = 0
res = "si"
res2 = "si"
nombre = {}
#Función que le pide su nombre al usuario
def nombre_u():
    
    global nombre
    
    name = input("\nIntroduce tu nombre: ")
    nombre = name
    print("\nJoder gran nombre")
    
    usuario()
    
#Funcion que pide un usuario y valida que no tenga espacios
def usuario():
    #funcion para repetir el ciclo si no es válido el usuario
    def repite():
        global res2
        while res2 == "si":
            autentica()
            imprime()
        
        contraseña()
#Función que pide el usuario    
    def pide_usuario():
        
        usu = input("Introduce un usuario: ")
        
        return usu
#funcion que autentica que no tenga espacios
    def autentica():
        
        global spaceU
        
        user = pide_usuario ()
        
        luser = len(user)
        
        for pos  in range (0,luser):
            if user[pos].isspace() == True:
                spaceU += 1
#funcion que avisa si es que tiene espacios
    def imprime():
        
        global spaceU
        global res2

        if spaceU == 0:
            print ("Usuario válido")
            res2 = "no"
        else:
            print("Contiene espacios")
            print("Usuario Inválido")
            spaceU -= spaceU
                    
    repite()
#funcion que pide y autentica la contraseña
def contraseña():
#funcion para repetir el ciclo si no es válida la contraseña    
    def repite():
        global res
        while res == "si":
            autentica()
            imprime()
        
        respuesta_n()
#Funcion que pide la contraseña        
    def pide_contraseña():
        
        print('''
Recuerda que tu contraseña debe contener al menos:
                                - una mayúscula
                                - una minúscula
                                - un número
                                - un símbolo
                                - mínimo 8 dígitos
                                ''')
        
        cont = input("Introduzca una contraseña: ")
        
        return cont
#funcion que auntentica la contraseña
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
            print("No cumple con la longitud necesaria")
#funcion que avisa si la contraseña está mal
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
                            print ("Contraseña válida")
                            res = "no"
                        else:
                            print("Contiene espacios")
                            print("Contraseña Inválida")
                    else:
                        print("No contiene números")
                        print ("Contraseña inválida")
                else:
                    print("No contiene símbolos")
                    print ("Contraseña inválida")
            else:
                print("No contiene minúsculas")
                print ("Contraseña inválida")
        else:
            print("No contiene mayúsculas")
            print ("Contraseña inválida")
    repite()
#funcion que da la bienvenida
def bienvenida_total():
    
    print('''
¡MATEMÁTICAS, HIJO!
''')
    
    print('''
Bienvenido a ¡matemáticas, hijo!, un juego en el que no solo aprenderás sobre
matemáticas, pero también mejorarás tu puntaje en tu próxima prueba PISA.
¡Esperamos que te diviertas! Pero antes...''')
    
    nombre_u()
#funcion para o finalizar el programa
def respuesta_n():
    
    respuesta = "si"
    while respuesta == "si":
        menu()
        respuesta = input("¿Quieres correr el juego de nuevo?: ")
    print("Hasta pronto wuuuuu")
    input("Presiona ENTER para salir")
    respuesta = "no"
#funcion que pide al usuario la opcion del menu
def menu():
    print('''
Ahora, a decidir...

1) Repasar división con punto decimal
2) Repasar divisón de fracciones
3) Ir directo a los niveles
''')
    
    opc = int(input("¿Qué opción deseas realizar?: "))
    
    if opc == 1 or opc == 2 or opc == 3:
        desvio(opc)
    
    else:
        print("Número inválido")
        respuesta_n()
#Opción que devía la respuesta del usuario al menu        
def desvio(opcion):
    
    if opcion == 1:
        divisiones_con_decimales()
    elif opcion == 2:
        divisiones_con_fracciones2()
    else:
        nivel1()

#Funcion que activa la explicacion de divisiones con punto decimal
def divisiones_con_decimales():
    #Funcion que da la bienvenida a la explicacion
    def hola():
        hello = open("hola.txt","r",encoding="utf8")
        holi = hello.read()
        print(holi)
        print('''\nPara ver explicaciones gráficas de cómo se hicieron las divisiones
de los\nejemplos, visita: https://sabnrs.wixsite.com/matematicashijo''')
        
        cual()
    #funcion que pregunta al usuario por el caso que quiere ver
    def cual():
        opcion = input("\n¿Cuál caso quieres ver?: ")
        print("")
        casos(opcion)
    
    #Funcion para seguir viendo casos
    def seguir():
        
        ans = input("¿Deseas seguir viendo casos?: ")
        if ans.lower() == "si" or ans == "sí" or ans == "Sí":
            cual()
            
        else:
            print("Volviendo al menú principal")
            menu()
        
    #Funcion que filtra la opcion elegida por el usuario    
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
            print("Opción no válida. Intenta de nuevo.")
            cual()
    
    #Funcion que explica todos los casos
    def todo():
        expli = open("todos.txt","r",encoding="utf8")
        todoo = expli.read()
        print(todoo)
        seguir()
    
    #Funcion que explica el primer caso
    def uno():
        caso1 = open("uno.txt","r",encoding="utf8")
        unoo = caso1.read()
        print(unoo)
        seguir()
    
    #Funcion que explica el segundo caso
    def dos():
        caso2 = open("dos.txt","r",encoding="utf8")
        doss = caso2.read()
        print(doss)
        seguir()
    
    #Funcion que explica el tercer caso
    def tres():
        caso3 = open("tres.txt","r",encoding="utf8")
        tress = caso3.read()
        print(tress)
        seguir()
    
    #Funcion que explica el cuarto caso
    def cuatro():
        caso4 = open("cuatro.txt","r",encoding="utf8")
        cuatroo = caso4.read()
        print(cuatroo)
        seguir()
    
    hola()

#Funcion para la explicacion de division de fracciones
def divisiones_con_fracciones2():
    #funcion que da la bienvenida, pide el caso a escoger y lo filtra
    def divisiones_con_fracciones():
        
        welcome = open("bienvenida.txt", "r", encoding = "UTF8")
        bienvenida = welcome.read()
        print(bienvenida)
        
        options = open("opciones.txt", "r", encoding = "UTF8")
        opciones = options.read()
        print(opciones)
        
        opcion = int(input("\n¿Qué opción deseas visualizar? "))
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
            print("Esa no es una opción")
            print(" ")
            
    #muestra explicación para caso1
    def multiplicacion_en_cruz():
        
        first = open("multiplicacionEnCruz.txt", "r", encoding = "UTF8")
        primera = first.read()
        print(primera)
        
    #muestra explicación para casp 2
    def invertir_y_multiplicar():
        
        second = open("invertirYMultiplicar.txt", "r", encoding = "UTF8")
        segunda = second.read()
        print(segunda)
        
    #muestra explicación para ambos casos
    def ambos_metodos():
        
        multiplicacion_en_cruz()
        invertir_y_multiplicar()

    #funcion para sefuir viendo casos o ir a niveles de juego
    def continuar_o_niveles():
        
        c = open("continuar.txt", "r", encoding = "UTF8")
        conti = c.read()
        print(conti)
        
        continuar = int(input("\n¿Qué opción escoges?:  "))
        
        if continuar == 1:
            menu()
        
        elif continuar == 2:
            print("")
            divisiones_con_fracciones()
        
        elif continuar == 3:
            nivel1()
            
        else:
            print("Esa no es una opción")
            print(" ")
    
    divisiones_con_fracciones()

#nivel 1 del juego
def nivel1():
    
    #indicaciones del juego
    def indicaciones():
    
        indications = open("indicaciones.txt", "r", encoding = "UTF8")
        indicaciones = indications.read()
        print(indicaciones)
        ejercicio1()
    
    #Nivel 1 como tal
    def ejercicio1():
    
        print("\nNivel 1: \n(1/6)/(5/9)")
        respuesta1 = input("\n¿Cuál es el resultado?: ")
            
        if respuesta1 == "9/30" or respuesta1 == "3/10":
            print("¡Correcto!")
            nivel2()
        else:
            print("Respuesta incorrecta")
            print("")
            ejercicio1()
    
    indicaciones()

#nivel 2 del juego
def nivel2():
    print("\nNivel 2: \n2.35/5")
    respuesta1 = float(input("\n¿Cuál es el resultado?: "))
        
    if respuesta1 == .47:
        print("¡Correcto!")
        nivel3()
        
    else:
        print("Respuesta incorrecta")
        print("")
        nivel1()

#nivel 3 del juego
def nivel3():
    print("\n¡Nivel3!, vas a la mitad\n(347/38)/(255/32): ")
    resp = input("¿Cuál es la fracción resultante simplificada?: ")
    
    if resp == "5552/4845":
        print("HÉROE")
        nivel4()
    
    else:
        print("aaaasiiiiiisteeeeenteeeee, de regreso")
        nivel2()
    
#nivel 4 del juego
def nivel4():
    print("\nYA NIVEL 4 WUUUU\n345.654/32.987")
    resp = float(input("¿Cuál es el resultado de la división? Redondea a 3 decimales: "))
                        
    if resp == 10.478 or resp == 10.479:
        print("HÉROE")
        nivel5()
        
    else:
        print("aaaasiiiiiisteeeeenteeeee, de regreso")
        nivel3()
    
#nivel 5 del juego
def nivel5():
    #Muestra el problema del nivel
    def cinco():
        print("\nNIVEL 5")
        notanfeo = open("decimalnotanfeo.txt","r",encoding="utf8")
        notanfeoo = notanfeo.read()
        print(notanfeoo)
        
        cincoans()
    
    #pide respuesta al nivel y la filtra
    def cincoans():
        respues = float(input("Introduce tu respuesta: "))
        
        #respuesta correcta: 344.38
        if respues == 344.38:
            print("\n¡Correcto! Pasas al siguiente nivel :)\n")
            nivel6()
            
            #MANDA LLAMAR A ESTE NIVEL ?
            
        else:
            print("\nRespuesta incorrecta.\nRegresas al nivel anterior.\n")
            
            #Y AQUÍ LO REGRESA AL NIVEL PREVIO
            nivel4()
    
    cinco()

#nivel 6 del juego
def nivel6():
    
    #Muestra el problema del nivel
    def seis():
        print("\nNIVEL 6")
        feo = open("decimalfeo.txt","r",encoding="utf8")
        feoo = feo.read()
        print(feoo)
        
        seisans()
    
    #pide y filtra la respuesta 
    def seisans():
        respuest = float(input("Introduce tu respuesta: "))
        
        #respuesta correcta: 49.81
        if respuest == 49.81:
            print("\n¡Correcto! Has terminado ¡Matemáticas, Hijo! :)\n")
            
            #CERTIFICADO
            certificado()
            
        else:
            print("\nRespuesta incorrecta.\nRegresas al nivel anterior.\n")
            #Y AQUÍ LO REGRESA AL NIVEL PREVIO
            nivel5()
    seis()

#función que arroja un certificado al usuario
def certificado():
    global nombre
    input("Presiona ENTER para ver tu certificado")
    print(f'''
--------------------------------------------------------------------------------


                                        DIPLOMA
                            
                            
                A ¡matemáticas, hijo! nos enorgullece otorgar este diploma a:
                
                                {nombre}
                                
                    por haber concluido con éxito los 6 niveles del juego
                    
                                    MUCHAS FELICIDADES
                                    
                                    Y nunca olvides...
                                
                                    ¡MATEMÁTICAS, HIJO!
                                    
                                    
--------------------------------------------------------------------------------
''')
#fin del programa


#Llamando a función
bienvenida_total()
