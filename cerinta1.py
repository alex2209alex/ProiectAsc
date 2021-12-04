fileInput1 = open("input_oponenti.txt", "r")
fileInput2 = open("output_oponenti", "rb")
fileOutput = open("parola_oponenti_repetata.txt", "w")

input1 = list(fileInput1.read())
input2 = list(fileInput2.read())

for i in range(30):
    x = ord(input1[i]) ^ input2[i]
    fileOutput.write(chr(x))

fileOutput.close()
fileInput1.close()
fileInput2.close()
