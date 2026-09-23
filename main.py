#Importar sqlite
import sqlite3

#Crear la conexión. Si existe se conecta, sino crea el archivo
conexion = sqlite3.connect("biblioteca.db")

#Crear el cursor
cursor = conexion.cursor()

print("Conexión creada!")

#Creacion de TABLA 
cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)")
conexion.commit()

listaEstudiantes = [("Jose","Sanchez"),("Roberto","Martinez")]

#Agregar algo -> CREATE
#cursor.execute("INSERT INTO estudiantes (nombre, apellido) VALUES (?, ?)",("Pepe","Perez"))
#conexion.commit()

#Agregar varios registros de una 
#cursor.executemany("INSERT INTO estudiantes (nombre, apellido) VALUES (?,?)", listaEstudiantes)
#conexion.commit()

print("Agregando algo a la DB")

#Actualizar
def actualizarEstudiante(id: int, nombre: str , apellido: str) -> None:
    cursor.execute("UPDATE estudiantes SET nombre = ?, apellido = ? WHERE id = ?",(nombre, apellido, id))
    conexion.commit()
    print("Estudiante actualizado")

def agregarEstudiante(nombre: str, apellido: str) -> None:
    print("aca",nombre.strip(), nombre.strip() == "")
    if nombre.strip() != "" and apellido.strip() != "":
        cursor.execute("INSERT INTO estudiantes (nombre, apellido) VALUES (?,?)",(nombre, apellido))
        conexion.commit()
    else:
        print("No acepto espacios vacios")
def leerEstudiantes() -> None:
    #Leer -> READ (lectura de datos de la db)
    resultado = cursor.execute("SELECT * FROM estudiantes").fetchall()
    for item in resultado:
        print(item)

def borrarEstudiante(id: int) -> None:
    cursor.execute("DELETE from estudiantes WHERE id = ?", (id,))
    conexion.commit()
    print("Estudiante eliminado")

leerEstudiantes()
print("Agrega datos")
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
agregarEstudiante(nombre, apellido)

#actualizarEstudiante(1, "Kevin","Olivieri")
#borrarEstudiante(2)
leerEstudiantes()
conexion.close()
