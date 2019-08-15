import pandas as pd
datos=pd.read_csv('puntajes.csv',header=0)
#print(datos)
print(datos[datos.iloc[:,1]<30])

juego = ""
demora = ""
contenido = "El juego "+juego+" demoro "+demora+" minutos"
nueva_ruta = "C:/Users/sr281/OneDrive/Escritorio/nuevospuntajes.txt"
archivo = open(nueva_ruta, 'w')
archivo.write(contenido)


