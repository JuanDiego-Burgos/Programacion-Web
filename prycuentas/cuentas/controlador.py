from cuentas.dao import daoPlan


class ctrPlan:
    def __init__(self, grup=None):
        self.grupo = grup

    def consulta(self):
        objDao = daoPlan()
        return objDao.consultar()

    def ingresar(self, plan):
        objDao = daoPlan()
        return objDao.ingresar(plan)

    def modificar(self, plan, id):
        objDao = daoPlan()
        return objDao.modificar(plan, id)

    def eliminar(self, id):
        objDao = daoPlan()
        return objDao.eliminar(id)