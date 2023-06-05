import os
import json

def dar_menu():
    productos = [
        {"id":"1", "Producto": "Hamburguesa","Precio": 1300 },
        {"id":"2", "Producto": "Pancho","Precio": 800 },
        {"id":"3", "Producto": "Papas Fritas","Precio": 800 },
        {"id":"4", "Producto": "Gaseosa","Precio": 400 },
        {"id":"5", "Producto": "Cerveza","Precio": 600 },
        {"id":"6", "Producto": "Helado","Precio": 700 }
    ]
   
    if not os.path.exists("menu.json"):                #crear el archivo JSON
        with open("menu.json", "w") as file:
            json.dump({"menu": []}, file)

    with open("menu.json", "r") as file:
        data = json.load(file)
        file.close()
    data["menu"].append(productos) 

    with open("menu.json", "w") as file:
        json.dump(data,file)  
        file.close()

    with open("menu.json", "r") as file:  
        data = json.load(file)
        indice = 0
        print("Menu: \n")
        for dic_prod in data['menu'][0]:
            id = dic_prod["id"]
            prod = dic_prod["Producto"]
            precio = dic_prod["Precio"]
            indice += 1
            print(f"{id}  {prod}  {precio} \n")
            file.close()


