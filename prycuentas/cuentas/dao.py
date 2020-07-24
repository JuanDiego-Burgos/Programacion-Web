from conexion import Conector


class daoPlan(Conector):
    def __init__(self, server='localhost', usuario='root', password='', basedato='crud'):
        Conector.__init__(self, server='localhost', usuario='root', password='', basedato='crud')

    def consultar(self):
        result = True
        try:
            sql = "Select p.idplancuenta, p.codigo, g.descripcion, p.descripcion, case p.naturaleza when 'A' then 'Acreedor' when 'D' then 'Deudor' END AS naturalezap, case p.estado when 0 then 'False' when 1 then 'True' END AS estadop from plancuenta p, grupo g where p.grupoid = g.idgrupo"
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as ex:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self, plan):
        result = True
        try:
            sql = "insert into plancuenta(codigo,grupoid,descripcion,naturaleza,estado)VALUES (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql, (plan.codigo, plan.grupoid, plan.descripcion, plan.naturaleza, plan.estado))
            self.conn.commit()
        except:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def modificar(self, plan, id):
        correcto = True
        try:
            sql = "update plancuenta set codigo = %s , grupoid = %s, descripcion = %s, naturaleza = %s, estado = %s where idplancuenta = %s"
            self.conectar()
            self.conector.execute(sql, (plan.codigo,plan.grupoid,plan.descripcion,plan.naturaleza,plan.estado, id))
            self.conn.commit()
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminar(self, id):
        correcto = True
        try:
            sql = "Delete from plancuenta where idplancuenta = %s"
            self.conectar()
            self.conector.execute(sql, (id))
            self.conn.commit()
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
