import sqlite3

baseDatos = "negocio"

miConexion = sqlite3.connect(baseDatos)

# insertar categorias

def insertarCategoria():
    try:
        nombre="Electrodomestico"
        cursor = miConexion.cursor()
        categoria = (nombre,)
        consulta = "insert into categoria values(null,?)"
        cursor.execute(consulta, categoria)
        miConexion.commit()
        if(cursor.rowcount==1):
            print(f"Categoria insertada con id {cursor.lastrowid}")
    except miConexion.Error as error:
        miConexion.rollback()
        print(str(error)) 

def listar():
    try:
        # crear el cursor
        cursor = miConexion.cursor()#cursor tiene 3 métodos
        #texto de la consulta
        consulta = "select *from categoria"
        cursor.execute(consulta)
        categoria = cursor.fetchall()
        if(len(categoria)>0):
            #imprimir
            for c in categoria: #p es una tupla
                print(c)
        else:
            print("En el momento no hay categorias registradas")
    except miConexion.Error as error:
        print(str(error))
        
def insertarProducto():
    try:
        cursor = miConexion.cursor()
        producto = (10, "Botas", 325000, 3)
        codigo = int(input("Ingrese el código del producto: "))
        nombre = input("Nombre del Producto: ")
        precio=int(input("Precio del Producto: "))
        categoria= listar()
        categoria = int(input("seleccione categoria ingresando un número de categoria: "))
        producto=(codigo,nombre,precio, categoria)
        consulta = "insert into Productos values(null,?,?,?,?)"
        cursor.execute(consulta, producto)
        miConexion.commit()
        if(cursor.rowcount==1):
            print(f"Producto insertado con id {cursor.lastrowid} ")
    except miConexion.Error as error:
        miConexion.rollback()
        print(str(error))
        
def listarProductos():
    try:
        cursor=miConexion.cursor()
        consulta= "select p.proCodigo,p.proNombre, p.proPrecio, p.catNombre from productos p inner join categoria c on p.proCategoria = c.idCategoria"
        cursor.execute(consulta)
        producto = cursor.fetchall()
        for p in producto:
            print(p)
    except miConexion.Error as error:
        print(str(error))
        
        
def consultarPorCategoria():
    try:
        

# insertarCategoria()
# listar()
# insertarProducto()
# listarProductos()

# TAREA --------> actualizar y eliminar un producto