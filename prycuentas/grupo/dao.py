from conexion import Conector


class daoGrupo(Conector):
    def __init__(self, server='localhost', usuario='root', password='', basedato='crud'):
        Conector.__init__(self, server='localhost', usuario='root', password='', basedato='crud')

    def consultar(self):
        result = True
        try:
            sql = 'Select * from grupo'
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

    def ingresar(self, gru):
        result = True
        try:
            sql = "insert into grupo(descripcion)VALUES (%s)"
            self.conectar()
            self.conector.execute(sql, (gru.descripcion))
            self.conn.commit()
        except:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def modificar(self, grupo, id):
        result = True
        try:
            sql = "update grupo set descripcion = %s where idgrupo = %s"
            self.conectar()
            self.conector.execute(sql, (grupo.descripcion, id))
            self.conn.commit()
        except:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def eliminar(self, id):
        result = True
        try:
            sql = "Delete from grupo where idgrupo = %s"
            self.conectar()
            self.conector.execute(sql, (id))
            self.conn.commit()
        except:
            result = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
