import os
from bar_cliente import Cliente
from bar_menu import *

def opcion():
    entrar = False
    while not entrar:
        try:
            entrada = int(input('Que desea hacer? '))

            if (entrada == 1):
                entrar = True
                print('Iniciar sesión: ')
                Email_input=input("Correo: ")
                Clave_input= input("Contraceña: ")
                clienteIS = Cliente("","","","")
                nombre_pedido = clienteIS.iniciarSesion(Email_input,Clave_input)

                if clienteIS:
                    dar_menu()
                    clienteIS.pedido(nombre_pedido)

                break
            elif (entrada == 2):
                entrar = True    
                print('Registrese: ')
                Email =input("Email: ")
                Nombre = input("Nombre: ")
                Apellido = input("Apellido: ")
                Clave = input("Contraseña: ")
                cliente1 = Cliente(Email,Nombre,Apellido,Clave)
                cliente1.registrar_cliente()
                
                break
            else:
                print('Opcion no valida. \nPara iniciar sesión: 1 \nPara registrarse: 2')

        except ValueError:
            print('No se puede escribir caracteres que no sean numeros')
        except FileNotFoundError:
            print("El usuario indicado no existe. Por favor, genere su usuario.")
        except TypeError:
            print('No se puede realizar esta operacion con string')
        except Exception as e:
            print(f'Error inesperado {type(e).__name__}. Intente de nuevo:\nPara iniciar sesión: 1 \nPara registrarse: 2')


os.system("cls")

print('Bienvenido al Bar Tito!!\nPara iniciar sesión: 1 \nPara registrarse: 2')

opcion()