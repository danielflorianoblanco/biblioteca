def agregarLibro (lista_libros):

    print ("Añadir un libro")
    tituloLibro = input("Dame el titulo del libro").lower()
    autorLibro = input("Dame el autor del libro").lower()
        
    while True:
        try: 
            fechaLibro = int(input("Dame la fecha del libro"))
            break
        except ValueError:
            print ("Introduce un valor numerico") 

    libro = {

        "titulo" : tituloLibro,
        "autor" : autorLibro,  
        "fecha" : fechaLibro
    }    

    lista_libros.append(libro)
    
    return(lista_libros)