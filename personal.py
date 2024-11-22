from ConexionBD import *


class CPersonal:
    def Ingresar_personal(nom_usu,apell_usu,cargo_usu,sexo_usu):
        try:
            connect = CConexion.Conexion_BDD()
            cursor = connect.cursor()
            sql = "insert into usuario values(null,%s,%s,%s,%s);"
            valores = (nom_usu,apell_usu,cargo_usu,sexo_usu)
            cursor.execute(sql,valores)
            connect.commit()
            print(cursor.rowcount,"Registro ingresado")
            connect.close
        except mysql.connector.Error as error:
            print("Error al ingresar datos{}".format(error))

    def Modificar_personal():
        try:
            connect = CConexion.Conexion_BDD()
            cursor = connect.cursor()
            cursor.execute("select * from usuario;")
            mi_result = cursor.fetchall()
            connect.commit()
            connect.close()
            return mi_result
        except ValueError as error:
            print("Error al mostrar datos{}".format(error))

    def Eliminar_personal(id_usu):
        try:
            connect = CConexion.Conexion_BDD()
            cursor = connect.cursor()
            sql =("Delete from usuario where usuario.id_usu = %s;")
            valores = (id_usu,)
            cursor.execute(sql,valores)
            connect.commit()
            print(cursor.rowcount,"Registro eliminado")
            connect.close

        except ValueError as error:
            print("Error al eliminar registro{}",format(error))

    def Modif_personal(id_usu,nom_usu,apell_usu,cargo_usu,sexo_usu):
        try:
            connect = CConexion.Conexion_BDD()
            cursor = connect.cursor()
            sql = ("update usuario set usuario.nom_usu = %s, usuario.apell_usu = %s,  usuario.cargo_usu = %s, usuario.sexo_usu = %s where usuario.id_usu = %s;")
            valores = (nom_usu,apell_usu,cargo_usu,sexo_usu,id_usu)
            cursor.execute(sql,valores)
            connect.commit()
            print(cursor.rowcount,"Registro actualizado")
            connect.close
        except ValueError as error:
            print("Error al eliminar registro{}".format(error))
