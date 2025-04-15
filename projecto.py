Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

while True:
    print("========================================")
    print("Lista de Productos:")
    print("========================================")
    print(f"{'Código':<5} {'Producto':<12} {'Precio':<10} {'Stock':<5}")  # Títulos de columnas
    
    for key in Productos:
        print(f"{key:<5} {Productos[key]:<12} {Precios[key]:<10} {Stock[key]:<5}")  # Imprimir productos alineados
    
    print("========================================")
    
    print("\nOpciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        nombre = input("Nombre del nuevo producto: ")
        precio = float(input("Precio del producto: "))
        stock = int(input("Stock inicial: "))
        
        nuevo_codigo = max(Productos.keys()) + 1
        Productos[nuevo_codigo] = nombre
        Precios[nuevo_codigo] = precio
        Stock[nuevo_codigo] = stock

        print(f"\nProducto '{nombre}' agregado exitosamente con código {nuevo_codigo}.\n")

    elif opcion == '2':
        codigo = int(input("Ingrese el código del producto a eliminar: "))
        
        if codigo in Productos:
            nombre_eliminado = Productos[codigo]
            del Productos[codigo]
            del Precios[codigo]
            del Stock[codigo]
            print(f"\nProducto '{nombre_eliminado}' eliminado exitosamente.\n")
        else:
            print("Código no válido. Intenta de nuevo.\n")

    elif opcion == '3':
        codigo = int(input("Ingrese el código del producto a actualizar: "))

        if codigo in Productos:
            print(f"\nProducto actual: {Productos[codigo]} - Precio: S/. {Precios[codigo]} - Stock: {Stock[codigo]}")

            nuevo_nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            nuevo_stock = input("Nuevo stock (dejar en blanco para no cambiar): ")

            if nuevo_nombre:
                Productos[codigo] = nuevo_nombre
            if nuevo_precio:
                Precios[codigo] = float(nuevo_precio)
            if nuevo_stock:
                Stock[codigo] = int(nuevo_stock)

            print(f"\nProducto con código {codigo} actualizado exitosamente.\n")
        else:
            print("Código no válido. Intenta de nuevo.\n")

    elif opcion == '4':
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta de nuevo.\n")
