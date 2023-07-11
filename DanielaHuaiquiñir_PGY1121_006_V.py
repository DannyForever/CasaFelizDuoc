import datetime
from datetime import datetime
now = datetime.now()

detalle_deptos = [
    {'Departamento': '1', 'Tipo': 'A', 'Precio UF': 3800},
    {'Departamento': '2', 'Tipo': 'B', 'Precio UF': 3000},
    {'Departamento': '3', 'Tipo': 'C', 'Precio UF': 2800},
    {'Departamento': '4', 'Tipo': 'D', 'Precio UF': 3500},
]

edificio = [[' ' for _ in range(4)] for _ in range(10)]
depto_seleccionado = []
lista_compradores = []

def ver_deptos():
    print("\nMAPA DE EDIFICIO")
    for fila in edificio:
        for disponibilidad in fila:
            print('[ ]' if disponibilidad == ' ' else '[X]', end=' ')
        print()

def seleccion_depto():
    while True:
      try:
        select_piso = int(input("Ingrese número de piso (0-9): ")) #Siendo 0 el 10º piso y 9 el 1º piso
        select_depto = int(input("Ingrese número de depto (A(0)-D(3)): ")) #Siendo 0 el depto A y 3 el depto D

        if select_piso < 0 or select_piso >= 10 or select_depto < 0 or select_depto >= 4:
            print("Las coordenadas ingresadas no son válidas o no existen. \nPor favor, intente nuevamente.")
            continue
        if edificio[select_piso][select_depto] == ' ':
            break
        else:
            print("El lote seleccionado no está disponible. \nPor favor, escoja y seleccione otro.")

      except ValueError:
        print("El valor ingresado no es válido. \nPor favor, intente nuevamente.")
        continue

    #DATOS_CLIENTE
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    rut = input("Ingrese su rut (sin dv): ")
    dpt_seleccionado = detalle_deptos[select_depto]
    depto_seleccionado.append({
        'Departamento': dpt_seleccionado['Departamento'],
        'Tipo': dpt_seleccionado['Tipo'],
        'Precio UF': dpt_seleccionado['Precio UF'],
        'Cliente': {
            'RUT': rut,
            'Nombre': nombre,
            'Apellido': apellido,
        }
    })

    edificio[select_piso][select_depto] = 'X'
    print("_______________________________________________")
    print("El lote seleccionado ha sido ocupado con éxito.")

def mostrar_compradores():
    if len(depto_seleccionado) > 0:
        print("\nCOMPRADORES:")
        for depto in depto_seleccionado:
          cliente = depto['Cliente']
          print("\tRUT:", cliente['RUT'])
          print("\tNombre:", cliente['Nombre'])
          print("\tApellido:", cliente['Apellido'])
          print("\tDepartamento:", depto['Departamento'])
          print("\tTipo:", depto['Tipo'])
          print("\tPrecio UF:", depto['Precio UF'])
          print()
    else:
        print("No hay números de RUT de compradores registrados por el momento.")

def ganancias_totales():
  if len(depto_seleccionado) > 0:
      acum_precio = 0
      cont_depto = 0
      print("\nGANANCIAS TOTALES:")
      for depto in depto_seleccionado:
        print("\tTipo:", depto['Tipo'])
        print("\tPrecio UF:", depto['Precio UF'])
        acum_precio = acum_precio + depto['Precio UF']
        cont_depto = cont_depto + 1
      print("\tTotal departamentos comprados: ",cont_depto)
      print("\tTotal acumulado: ",acum_precio)
  else:
      print("No hay ganancias totales por el momento.")

def salida():
  print("\n¿Desea salir de la aplicación?")
  print("1. SI")
  print("2. NO")
  opcion_2 = int(input("\nIngrese una opción: "))

  if opcion_2 == 1:
    if len(depto_seleccionado) > 0:
      print("\nHas salido de la aplicación.")
      for depto in depto_seleccionado:
        cliente = depto['Cliente']
        print("\tComprador(a):", cliente['Nombre'], cliente['Apellido'])
        print("\tFecha actual: ", now.date())
        hora_actual = datetime.now()
        hora_formateada = hora_actual.strftime('%H:%M')
        print("\tHora actual: ", hora_formateada)
        print("\n¡Hasta luego!")
  elif opcion_2 == 2:
    menu_principal()
  else:
    print("\nLa opción ingresada no es válida. \nPor favor, intente nuevamente.")

def menu_principal():
    while True:
      print("\n---MENU PRINCIPAL---")
      print("1. Comprar departamento")
      print("2. Mostrar departamentos disponibles")
      print("3. Ver listado de compradores")
      print("4. Mostrar ganancias totales")
      print("5. Salir")
      try:
        opcion = int(input("\nIngrese una opción: "))
      except ValueError:
        print("\nLa opción ingresada no es válida. \nPor favor, intente nuevamente.")
        continue

      if opcion == 1:
        seleccion_depto()
      elif opcion == 2:
        ver_deptos()
      elif opcion == 3:
        mostrar_compradores()
      elif opcion == 4:
        ganancias_totales()
      elif opcion == 5:
        salida()
        break
      else:
        print("\nLa opción ingresada no es válida. \nPor favor, intente nuevamente.")

menu_principal()