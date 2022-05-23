logs = ""
# rutas de los archivos
paths = ['logs/log','logs/log2']
# abre los dos archivos y crea un solo string 
for path in paths:
    with open(path) as f:
        logs+= f.read()
# separa los datos
datosSplitted = [datoLog.split(";") for datoLog in logs.splitlines()]
# ordena los datos
datosSplitted = sorted(datosSplitted,key=lambda x:x[2])
# guarda los datos
with open("out/out.txt","w") as f:
    # reconstruye el formato inicial del log
    datosFormateados = [";".join(dato) for dato in datosSplitted]
    # escribe los datos en un archivo
    f.write("\n".join(dato for dato in datosFormateados))