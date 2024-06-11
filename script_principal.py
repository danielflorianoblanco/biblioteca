from funciones.agregarlibro import agregarLibro
from funciones.buscarLibro import buscarLibro
from funciones.eliminarLibro import eliminarLibro
from funciones.mostrarLibros import mostrarLibros
from funciones.siHayLibro import sihaylibro



def principal ():

    # Menu 
            
    print ("Gestion de la biblioteca")
    print ("1. Añadir un libro")
    print ("2. Mostrar todos los libros")
    print ("3. Buscar libro por autor")
    print ("4. Eliminar un libro")
    print ("5. Terminar el programa")

    opcion = input ("Introduce la opcion que necesitas\n")
            

    lista_libros = []


    match opcion:
        case "1":
            agregarLibro(lista_libros)

        case "2":
            if (sihaylibro(lista_libros) == False):
                pass
            else:
                mostrarLibros(lista_libros)
        
        case "3":
            if (sihaylibro(lista_libros) == False):
                pass
            else:
                buscarLibro (lista_libros)
        
        case "4":
            print ("Elige el libro que deseas eliminar")
            
            mostrarLibros(lista_libros)
            print ("Dime el titulo que deseas eliminar ")
            
            if (sihaylibro(lista_libros) == False):
                pass
            else:
                eliminarLibro(lista_libros)
        
        case "5":
            print ("Has elegido salir del programa")
        
        case "_":
            print ("Opcion no contemplada")


principal ()