#Calculo horas trabajadas
#Preguntar al usuario el N° de horas trabajadas y mostrar en pantalla la paga que le corresponde

valor_hora_obrero = 7.824
valor_hora_admin = 10.000
valor_hora_ing = 12.000

while True:

    horas_trabajadas = float(input("N° de horas trabajadas: "))
    paga = valor_hora * horas_trabajadas
    print(f"Tu paga es:{paga:.3f}")


