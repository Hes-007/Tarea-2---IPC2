from ListaCircularDoblementeEnlazada import ListaCircularDoblementeEnlazada

listado = ListaCircularDoblementeEnlazada()

listado.AgregarInicio(2)
listado.AgregarInicio(7)
listado.AgregarInicio(5)
listado.AgregarInicio(11)
listado.AgregarInicio(4)


print("Lista Completa: ")
listado.RecorrerFinInicio()


print("Seleccione un número: ")
valor = input()
if valor == "2":
    listado.buscar(2)
elif valor == "7":
    listado.buscar(7)
elif valor == "5":
    listado.buscar(5)
elif valor == "11":
    listado.buscar(11)
elif valor == "4":
    listado.buscar(4)
else:
    print("El número seleccionado no se encuentra en la lista")

