inputFile = open("output_oponenti", "rb")
inputFile2 = open("pass.txt", "r")
outputFile = open("fisier_verificare_parole.txt", "w")

criptedText = inputFile.read()

poz = 1
for x in inputFile2.readlines():
    outputFile.write(f"{poz}\n")
    poz += 1
    str = x[:13] * 20
    outputFile.write(f"{str}\n")
    for i in range(200):
        outputFile.write(f"{chr(criptedText[i] ^ ord(str[i]))}")
    outputFile.write("\n\n")