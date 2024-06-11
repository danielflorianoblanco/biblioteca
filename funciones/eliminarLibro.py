def eliminarLibro (lista_libros):

    tituloBusqueda = input("Dime un titulo").lower()
        
    for libro in lista_libros:
        if libro["titulo"] == tituloBusqueda:
            lista_libros.remove(libro)
        else:
            pass 