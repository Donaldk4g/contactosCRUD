import os
import csv
ID='ID'
NOMBRE='NOMBRE'
TELEFONO='TELEFONO'
CORREO='CORREO'
HEAD=[ID,NOMBRE,TELEFONO,CORREO]


def read_csv(ruta):
     dato=[]
     z=[]
     if not os.path.isfile(ruta):
         z.append(HEAD)
         with open(ruta, 'w') as csvfile:
             escritor=csv.writer(csvfile,delimiter=';')
             escritor.writerows(z)

         
    
     with open(ruta, 'r+') as csvfile:
         reader = csv.reader(csvfile, delimiter=';')
        # if  os.stat(ruta).st_size != 0:
            #next(reader)
         dato=[i for i in reader]
         return dato
        
                 
def guardar_csv(path, tipo='O',datos=dict,datos2=[]):
     if tipo=='O':
      if  os.stat(path).st_size == 0:
         with open(path, 'a',newline='') as csvfile:
               escritor_csv = csv.writer(csvfile, delimiter=';')
               escritor_csv.writerow(datos.keys())
               escritor_csv.writerow(datos.values())
      else:
            with open(path, 'a',newline='') as csvfile:
               escritor_csv = csv.writer(csvfile, delimiter=';')
               escritor_csv.writerow(datos.values())
     else:
           with open(path, 'w', newline='') as archivo:
                escritor_csv = csv.writer(archivo, delimiter=';')
                escritor_csv.writerows(datos2)


def pedirDato(tipo,mensaje,zize=10):
   
    
     while True:
        entrada=input(mensaje)
        if entrada and entrada.isdigit() and len(entrada)>=zize and tipo=='N':
           break

        elif entrada and entrada.isalpha() and len(entrada)>=zize and tipo=='L':
           break

        elif entrada and entrada.count("@") == 1 and tipo=='C' and len(entrada)<=253:
           username_part, domain_part = entrada.rsplit("@", 1)
           if len(username_part) < 64 or len(domain_part) < 253:
              break 
     return entrada
         

def cliente(datos):
 if len(datos)==1:
    dato={
    ID:len(datos),
    NOMBRE: pedirDato('L','Ingrese Nombre del Cliente: ',3),
    TELEFONO: pedirDato('N','Ingrese Telefono del Cliente: ',10),
    CORREO: pedirDato('C','Ingrese Correo del Cliente: ')
      }
 else:
    x=datos[-1][0]
    x=int(x)+1
    dato={
    ID:x,
    NOMBRE: pedirDato('L','Ingrese Nombre del Cliente: ',3),
    TELEFONO: pedirDato('N','Ingrese Telefono del Cliente: ',10),
    CORREO: pedirDato('C','Ingrese Correo del Cliente: ')
    }
 return dato


def eliminar_linea_csv(ruta, linea):
   datos=[]
   m=False
   with open(ruta, 'r') as csvfile:
       reader = csv.reader(csvfile, delimiter=';')
       for y in reader:
          if y[0]==linea:
                m=True
                continue
          datos.append(y)
   return m,datos


def actualizardato(ruta, idcliente,idmodif,mensaje):
   M=False
   z=int(idmodif)
   datos=read_csv(ruta)
   for index,dato in enumerate(datos):
       if dato[0]==idcliente:
           datos[index].insert(z,mensaje)
           M=True
           break
   return M, datos


       
   
