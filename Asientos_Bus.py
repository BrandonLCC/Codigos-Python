#Ejercicio 2: Crear un arreglo de dos dimensiones de tamaño 10 y 4, el cual, 
#simula a un bus. Se pide asignar los números de asiento en forma automática, considerando el siguiente formato:

from colorama import *;
import numpy as np;

salir = False;
FlagValid = False; 
salir_menu = 0;

mensaje = 0;
asientos = 0;
cantidad_asientos = 0;

#(1).   La rimera parte del codigo es crear los asientos disponibles. 
#(1.1). Para eso vamos a generar un arreglo de 10 x 4: 4 filas de 10 de largo de tipo (object: Nos permite ingresar una "X" al ingresar un asiento).
#(1.2). Para rellenar las filas y columnas usaremos for.

escenario = np.empty((10,4), dtype= object); 
for fila in range(10):                          
    for columna in range(4):                    
        asientos += 1;                          
        escenario[fila,columna] = asientos;

#(2). Presentaciòn del programa "BUS".

print("\n" + "*"* 25);
print("\n",Fore.LIGHTGREEN_EX + "  ¡BIENVENIDO AL BUS!\n", Fore.RESET);
print("*"* 25);
    
print("***     "+ Fore.LIGHTGREEN_EX + "ASIENTOS"+ Fore.RESET +"      ***\n");
print(escenario);
print("\n" + "*"* 25);
print(Fore.LIGHTYELLOW_EX + "\n      Escoja un\n  Asiento disponible.\n", Fore.RESET);

print("*"* 25,"\n");

#(2.1). Fin de la presentaciòn del programa "BUS".

