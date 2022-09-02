import mysql.connector

class Conectar_bd:
    def __init__(self, host = "localhost", user = "root", password = "", database = "hotel"):
        self._host = host
        self._user = user
        self._password = password
        self._database = database 


    def conectar(self):
        self.con = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "hotel")


        self.cu = self.con.cursor()


    def desconectar(self):
        self.con.close()


    def comando_dql(self, sql):
        self.conectar()
        self.cu.execute(sql)
        self.resultado = self.cu.fetchall()
        self.desconectar()

