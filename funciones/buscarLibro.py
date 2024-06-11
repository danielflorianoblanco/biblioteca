def buscarLibro (lista_libros):
    print ("Buscar libro por autor")
    autorBusqueda = input("Dime un autor").lower()
    for libro in lista_libros:
        if libro["autor"] == autorBusqueda:
            print(f"Se ha encontrado el {autorBusqueda} en {libro['titulo']}")
        else:
            pass    
