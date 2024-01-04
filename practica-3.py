
class Curso:
    def __init__(self, nombre_curso, docente):
        self.nombre_curso = nombre_curso
        self.docente = docente
        self.estudiantes = []

    def mostrar_informacion_curso(self):
        print(f"Nombre del curso: {self.nombre_curso}")
        print(F"Nombre del docente que imparte el curso {self.docente.nombre}")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado al curso {self.nombre_curso}")

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)
            print(f"Estudiante {estudiante.nombre} eliminado del curso {self.nombre_curso}")
        else:
            print(f"Estudiante {estudiante.nombre} no encontrado en el curso {self.nombre_curso}")

class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self. especialidad = especialidad


class Estudiante:
    def __init__(self, nombre, edad, escuela):
        self.nombre = nombre
        self.edad = edad
        self.escuela = escuela
        self.cursos = []

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Escuela profesional: {self.escuela}")
        print(f"Estudiante matriculado en los siguientes cursos:")
        for curso in self.cursos:
            curso.mostrar_informacion_curso()

    def cumpleanios(self):
        self.edad += 1

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
    def matricular_curso(self, curso):
        self.cursos.append(curso)
        print(f"Estudiante {self.nombre} matriculado en el curso {curso.nombre_curso}")

    def desmatricular_curso(self, curso):
        if curso in self.cursos:
            self.cursos.remove(curso)
            print(f"Estudiante {self.nombre} desmatriculado del curso {curso.nombre_curso}")
        else:
            print(f"Estudiante {self.nombre} no está matriculado en el curso {curso.nombre_curso}")

class Universidad:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado a la universidad")

    def imprimir_numero_estudiantes(self):
        print(f"La cantidad de estudiantes es de {len(self.estudiantes)}")

    def mostrar_informacion_todos_los_estudiantes(self):
        for estudiante in self.estudiantes:
            estudiante.mostrar_informacion()
            print('')

class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    
    def mostrar_informacion(self):
        print(f"Nombre del libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")
        

# Creando docentes
docente1 = Profesor("Guido van Rossum", "Lenguajes de Programación")
docente2 = Profesor("Linus Torvalds", "Sistemas Operativos")
docente3 = Profesor("Gennady Korotkevich", "Programación Competitiva")

# Creando cursos
poo2 = Curso("Programación Orientada a Objetos 2", docente1)
sistemas_operativos = Curso("Sistemas Operativos", docente2)
estructuras_datos = Curso("Estructuras de Datos", docente3)

# Crear instancias de la clase Estudiante
estudiante1 = Estudiante("Juan", 20, "Ingeniería")
estudiante2 = Estudiante("Ana", 22, "Ciencias de la Computación")
estudiante3 = Estudiante("Yoel", 20, "Ingenieria de Sistemas")
# Creando universidad
u_ficticia = Universidad()
# Agregándole alumnos a la universidad
u_ficticia.agregar_estudiante(estudiante1)
u_ficticia.agregar_estudiante(estudiante2)
u_ficticia.agregar_estudiante(estudiante3)
#matriculando estudiantes en diferentes cursos:
estudiante1.matricular_curso(poo2)
poo2.agregar_estudiante(estudiante1)
estudiante1.matricular_curso(estructuras_datos)
estructuras_datos.agregar_estudiante(estudiante1)

estudiante2.matricular_curso(sistemas_operativos)
sistemas_operativos.agregar_estudiante(estudiante2)
estudiante2.matricular_curso(poo2)
poo2.agregar_estudiante(estudiante2)

estudiante3.matricular_curso(sistemas_operativos)
sistemas_operativos.agregar_estudiante(estudiante3)
estudiante3.matricular_curso(estructuras_datos)
estructuras_datos.agregar_estudiante(estudiante3)
# mostrando la información de todos los estudiantes
u_ficticia.mostrar_informacion_todos_los_estudiantes()


# Modificando la edad de un estudiante con el método cumpleanios
estudiante1.cumpleanios()

# Mostrar la información de los estudiantes
print("Información del Estudiante 1:")
estudiante1.mostrar_informacion()

print("\nInformación del Estudiante 2:")
estudiante2.mostrar_informacion()

print(f'\nInformación del Estudiante 3:')
estudiante3.mostrar_informacion()
print('\n')

# Creando universidad
una_puno = Universidad()
# Agregándole alumnos a la universidad
una_puno.agregar_estudiante(estudiante1)
una_puno.agregar_estudiante(estudiante2)
una_puno.agregar_estudiante(estudiante3)
print('')
# Mostrando la cantidad de estudiantes en la universidad
una_puno.imprimir_numero_estudiantes()
print('')
# Mostrando la información de todos los estudiantes de la universidad
una_puno.mostrar_informacion_todos_los_estudiantes()


# Verificando si los estudiantes de la universidad son mayores de edad:
for estudiante in una_puno.estudiantes:
    if estudiante.es_mayor_de_edad:
        print(f"El estudiante {estudiante.nombre} es mayor de edad")
    else:
        print(f"El estudiante {estudiante.nombre} no es mayor de edad")

# Creando instancias de la clase Libro y mostrando su información
print('-' * 8)
libro1 = Libro("The Data Science Handbook", "Carl Shan", 2015)
libro2 = Libro("Naked Statistics", "Charles Wheelan", 2014)

libro1.mostrar_informacion()
print('-' * 8)
libro2.mostrar_informacion()