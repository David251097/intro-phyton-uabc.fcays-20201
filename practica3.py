class Estudiante:
  #Indicamos atributos para la clase
  edad=0
  carrera="desconocida"
  universidad="desconocida"
  genero="femenino"
  
  #Definimos funciones
  def festejar(self):
    print("Festejando")
    
  def estudiar(self,materia):
    print("Estudiando"+materia)
    
  def llorar(self):
    print("Llorando...")
    
  def dormir(self):
    print("Durmiendo....")
    
#Ajustamos la edad  
  def cambiarEdad(self, edadalumno):
      self.edad=edadalumno
      print("Nueva edad", edadalumno)
      
 #Generamos un nuevo estudiante
David=Estudiante()
David.estudiar(" logica para la programacion")
#Imprimimos atributo del objeto
David.cambiarEdad(23)
print(David.edad)


    