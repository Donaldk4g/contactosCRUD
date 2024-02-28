import modulo
import click
from tabulate import tabulate
ruta='data.csv'


@click.group()
def cli():
    pass

@cli.command()
def crear_usuario():
    file=modulo.read_csv(ruta)
    data_cliente=modulo.cliente(file)
    print(data_cliente)
    confirmacion=click.confirm('Deseas guardar los datos?')
    if confirmacion:
        modulo.guardar_csv(ruta,'O',data_cliente,[])
        click.echo('El registro se guardo con exito')
    else:
        click.echo('Operacion cancelada')



@cli.command()
def print_usuario():
     file=modulo.read_csv(ruta)
     print(tabulate(file,headers="firstrow"))
     

@cli.command()     
def cliente_eliminar():
    
    file=modulo.read_csv('data.csv')
    idCliente=modulo.pedirDato('N','ingresa el ID del usuario: ',1)
    eliminar,datos=modulo.eliminar_linea_csv(ruta,idCliente)
    if eliminar:
        confirmacion=click.confirm('Deseas guardar los datos?')
        if confirmacion:
             modulo.guardar_csv(ruta,'n',datos2=datos)
             click.echo('El registro se ha eliminado con exito')
        else:
             click.echo('Operacion cancalada')
    else:
         click.echo('El registro no se encuentra en la base de datos')


@cli.command()
def updateCliente():
    dato=None
    idCliente=modulo.pedirDato('N','ingresa el ID del usuario: ',1)
    idmodif=modulo.pedirDato('N','ingrese [1] para modificar el Nombre del cliente\ningrese [2] para modificar el Telefono del cliente\ningrese [3] para modificar el correo del cliente:\n',1)
    if idmodif=='1':
         dato=modulo.pedirDato('L','ingrese el nuevo Nombre del cliente: ',3)
    elif idmodif=='2':
         dato=modulo.pedirDato('N','ingrese el nuevo Telefono del cliente: ',10)
    elif idmodif=='2':
         dato=modulo.pedirDato('C','ingrese el nuevo Correo del cliente: ')

    actualizar, datos=modulo.actualizardato(ruta,idCliente,idmodif,dato)

    if actualizar:
         confirmacion=click.confirm('Deseas actualizar los datos?')
         if confirmacion:
              modulo.guardar_csv(ruta,'n',datos2=datos)
              click.echo('El registro se ha actualizado con exito')
         else:
             click.echo('Operacion cancalada')

    else:
         click.echo('El registro no se encuentra en la base de datos')


    
    
  
         





            
   
        




if __name__=='__main__':
    cli()