while salir != True:
    if mensaje > 0:
        #(3). En el "if mensaje > 0:" indica que una vez que el usuario quiera volver a escojer un asiento,
        # Dara una nueva presentaciòn del escenario. 
        print("\n"*2 + "*"* 25);
        print(Fore.LIGHTGREEN_EX + "\n   ¡Usted ha vuelto\n     Al principio!\n", Fore.RESET);
        print("*"* 25,"\n");
        print(escenario);
        print("\n","*"* 25);

        print(Fore.LIGHTYELLOW_EX + "\n      Escoja un\n  Asiento disponible.\n", Fore.RESET);
        print("*"* 25,"\n");
        mensaje = 0; 
        FlagValid = False

        #(3.1). Fin de la presentaciòn del bucle "if mensaje > 0:".

    try:
        #(4). El usuario ingresara su fila y columna para marcar con "X" el asiento escojido.

        fila = int(input("Fila: "));
        columna = int(input("Columna: "));
        print("\n")
        fila -= 1;
        columna -= 1;
        
        #(4.1). En fila -= 1 y columna -= 1 ajustaremos los datos ingresados ya que las posiciones de los arreglos empiezan desde 0.

        if fila <= -1 and columna <= -1 or fila >= 11 and columna >= 5 : 
            while FlagValid != True:
                try:
                    #(5). Si se cumple con la condicion if ingresara en un bucle infinito. 
                    #(5.1). El usuario debera ingresar los datos permitidos por el programa para poder salir del bucle.
                    
                    print("*"* 25,"\n");
                    print(Fore.LIGHTRED_EX + " ¡Usted ha ingresado un dato \n      Fuera del rango!",Fore.RESET + Fore.LIGHTGREEN_EX + " \n\n  Porfavor vuelva a ingresar \n        los datos.", Fore.RESET);
                    print("\n" + "*"* 25);
                    fila = int(input("\nFila: "));
                    columna = int(input("Columna: "));
                    print("\n" + "*"* 25,"\n");
                        
                    if fila >= 0 and columna >= 0 or fila <= 9 and columna <= 4:
                        fila -= 1;
                        columna -= 1;
                        FlagValid = True; 
                    
                    #(5.2). Si el usuario cumple con las condiciones que pide el programa podra salir del bucle con "FlagValid".
                            
                    else:
                        print(Fore.LIGHTRED_EX + "   !Intente nuevamente a\n escojer su asiento disponible!\n", Fore.RESET);
                        print("\n" + "*"*25,"\n");
                        print(" ¡ENTRADAS DISPONIBLES!");
                        print("\n" + "*"*25,"\n");
                        print(escenario);
                        print("\n" + "*"*25,"\n");
                
                    #(5.3). De lo contrario, si el usuario no cumple con las condiciones establecidad se le volvera a mostrar el escenario para escojer de forma valida su asiento disponible.
                                
                except ValueError:
                    print(Fore.LIGHTRED_EX + "\n¡SOLAMENTE SE ADMITEN\n DATOS DE TIPO ENTERO.\n", Fore.RESET);
                    print("-" * 25,"\n");

                except IndexError:  
                    print("\n" + Fore.LIGHTRED_EX + "¡HA INGRESADO UN NUMERO \nMAYOR AL PERMETIDO!\n", Fore.RESET);
   
        try:
            if fila >= 0 and columna >= 0 and  Fore.RED + "X" + Fore.RESET:
                escenario[fila, columna] = Fore.RED + "X" + Fore.RESET;
                cantidad_asientos += 1;                                      # Segun la columna y fila del escenario.
                                                                                
            else:
                print(Fore.LIGHTRED_EX + "\n¡LO SENTIMOS! EL ASIENTO NO SE ENCUENTRA DISPONIBLE.", Fore.RESET); 
        
        except IndexError:
            print("\n" + Fore.LIGHTRED_EX + "¡HA INGRESADO UN NUMERO \nMAYOR AL PERMETIDO!", Fore.RESET);
    
        #(7). Una vez pasado por todos los filtros que se necesitan para escojer un asiento, se volvera a mostrar el menu 
        #     donde se le mostrara al usuario los asientos escojidos 

        print("\n" + "*"*25,"\n");
        print(Fore.LIGHTGREEN_EX + " ¡ENTRADAS DISPONIBLES!", Fore.RESET);
        print("\n" + "*"*25,"\n");
        print(escenario);
        print("\n" + "*"*25,"\n");

        while True:
            try:
                #(8). Se le dara la opcion al usuario si desea volver a escojer asientos.
                # Son dos opciones las cuales son, volver al programa o salir del programa.

                salir_menu = int(input("¿Desea volver a escojer un asiento?\n\n(" + Fore.LIGHTGREEN_EX + "0" + Fore.RESET + "). Volver al programa\n(" + Fore.LIGHTRED_EX + "1" + Fore.RESET + "). Salir del programa\n\nOpcion: "));
                
                if salir_menu == 1: #(8.1). Si el usuario ingresa la opcion (0) saldra del primer bucle y para posterior salir del programa
                    salir = True;
                    break;

                elif salir_menu == 0: #(8.2). Si el usuario ingresa la opcion (1) volvera al programa rompiendo el bucle principal.
                    mensaje += 1;
                    break;
                
                else:
                    print("\n" + Fore.LIGHTRED_EX + "\n¡VUELVA A INTENTAR NUEVAMENTE!", Fore.RESET); #(8.3). Si el usuario desea escojer una opcion fuera de lo establecido saldra un mensaje
                                                                                                     # Obligando al usuario volver a ingresar una opcion valida.
            except ValueError:
                print(Fore.LIGHTRED_EX + "\n¡SOLAMENTE SE ADMITEN\n DATOS DE TIPO ENTERO.\n", Fore.RESET);
    
    except ValueError:
        print(Fore.LIGHTRED_EX + "\n¡SOLAMENTE SE ADMITEN\n DATOS DE TIPO ENTERO!.\n", Fore.RESET);  

#Final del programa.
#Se mostrara los asientos escojidos por el usuario,
#la cantidad de asientos y un mensaje de agradecimiento.

print("\n"*2 + "*"*25);
print(Fore.LIGHTGREEN_EX + "   ASIENTOS TOTALES ", Fore.RESET);
print("*"*25);
print(escenario);
print("\n" + "*"*25);
print("\nAsientos adquiridos:", Fore.LIGHTGREEN_EX + (str(cantidad_asientos)), Fore.RESET);
print( "\n" + "*"*25);
print(Fore.LIGHTYELLOW_EX + " ¡Muchas gracias por");
print(" ingresar al sistema!", Fore.RESET);
print("*"*25);

#17/08/2023 - Brandon Casas.
