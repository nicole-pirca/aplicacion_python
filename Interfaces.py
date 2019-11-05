from tkinter import*
raiz= Tk()
raiz.title("Ventana de prueba")
raiz.resizable(0,0)#parametros de tipo boleanancho y alto
raiz.iconbitmap("icono.ico")
raiz.mainloop()


import pysysql
class DataBase:
    def _init_(self):
        self.connection= pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="mysql")
        )
        self.cursor=self.connection.cursor()
database=DataBase()

#conexion a base de datos 
import pymysql
coon=pymysql.connect(
	host="localhost",
    user="root",
    password="",
    db="mysql")
cursor.execute("SELECT VERSION()")
		
for row in cursor:
	print(row)
cursor.close()
conn.close()
	
#botones
import sys
from PyQt5 import QtWidgets

def window():
	app=QtWidgets.QApplication(sys.argv)
	ventana=QtWidgets.QtWidget()
	boton= QtWidgets.QPushButton(ventana)
	texto=QtWidgets.QLabel(ventana)
	boton.setText(Presionar)
	ventana.show()
	sys.exit(app.exec_())
window()
#crear una pagina web


Nr	User	UserName	Data	Text	Hashtags	Words	Medias	Media Urls	ReTweet	public












