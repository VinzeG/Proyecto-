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
