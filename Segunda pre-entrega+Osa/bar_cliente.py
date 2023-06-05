import os
import json


class Cliente:
    cliente = {}
    cliente["usuarios"] = []
    compra = []

    def __init__(self,Email,Nombre,Apellido,Clave):   # metodo init=> metodo constructor
        self.Email = Email  
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Clave = Clave    

    def __str__(self):
        return f"El cliente es {self.Nombre} {self.Apellido} y su casilla de Email es {self.Email}"

    def registrar_cliente(self):
        
        cliente = {
            'Email': self.Email,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'Clave': self.Clave
        }
        os.system("cls")

        if not os.path.exists("usuarios.json"):                #crear el archivo JSON
            with open("usuarios.json", "w") as file:
                json.dump({"usuarios": []}, file)

        with open("usuarios.json", "r") as file:
            data = json.load(file)
            file.close()
        data["usuarios"].append(cliente) 
        with open("usuarios.json", "w") as file:
            json.dump(data,file)  
            file.close()
        print("Registro exitoso")


    def iniciarSesion(self,Email_input,Clave_input):
        self.Email = Email_input
        self.Clave = Clave_input 
        
        os.system("cls")
        with open("usuarios.json", "r") as file:  
            data = json.load(file)
            for user in data['usuarios']:
                if(user["Email"] == self.Email and user["Clave"] == self.Clave):
                    Nombre = user["Nombre"]
                    print(f"Bienvenido al Bar Tito {Nombre}")
                    file.close()
                    return Nombre
            else:
                print("Usuario o contraseña incorrectos")
                return None
            
    def pedido(self,Nombre_pedido):
        self.Nombre =Nombre_pedido
        print(f'{self.Nombre} haga su pedido por favor.')
        with open("menu.json", "r") as file:  
            data = json.load(file)
            indice = 0
            for dic_prod in data['menu'][0]:
                prod = dic_prod["Producto"]
                precio = dic_prod["Precio"]
                indice += 1
                cantidad = int(input(f"Cuantos {prod} quiere?"))
                valor = cantidad * precio
                print(valor)
                Cliente.compra.append(valor)
                file.close()
        print(f"Su total de su compra es ${sum(Cliente.compra)}")


cliente1 = Cliente("pipo@gmail.com", "Pipo", "Cipolatti", "123")

print(cliente1)