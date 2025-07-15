import time

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}



def stock_marca(marca):
    stock_total = 0
    for modelo,datos in productos.items():
        if datos[0].lower() == marca.lower():
            stock_total += stock[modelo][1]
    print(f"el stock de la marca eleguida es: {stock_total}")

def buscar_precio(precio_min,precio_max):
    encontrados = 0
    for modelo,datos in stock.items() and productos,items():
        if precio_min <= stock[modelo][0] and  precio_max >= stock[modelo][0]:
            if modelo in stock and stock[modelo][1] > 0 and stock[modelo][0] <= precio_max:
                print(datos)
        
def actualizacion_precio(modelo,precio):
    if modelo in productos and modelo in stock:
        stock         


def menu():
    while True:
        print("******** Menu Principal**********")
        print("1. stock marca")
        print("2. busqueda por precio")
        print("3. actualizar precio")
        print("4. salir")

        op = input("ingresa opcion (1-4): ")

        if op == "1":
            marca = input("ingresa marca (hp, lenovo,asus,dell): ")
            stock_marca(marca)
            time.sleep(2)

        if op == "2":
            while True:
                try:
                    precio_min = int(input("ingresa precio minimo: "))
                    precio_max = int(input("ingresa precio maximo: "))
                    break
                except ValueError:
                    print("ingrese opcion valida")
                
                
            buscar_precio(precio_min,precio_max,)

        if op == "3":
            while True:
                in
                actualizar = int(input("ingrese nuevo precio"))




        if op == "4":
            print("programa finalizado")
        else:
            print("ingrese opcion valida.")


menu()