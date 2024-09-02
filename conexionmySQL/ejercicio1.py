import pymysql as mysql

user = "root"
password = "CTPI2024*"
baseDatos = "club"
host = "localhost"

miConexion = mysql.connect(host=host, user=user, db=baseDatos, password=password)
 
def insertar():
    try:
        # creando un producto en una tupla
        socio = ("Mariana Castañeda Salazar", 25000, "Asociado")
        cursor = miConexion.cursor()
        # texto de la consulta
        consulta = "insert into socios values(null, %s,%s,%s)"
        # ejecutar la consulta
        resultado = cursor.execute(consulta, socio)
        miConexion.commit()
        if(cursor.rowcount==1): #Numero de filas actualizadas
            print("Socio agregado")
        
        
    except miConexion.Error as error:
        print(str(error))
        
# insertar()

def listar():
    try:
        # crear el cursor
        cursor = miConexion.cursor()#cursor tiene 3 métodos
        #texto de la consulta
        consulta = "select *from socios"
        cursor.execute(consulta)
        socios = cursor.fetchall()
        print(socios)
        if(len(socios)>0):
            #imprimir
            for p in socios: #p es una tupla
                print(p)
                print(f"Nombre: {p[1]}")
                print(f"Mensualidad: {p[2]}")
                print(f"Categoria: {p[3]}")
        else:
            print("En el momento no hay socios agregados")
    except miConexion.Error as error:
        print(str(error))
        
        
def consultarPorCategoria():
    try:
        cursor = miConexion.cursor()
        categoria = str(input("Ingresa la categoria del socio a consultar: "))
        socioConsultar = (categoria)
        consulta = "select * from socios where categoria = %s"    
        cursor.execute(consulta, socioConsultar)
        socio = cursor.fetchone()
        if(socio):
            print(socio)
        else:
            print("No existe socio con esa categoría en el club")  
    except miConexion.Error as error:
        print(str(error))
              
    return socio

def actualizar():
    try:
       socio = consultarPorCategoria()
       cursor = miConexion.cursor()
       nuevoCosto = socio[2]*1.20
       socioActualizar = socio[3]
       datosActualizar = (nuevoCosto, socioActualizar )
       consulta = "update socios set mensualidad=%s where categoria=%s"
       resultado = cursor.execute(consulta, datosActualizar)
       miConexion.commit()
       if(cursor.rowcount==1):
           print("Socio actualizado")
       else:
           print("Error al actualizar los datos del socio")
       
    except miConexion.Error as error:
        print(str(error)) 

def eliminar():
    try:
        cursor = miConexion.cursor()
        categoria = str(input("Ingresa la categoria a eliminar: "))
        socioEliminar = (categoria)
        consulta = "delete from socios where categoria=%s"
        cursor.execute(consulta, socioEliminar)
        miConexion.commit()
        if(cursor.rowcount==1):
            print("Socio eliminado")
        else:
            print("No existe socio con esa categoria")
        cursor.close()
        
    except miConexion.Error as error:
        print(str(error)) 
# insertar()
# listar()
# consultarPorCategoria()
actualizar()
# eliminar()
