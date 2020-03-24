# Input altura do objeto for output velocidade final e tempo de queda

from math import sqrt
while True:
    print("If you tell me the height of an object, I'll tell you its final velocity.")

    h = input("Height in meters: ")

    # Sair do programa
    if h in "exit":
        ext = input("Are you sure? ")
        if ext in "yes":
            exit()
        else:
            break     # NAO ESTA VOLTANDO PARA O CALCULO

    # Calculo da velocidade
    else:
        g = 9.80665  # m/sˆ2

        V = sqrt(2*g*float(h))
        t = V/g

        print(round(V*3.6, 2), "km/h")
        print(round(t, 2), "seconds of free fall")
        print("--------------------")
