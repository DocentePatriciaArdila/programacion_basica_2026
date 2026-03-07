#ALGORITMO
#1. Pedir el nombre al usuario
#2. Pedir la edad al usuario
#3. Pedir la ciudad al usuario
#4. Mostrar el nombre
#5. Mostrar la edad
#6. Mostrar la ciudad
#7. Comparar si la edad es mayor o igual a 18
#8. Mostrar el resultado True o False

#PSEUDOCODIGO
#INICIO
   #LEER nombre
   #LEER edad
   #LEER ciudad
   #ESCRIBIR "Hola, me llamo", nombre
   #ESCRIBIR "Tengo", edad, "anos"
   #ESCRIBIR "Soy de", ciudad
   #ESCRIBIR "Es mayor de edad?", edad>18
#FIN

name=input('Dime tu nombre:')
age=int(input('dame tu edad:'))
city=input(input('Donde vives?'))
print('hola, me llamo',name)
print("Tengo", age,"años")
print("soy de",city )
print("Es mayor de edad?",age>18)
