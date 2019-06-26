import os
from datetime import datetime

lista_links = []
# lista se va a popular con links de youtube

input_nombre_carpeta = input("nombre de la carpeta, vacio para que tenga el nombre de la fecha de hoy: ")

if len(input_nombre_carpeta) > 0:
    nombre_carpeta = input_nombre_carpeta
else:
    nombre_carpeta = datetime.today().strftime("%d-%M-%Y")

path_actual = os.path.dirname(os.path.abspath(__file__))
path_completo = path_actual + "/" + nombre_carpeta + "/" + "'%(uploader)s-%(title)s'"
os.system("mkdir %s" % nombre_carpeta)

def bajarse_audios(lista_links, nombre_carpeta):
    for link in lista_links:
        # Crear carpeta
        os.system("mkdir " + nombre_carpeta)
	
        comando_basico = "youtube-dl -f 140 --no-overwrites -o " + '"' + path_completo + '" '
        comando_completo = comando_basico + ' "' + link + '"'
        print(comando_completo)
        os.system(comando_completo)


def recibir_input(nombre_carpeta):
    texto_input = input("Pegar un link de youtube o H para continuar: ")
    if texto_input == "H":
        bajarse_audios(lista_links, nombre_carpeta)
    else:
        lista_links.append(texto_input)
        recibir_input(nombre_carpeta)

recibir_input(nombre_carpeta)
