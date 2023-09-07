#Codigos del primer semestre de programacion DUOC UC
from time import time
tiempo_inicio = time();
from colorama import Fore, init         #Detalle voluntario (Colores)
from datetime import datetime as tiempo #Detalle voluntario (Fecha y hora)
fecha_actual = tiempo.now() #Se obtiene la hora y fecha actual

formato_fecha = fecha_actual.strftime("%d-%m-%Y");
formato_hora = fecha_actual.strftime("%H:%M %p");

flaguser = False;           #Uso de bandera
user1 = 'fcalfun';          #usuario 1
passw1 = 1234;
user2 = 'cbrandon';         #usuario 2
passw2 = 1234;

tipo_usuario = 0;
cantidad_impresion = 0;

intentos = 0;
total = 0;
precio = 0;
invocar = 0;
invocar1 = 0;
                    #Detalles adicionales
descuentoa = 0;     #Solamente mostrara el porcentaje del cliente
descuentob = 0;     #Calculara el porcentaje del cliente con el precio total a pagar

tipo_inpresion = 0; #Representado lo dos tipos de impresion

menu = int;         #Nos pide definir el menu ya que esta dentro del while


print("-" * 43);
print("|     Bienvenido a La institución de      |");
print("| " + Fore.YELLOW + "                Duoc" + Fore.BLUE + "UC" + Fore.RESET + "                  |");
print("-" * 43);
print("|                [LOGIN]                  |");
print("-" * 43);

while intentos != 3:
    print(f"\nIntentos: {intentos} ");
    user = str(input("Nombre de usuario: "));

    try:
        passw = int(input("Contraseña: "));
        intentos += 1
        print("\n" + "-" * 43);
    
    except ValueError:
        print(Fore.RED + "¡SOLAMENTE SE ADMITEN DATOS DE TIPO ENTERO! Vuelva a intentar denuevo porfavor..", Fore.RESET);
        intentos += 1;
    
    if user == user1 and passw == passw2 or user == user2 and passw == passw2:
        break; #Si usuario ingreso correctamente sus datos saldra del buble while   
    elif intentos == 3:
        print("\n¡Ha superado la cantidad maxima de intentos!");
        print(f"Intentos: {intentos}\n");
        break;

