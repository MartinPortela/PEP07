from os import strerror
import csv

cabeceras=["Ciudad","País","Continente"]
data=["París","Francia","Europa"],["Canberra","Australia","Oceanía"],["Nairobi","Kenia","África"],["Ottawa","Canadá","América"]
try:
    with open("capitales.csv","w") as fichero_csv:
        writer = csv.writer(fichero_csv)
        writer.writerow(cabeceras)
        writer.writerows(data)
    print("Archivo 'capitales.csv' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)