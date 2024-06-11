def mostrarLibros (lista_libros):
    print ("Mostrar todos los libros")
    for indice, libro in enumerate (lista_libros):
        print (f"\nLibro numero {indice+1}")
        for key, value in libro.items ():
                print (f"{key} : {value}")