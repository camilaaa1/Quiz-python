Linea = "------------"
Glosario = {"Bucle":"Iteración de un valor seleccionado",
            "Booleano":"Variable que solo admite dos respuestas",
            "Arreglo":"'Variable' que almacena distintas variables",
            "Metodos":"parte de un código que se activa con cierto objeto",
            "Variables":'"Almacenador" de datos, pueden ser asignados por el código o ser digitados por el usuario dependiendo de su funció'}

num = Glosario.keys()
for num in reversed(Glosario):
    print("La palabra" ,str(num), "significa",":",str(Glosario[num]))

print (Linea)

for num in reversed(Glosario):
    print("La palabra",str(num),"significa",":","\n", "  ",str(Glosario[num]))