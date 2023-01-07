class Alumno:
    
    def datos(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def data(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
 

    def resultado(self):
            if self.nota < 5:
                print("El alumno ha suspendido")
            else:
                print("El alumno ha aprobado")
    def espacio(self):
            print("     ")
 
alumno1=Alumno()
alumno2=Alumno()
alumno3=Alumno()
alumno4=Alumno()


alumno1.datos("Nicolás González",10)
alumno2.datos("Ronald Giménez",2)
alumno3.datos("Mario Rodriguez",10)
alumno4.datos("Tamara Cegla", 10)

alumno1.data()
alumno1.resultado()
alumno1.espacio()

alumno2.data()
alumno2.resultado()
alumno2.espacio()

alumno3.data()
alumno3.resultado()
alumno3.espacio()

alumno4.data()
alumno4.resultado()
alumno4.espacio()
