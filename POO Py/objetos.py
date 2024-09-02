# from perro import Perro

# perro1 = Perro("Tayson", "Pitbull Stanford")
# perro2 = Perro("Apolo", "Lobo Siberiano")

# perro1.caminar(10)
# perro2.ladrar()

# perro2.nombre = "Zeus"
# perro2.ladrar()
# perro2.caminar(20)

# ---------------------------------------------------------------------------------------------

# from persona import Persona #Para traer muchas clas se utiliza * despues del import
# from aprendiz import Aprendiz
# from instructor import Instructor

# people = Persona(11, "Pedro", "peter@yahoo.com")
# print(people.getIdentificacion())
# print(people.getNombre())
# print(people.getCorreo())

# people.setIdentificacion(111)
# print(people.getIdentificacion())

# people2 = Persona()
# print(people.getNombre())

# people3 = Persona(nombre="Rosa", correo="rosita@hotmail.com", identificacion="3232")
# people4 = Persona("13", "Maria", "maria@gmail.com")

# aprendiz = Aprendiz(320, "99", "Marco Pinto", "marco@yahoo.com")
# aprendiz.setIdentificacion("100")
# print(aprendiz.getIdentificacion())

# aprendiz.setPuntajeIcfes(380)
# print(aprendiz.getPuntajeIcfes())

# aprendiz.saludar()

# ---------------------------------------------------------------------------------------------

# from alumnos import Alumno
# from curso import Curso

# unCurso = Curso("Desarrollo web en Python")

# alumno1 = Alumno("Maria", 18)
# alumno2 = Alumno("Pedro", 21)
# alumno3 = Alumno("Erick", 25)

# unCurso.matricularAlumno(alumno1)
# unCurso.matricularAlumno(alumno2)
# unCurso.matricularAlumno(alumno3)

# print(f"Curso: {unCurso.getNombre()}")
# print("Relación de alumnos matriculados")

# alumnos = unCurso.getAlumnos()

# alumnos = unCurso.getAlumnos()
# for a in alumnos:
#     print(a.getNombre())
#     print(a.getEdad())

# ----------------------------------------------------------------------------------------------



# from empleado import Empleado
# from empresa import Empresa

# elSena = Empresa("SENA")

# elSena.agregarEmpleado("Martin Rojas", "Director Regional", 75000)
# elSena.agregarEmpleado("pablo Ortiz", "Instructor", 60000)
# elSena.agregarEmpleado("Monika Galindo", "Tesorero", 65000)

# print(f"Lista de Empleados de la empresa {elSena}")

# for empleado  in elSena.getEmpleados():
#     print(empleado)
    
# -------------------------------------------------------------------------------------------

from animales import Animal, Perro, Gato, Pez

def animal():
    pez = Pez(4)
    perro =Perro(5)
    gato = Gato(10)
    
    Pez.nadar()
    Perro.ladrar()
    Gato.maullar()
    
    Pez.respirar()
    Perro.respirar()
    Gato.respirar()
    
    if __name__ == "__animal__":
        print("sapo")
animal()


