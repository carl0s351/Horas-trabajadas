#Calculo horas trabajadas
#Preguntar al usuario el N° de horas trabajadas y mostrar en pantalla la paga que le corresponde

valor_hora = 7.824

while True:

    horas_trabajadas = float(input("N° de horas trabajadas: "))
    paga = valor_hora * horas_trabajadas
    print(f"Tu paga es:{paga:.3f}")


