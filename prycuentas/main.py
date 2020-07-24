from grupo.controlador import ctrGrupo
from grupo.modelo import modGrupo
from cuentas.controlador import ctrPlan
from cuentas.modelo import modPlan

ctrg = ctrGrupo()
ctrp = ctrPlan()

opc = 0
try:
    while opc != 4:
        print("******************MENU PRINCIPAL*****************")
        opc = int(input('1) Grupo de Cuentas' + '\n2) Plan de Cuentas' + '\n3) Salir' + '\n¿Opcion?: '))

        if opc == 1:
            print("******************MODULO GRUPOS*****************")
            opcG = 0
            while opcG != 6:
                opcG = int(input(
                    '1) Listar Grupos' + '\n2) Nuevo Grupo' + '\n3) Editar Grupo' + '\n4) Eliminar  Grupos' + '\n5) Regresar' + '\n¿Opcion?: '))

                if opcG == 1:
                    print("\n---------------LISTADO GRUPOS---------------\n")
                    grupolist = ctrg.consulta()
                    print("Id - Descripción")
                    for r in grupolist:
                        print("{} - {}".format(r[0], r[1]))
                    print("\n-----------------------------------------")

                elif opcG == 2:
                    for i in range(1):
                        descripcion = input('Ingrese una descripción: ')
                        grupoAdd = modGrupo(descripcion.upper())
                        if ctrg.ingresar(grupoAdd):
                            print("Registro grabado correctamente\n")
                        else:
                            print("Error")

                elif opcG == 3:
                    print("\n---------------LISTADO GRUPOS---------------\n")
                    grupolist = ctrg.consulta()
                    print("Id - Descripción")
                    for r in grupolist:
                        print("{} - {}".format(r[0], r[1]))
                    print("\n-----------------------------------------")
                    for i in range(1):
                        id = int(input('Ingrese codigo id de grupo a editar: '))
                        descripcion = input('Ingrese una nueva descripción: ')
                        grupoEdit = modGrupo(descripcion)
                        if ctrg.modificar(grupoEdit, id):
                            print("Registro grabado correctamente\n")
                        else:
                            print("Error")

                elif opcG == 4:
                    print("\n---------------LISTADO GRUPOS---------------\n")
                    grupolist = ctrg.consulta()
                    print("Id - Descripción")
                    for r in grupolist:
                        print("{} - {}".format(r[0], r[1]))
                    print("\n-----------------------------------------")
                    for i in range(1):
                        id = int(input('Ingrese codigo id de grupo a eliminar: '))
                        if ctrg.eliminar(id):
                            print("Registro eliminado correctamente\n")
                        else:
                            print("Error")

                elif opcG == 5:
                    opcG = 6
                    opc = 0
                    pass

                else:
                    print('Esta opcion no existe')
                    print("\n")
                    opcG = 0

        elif opc == 2:
            print("******************MODULO PLAN DE CUENTAS*****************")
            opcP = 0
            while opcP != 6:
                opcP = int(input(
                    '1) Listar Plan' + '\n2) Nuevo Plan' + '\n3) Editar Plan' + '\n4) Eliminar  Plan' + '\n5) Regresar' + '\n¿Opcion?: '))

                if opcP == 1:
                    print("\n---------------LISTADO PLAN DE CUENTAS---------------\n")
                    lista = ctrp.consulta()
                    print("Id - Codigo - Grupo - Descripcion - Naturaleza - Estado")
                    for r in lista:
                        print("{} - {} - {} - {} - {} - {}".format(r[0], r[1], r[2], r[3], r[4], r[5]))
                    print("\n-----------------------------------------")

                elif opcP == 2:
                    for i in range(1):
                        codigo = input('Ingrese una codigo: ')
                        print("\n---------------LISTADO GRUPOS---------------\n")
                        grupolist = ctrg.consulta()
                        print("Id - Descripción")
                        for r in grupolist:
                            print("{} - {}".format(r[0], r[1]))
                        print("\n-----------------------------------------")
                        grupoid = int(input('Ingrese la id del grupo: '))
                        descripcion = input('Ingrese una descripción: ')
                        print('D = Deudora \nA = Acredora')
                        nat = 0
                        naturaleza = input('Ingrese una naturaleza: ')
                        while nat != 1:
                            if naturaleza == 'A' or naturaleza == 'a':
                                nat = 1
                            elif naturaleza == 'B' or naturaleza == 'b':
                                nat = 1
                            else:
                                print('Opcion no valida')
                                print('D = Deudora \nA = Acredora')
                                naturaleza = input('Ingrese una naturaleza: ')

                        print('0 = False \n1 = True')
                        est = 0
                        estado = int(input('Ingrese un estado: '))
                        while est != 1:
                            if estado == 0:
                                est = 1
                            elif estado == 1:
                                est = 1
                            else:
                                print('Opcion no valida')
                                print('0 = False \n1 = True')
                                estado = int(input('Ingrese un estado: '))

                        add = modPlan(codigo, grupoid, descripcion.upper(), naturaleza.upper(), estado)
                        if ctrp.ingresar(add):
                            print("Registro grabado correctamente\n")
                        else:
                            print("Error")

                elif opcP == 3:
                    print("\n---------------LISTADO PLAN DE CUENTAS---------------\n")
                    lista = ctrp.consulta()
                    print("Id - Codigo - Grupo - Descripcion - Naturaleza - Estado")
                    for r in lista:
                        print("{} - {} - {} - {} - {} - {}".format(r[0], r[1], r[2], r[3], r[4], r[5]))
                    print("\n-----------------------------------------")

                    for i in range(1):
                        id = int(input('Ingrese codigo id de grupo a editar: '))
                        codigo = input('Ingrese una codigo: ')
                        print("\n---------------LISTADO GRUPOS---------------\n")
                        grupolist = ctrg.consulta()
                        print("Id - Descripción")
                        for r in grupolist:
                            print("{} - {}".format(r[0], r[1]))
                        print("\n-----------------------------------------")
                        grupoid = int(input('Ingrese la id del grupo: '))
                        descripcion = input('Ingrese una descripción: ')
                        print('D = Deudora \nA = Acredora')
                        naturaleza = input('Ingrese una naturaleza: ')
                        nat = 0
                        while nat != 1:
                            if naturaleza == 'A' or naturaleza == 'a':
                                nat = 1
                            elif naturaleza == 'B' or naturaleza == 'b':
                                nat = 1
                            else:
                                print('Opcion no valida')
                                print('D = Deudora \nA = Acredora')
                                naturaleza = input('Ingrese una naturaleza: ')
                        print('0 = False \n1 = True')
                        estado = int(input('Ingrese un estado: '))
                        est = 0
                        while est != 1:
                            if estado == 0:
                                est = 1
                            elif estado == 1:
                                est = 1
                            else:
                                print('Opcion no valida')
                                print('0 = False \n1 = True')
                                estado = int(input('Ingrese un estado: '))
                        edit = modPlan(codigo, grupoid, descripcion.upper(), naturaleza.upper(), estado)
                        if ctrp.modificar(edit, id):
                            print("Registro grabado correctamente\n")
                        else:
                            print("Error")

                elif opcP == 4:
                    print("\n---------------LISTADO PLAN DE CUENTAS---------------\n")
                    lista = ctrp.consulta()
                    print("Id - Codigo - Grupo - Descripcion - Naturaleza - Estado")
                    for r in lista:
                        print("{} - {} - {} - {} - {} - {}".format(r[0], r[1], r[2], r[3], r[4], r[5]))
                    print("\n-----------------------------------------")

                    for i in range(1):
                        id = int(input('Ingrese codigo id de plan a eliminar: '))
                        if ctrp.eliminar(id):
                            print("Registro eliminado correctamente\n")
                        else:
                            print("Error")

                elif opcP == 5:
                    opcP = 6
                    opc = 0
                    pass

                else:
                    print('Esta opcion no existe')
                    print("\n")
                    opcP = 0

        elif opc == 3:
            print('ADIOS')
            break

        else:
            print('Esta opcion no existe')
            print("\n")
            opc = 0

except Exception as ex:
    print(ex)