while flaguser == False: #mienetras bandera sea falso el ciclo se repetira..
    if user == user1 and passw == passw2 or user == user2 and passw == passw2:
        flaguser = True; #mientras tanto si es true se rompera el cilo while de ingreso a los usuarios..
        print("\n"*3 + Fore.GREEN + f'Bienvenido {user}. ¡Usted a ingresado sus datos con exito! ', Fore.RESET);
        
        try:
            print("\n" + "-"*43);
            print("|            TIPO DE USUARIO              |");
            print("-"*43);
            print("|   ¡INGRESE LA OPCION CORRESPONDIENTE!   |");
            print("-"*43);
            tipo_usuario = int(input("\n(1). Diurna\n(2). Vespertina\n(3). Administrativo\n(4). Salir del programa\n\nOpcion: "));

               
            while flaguser:
                print("-"*32);
                print("|\t     [MENU]            |");
                print("-"*32);
                print("| OPC | TIPO SERVICIO | PRECIO |");
                print("-"*32);
                print( "| 1.  |   Inpresión:           |\n|     |   B/N           $150   |  \n|     |   Color:        $300   |\n| 2.  |   Fotocopias:   $80    |\n| 3.  |   Anillados:    $5.000 |\n| 4.  |   Anular pedido        |\n| 5.  |   Salir del programa   |\n--------------------------------");

                if invocar > 1: #Invocar: Presenta un mensaje donde el usuario escoje una opcion y este mostrata la opcion escojida. sto es para saber donde recorre el codigo y verificar que las opciones escojidas van por buen camino.
                    print(Fore.LIGHTGREEN_EX+"¡HA VUELTO  AL MENU PRINCIPAL!", Fore.RESET);
                    invocar = 0;
                if invocar1 > 1:
                    print(Fore.RED+"¡HA ANULADO EL PEDIDO!",Fore.RESET);
                    invocar1 = 0;
                
                try:

                    menu = int(input("\nOpcion del menu: "));
                    
                    if menu == 1:
                        print("\n" + "-" * 43);
                        print ("|\t    TIPO DE IMPRESION             |");
                        print("-" * 43);
                        tipo_inpresion = int(input("\n1- Impresion: B/N $150\n2- Color $300\n\nOpcion: "));
    
                        if tipo_inpresion == 1:
                            cantidad_impresion = int(input("Cantidad de hojas B/N: "));
                            precio = cantidad_impresion  * 150;
                            total = total + precio

                        elif tipo_inpresion == 2:
                            cantidad_impresion = int(input("Cantidad de hojas a color: "));
                            precio = cantidad_impresion * 300;
                            total = total + precio;
                        else:
                            print(Fore.RED+"¡Esta opcion no existe!",Fore.RESET);
                
                    elif menu == 2:
                        print("\n" + "-"*43);
                        print("|            FOTOCOPIAS A $80             |");
                        print("-"*43,"\n");
                        cantidadfoto = int(input("Cantidad de Fotocopias: "));
                        precio = cantidadfoto * 80;
                        total = total + precio;
                    
                    elif menu == 3:
                        print("\n" + "-"*43);
                        print("|            ANILLADOS A $5.000           |");
                        print("-"*43,"\n");
                        cantidadanillados = int(input("Cantidad de Anillados: "));
                        precio = cantidadanillados * 5000;
                        total = total + precio;
                
                    elif menu == 4: #El usuario volvera al principio, esta vez los datos ingresados o comprados seran reiniciados.
                        cantidad_impresion = 0;
                        cantidadfoto = 0;
                        cantidadanillados = 0;
                        precio = 0;
                        total = 0;
                        invocar1 += 2;
                    
                    elif menu == 5:
                            print("\n---------------------------------------------");
                            print(f"|{Fore.RED}\t   ¡PROGRAMA FINALIZADO!         {Fore.RESET}|");
                            break
                        
                    else:
                        print(Fore.RED+"¡Esta opcion no existe!",Fore.RESET);
                    
                    if menu == 1 or menu == 2 or menu == 3:
                        print("\n" + "-"*43);
                        print("|            OPCION DEL PROGRAMA          |");
                        print("-"*43);
                        menu = int(input("(5). Salir del programa \n(6). Volver al menu principal\n\nOpcion: "));
                        
                        if menu == 6: #Se le dara un aviso que al usario que volvio a ingresar al menu principal (Bucle) para ahorrar codigo volvera al principio.
                            invocar += 2;
                        
                        elif menu == 5:
                            print("\n---------------------------------------------");
                            print(f"|{Fore.RED}\t   ¡PROGRAMA FINALIZADO!         {Fore.RESET}|");
                            break

                        else:
                            print(Fore.RED+"¡Esta opcion no existe!",Fore.RESET);
                                        
                except ValueError:
                    print(Fore.RED + "¡SOLAMENTE SE ADMITEN DATOS DE TIPO ENTERO! Vuelva a intentar denuevo porfavor..", Fore.RESET);
            
            #Descuento A: Muestra en el terminal el porcentaje del descuento. Descuento B: muestra el descuento del total de la compra.        
            if tipo_usuario == 1:
                descuentoa = 10;
                descuentob = total * 0.10;
            elif tipo_usuario == 2:
                descuentoa = 20;
                descuentob = total * 0.20;
            elif tipo_usuario == 3:
                descuentoa = 0;
                descuentob = total * 0;
            
            print("---------------------------------------------");
            print("|          Servicio de Fotocopiado          |");
            print("---------------------------------------------");
            print(f'  Subtotal: ${total}                         ');
            print(f'  Descuento del %{descuentoa}: ${round(descuentob)}');
            print("---------------------------------------------");
            print(f'  Total a pagar: ${round(total - descuentob)}');
            print("---------------------------------------------");
            print("  Fecha de la compra:", formato_fecha);
            print("  Hora de la compra: ", formato_hora);
            tiempo_final = time()
            tiempo_ejecucion = round(tiempo_final - tiempo_inicio);
            print("  Tiempo de ejecucion:",tiempo_ejecucion," Segundos");
            print("---------------------------------------------");
            print("|\t  ¡Gracias por su compra!           |");
            print("|\t\t",Fore.YELLOW + "  Duoc"+Fore.BLUE+"UC", Fore.RESET,"                 |");
            print("---------------------------------------------");
        
        except ValueError:
            print(Fore.RED + "¡SOLAMENTE SE ADMITEN DATOS DE TIPO ENTERO! Vuelva a intentar denuevo porfavor..", Fore.RESET);
      
    else:
        print(Fore.RED + "¡LOS DATOS INGRESADOS SON INCORRECTOS! Solo se admiten usuarios registrados..", Fore.RESET); 
        break;

#Creado por Brandon luis casas :)
#19-07-2023
