#parola poate contine a...z, A...Z si 0...9
fileInput = open("output_oponenti", "rb")
fileOutput = open("cerinta2_parola_11_output.txt", "w")
input = fileInput.read()

#incerc fiecare posibilitate pe prima pozitie si afisez toate caracterele formate
#litere mici
dictionar = [[] for x in range(256)]
for x in range(ord("a"), ord("z") + 1):
    sir = f"caracterul: {chr(x)}\n"
    fileOutput.write(sir)
    for i in range(0,len(input),11):
        rez = x ^ input[i]
        if x not in dictionar[x]:
            dictionar[x].append(rez)
    for y in dictionar[x]:
        sir = f"{chr(y)} "
        fileOutput.write(sir)
    sir = "\n\n"
    fileOutput.write(sir)

#litere mari
for x in range(ord("A"), ord("Z") + 1):
    sir = f"caracterul: {chr(x)}\n"
    fileOutput.write(sir)
    for i in range(0,len(input),11):
        rez = x ^ input[i]
        if x not in dictionar[x]:
            dictionar[x].append(rez)
    for y in dictionar[x]:
        sir = f"{chr(y)} "
        fileOutput.write(sir)
    sir = "\n\n"
    fileOutput.write(sir)

#cifre
for x in range(ord("0"), ord("9") + 1):
    sir = f"caracterul: {chr(x)}\n"
    fileOutput.write(sir)
    for i in range(0,len(input),11):
        rez = x ^ input[i]
        if x not in dictionar[x]:
            dictionar[x].append(rez)
    for y in dictionar[x]:
        sir = f"{chr(y)} "
        fileOutput.write(sir)
    sir = "\n\n"
    fileOutput.write(sir)

"""
    Se observa in fisierul cerinta2_parola_11_output.txt ca niciun caracter eligibil nu se poate afla pe prima pozitie a parolei de lungime 11 deoarece dau caractere invalide
cand incerc sa decriptez partial fisierul. Din aceasta cauza se poate determina ca parola nu are lungime 11.
"""