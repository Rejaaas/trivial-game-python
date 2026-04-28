import json
import time
import random
import os  # para limpiar la


# función que al llamarla limpia la pantalla
def limpiar_pantalla():
    os.system("cls")  # limpia la terminal


# 1 funcion creaar usuario
def crear_usuario():
    limpiar_pantalla()
    with open("jugadores.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        # mostrar  el diccionario
        # print(data)

        # pdeimos los datos al usuario
        print("CREAR NUEVO USUARIO")
        nuevo_nombre = input("Ingresa tu nombre: ")
        nuevo_gametag = input("Ingresa el gametag: ")
        nueva_edad = int(input("Ingresa la edad: "))

        # crear el diccionario del nuevo jugador

        nuevo_jugador = {
            "nombre": nuevo_nombre,
            "gametag": nuevo_gametag,
            "edad": nueva_edad,
            "puntos": 0,  # siempre fijo
        }

        # añadimos la lista de usuarios
        # accedemos a la clave 'usuarios' del json y usamos.append() para añadir el nuevo
        data["usuarios"].append(nuevo_jugador)

        # guardamos, realmente sobreescribimos.

        with open("jugadores.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)  # indent 4 pone el formato
        print("Usuario creado correctamente")


# 2 función seleccionar usuario (de los que hay)
def seleccionar_usuarios():
    limpiar_pantalla()
    with open("jugadores.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    usuarios = data["usuarios"]

    print("SELECCIONA TU GAMETAG: ")
    print("------------------------------")
    print("\n")

    # mostrar gametag con indice
    total = 0
    for i, user in enumerate(usuarios):

        print(f"{i + 1}. {user['gametag']}")
        print("\n")
        total += 1

    usuario_selecionado_bien = True
    print("------------------------------")
    opcion = int(input("Elige el número de tu jugador: "))
    if opcion <= total:
        jugador_elegido = usuarios[opcion - 1]
    else:
        usuario_selecionado_bien = False

    while usuario_selecionado_bien == False:
        opcion = int(input("Elige el número de tu jugador: "))
        if opcion <= total:
            jugador_elegido = usuarios[opcion - 1]
            usuario_selecionado_bien = True

    return jugador_elegido


# 4 coger preguntas
def acceder_preguntas(modalidad, jugador):
    limpiar_pantalla()
    # rutas de los archivos
    rutas = {
        1: "preguntas/acertijos.json",
        2: "preguntas/ciencia.json",
        3: "preguntas/culturaPop.json",
        4: "preguntas/deportes.json",
        5: "preguntas/historia.json",
        6: "preguntas/literatura.json",
        7: "preguntas/matematicas.json",
        8: "preguntas/paises.json",
        9: "preguntas/tecnologia.json",
    }

    preguntas = []

    # modalidad aleatoria (mezcla de todo)

    if modalidad == 10:
        for ruta in rutas.values():
            with open(ruta, "r", encoding="utf-8") as file:
                datos = json.load(file)
                preguntas.extend(datos)
    # por categoria
    else:
        ruta = rutas[modalidad]  # segun número accedemos al diccionario
        with open(ruta, "r", encoding="utf-8") as file:
            preguntas = json.load(file)

    # escoger 15 preguntas aleatorias

    if len(preguntas) > 15:
        preguntas = random.sample(preguntas, 15)

    print("EMPIEZA EL JUEGO\n")

    # jugar
    contador_correctas = 0
    contador_incorrectas = 0

    for item in preguntas:
        print("-" * 50)
        print("\n")
        print(item["pregunta"])
        print("\n")

        opciones = item["opciones"]

        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion} \n")

        print("-" * 50)
        seleccion = int(input("Tu respuesta: "))
        if 1 <= seleccion <= len(opciones):
            respuesta_usuario = opciones[seleccion - 1]

            if respuesta_usuario == item["respuesta_correcta"]:
                contador_correctas += 1
                jugador["puntos"] += 100
                print(" ✅ Correcto")
            else:
                contador_incorrectas += 1
                jugador["puntos"] -= 100
                print(f" ❌ Incorrecta. Era {item['respuesta_correcta']}")
        else:
            print(f" ❌ Incorrecta. Era {item['respuesta_correcta']}")
            contador_incorrectas += 1
            jugador["puntos"] -= 100

        time.sleep(
            1.5
        )  # pausa para que al usuario le de tiempo a ver si lo ha hecho bien o no
        limpiar_pantalla()

    with open("jugadores.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for user in data["usuarios"]:
        if user["gametag"] == jugador["gametag"]:
            user["puntos"] = jugador["puntos"]
            break

    with open("jugadores.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Juego terminado")
    print(f"Aciertos: {contador_correctas}")
    print(f"Fallos: {contador_incorrectas}")
    print(f"Puntos finales: {jugador['puntos']}")
    voler_a_menu = input("Enter para volver al menu: ")


# 3 funcion el usuario escoge si jugar a un tema o todos los temas
def jugar(name):
    limpiar_pantalla()
    print(f"Bienvenido al Juego, {name['gametag']}")
    print("\n")

    while True:
        print("Escoge una Modalidad: ")
        print("------------------------------")
        print("\n")
        print("1 - Modalidad aleatoria (Mezcla de todo)")
        print("\n")
        print("2 - Modalidad por Categoría")
        print("\n")
        print("------------------------------")
        opcion = int(input("Escoge (1 -2):"))

        if opcion == 1:
            print("Has escogido Modalidad Aleatoria")
            return 10

        elif opcion == 2:
            limpiar_pantalla()
            while True:
                print("\n" * 2)
                print("--- TEMÁTICAS ---")
                print("------------------------------")
                print("\n")
                print("1 - Acertijos \n ")

                print("2 - Ciencia \n ")

                print("3 - Cultura Pop \n ")

                print("4 - Deportes \n ")

                print("5 - Historia \n ")

                print("6 - Literatura \n ")

                print("7 - Matematicas \n ")

                print("8 - Paises \n ")

                print("9 - Tecnologia \n ")
                print("------------------------------")
                tematica = int(input("Escoge una temática (1 - 9): "))

                if 1 <= tematica <= 9:
                    return tematica
                else:
                    limpiar_pantalla()
                    print("Número incorrecto. Por favor, elige entre 1 y 9. \n")

        else:
            print("Opción no válida. Elige 1 o 2.")
            print(" ")
            limpiar_pantalla()


############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
# menu e inicio del juego

menu = True
gametag = None

while menu == True:
    limpiar_pantalla()

    print("🎮🎮 TRIVIAL DE JULEN 🎮🎮")
    print("\n")
    print("----------------------------")
    print("1 - QUIERO CREAR UN USUARIO")
    print("\n")
    print("2 - SELECCIONAR USUARIO Y JUGAR")
    print("\n")
    print("3 - JUGAR COMO INVITADO / USUARIO ACTUAL")
    print("\n")
    print("4 - Salir")
    print("----------------------------")

    opcion_menu = int(input("Tu opcion: "))

    if opcion_menu == 1:
        crear_usuario()

    elif opcion_menu == 2:
        gametag = seleccionar_usuarios()
        # obtener id
        id_categoria = jugar(gametag)
        # 2. pasar a la funcion
        acceder_preguntas(id_categoria, gametag)

    elif opcion_menu == 3:
        if gametag is None:
            usuario_actual = {"gametag": "Invitado", "puntos": 0}
        else:
            usuario_actual = gametag

        # obtener id
        id_categoria = jugar(usuario_actual)
        # pasar función
        acceder_preguntas(id_categoria, usuario_actual)

    elif opcion_menu == 4:
        print("Adiós!")
        menu = False
