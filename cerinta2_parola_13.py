inFile = open("output_oponenti.txt" , 'rb')
outFile = open("parola_13.txt",'w')
input = inFile.read()

# verificam fiecare caracter daca poate fi prima litera a parolei
# parcurgem din 13 in 13 si afisam rezultatele
# analizam parola_13.txt si vedem daca merita sa continuam testele pe celelalte caractere
pass_dict = {}
def eligible_char(start : int):
    dict = [[] for _ in range(256)]
    for small_char in range(ord('a'), ord('z') + 1):
        outFile.write(f"caracterul {chr(small_char)}\n")
        for i in range(start, len(input) + 1, 13):
            output_xor = small_char ^ input[i]
            dict[small_char].append(output_xor)
        dict[small_char] = set(dict[small_char])
        for results in dict[small_char]:
            outFile.write(f"{chr(results)} ")
        outFile.write("\n\n")

    for capital in range(ord('A'), ord('Z') + 1):
        outFile.write(f"caracterul {chr(capital)}\n")
        for i in range(start, len(input) + 1, 13):
            output_xor = capital ^ input[i]
            dict[capital].append(output_xor)
        dict[capital] = set(dict[capital])
        for results in dict[capital]:
            outFile.write(f"{chr(results)} ")
        outFile.write("\n\n")

    for digit in range(ord('0'), ord('9') + 1):
        outFile.write(f"caracterul {chr(digit)}\n")
        for i in range(start, len(input) + 1, 13):
            output_xor = digit ^ input[i]
            dict[digit].append(output_xor)
        dict[digit] = set(dict[digit])
        for results in dict[digit]:
            outFile.write(f"{chr(results)} ")
        outFile.write("\n\n")    

def eligible_char_v2(start : int):
    dict = [[] for _ in range(256)]
    for small_char in range(ord('a'), ord('z') + 1):
        outFile.write(f"caracterul {chr(small_char)}\n")
        for i in range(start, len(input) - 3, 13):
            output_xor = small_char ^ input[i]
            dict[small_char].append(output_xor)
        dict[small_char] = set(dict[small_char])
        for results in dict[small_char]:
            outFile.write(f"{chr(results)} ")
        outFile.write("\n\n")

    for capital in range(ord('A'), ord('Z') + 1):
        outFile.write(f"caracterul {chr(capital)}\n")
        for i in range(start, len(input) - 3, 13):
            output_xor = capital ^ input[i]
            dict[capital].append(output_xor)
        dict[capital] = set(dict[capital])
        for results in dict[capital]:
            outFile.write(f"{chr(results)} ")
        outFile.write("\n\n")

    for digit in range(ord('0'), ord('9') + 1):
        outFile.write(f"caracterul {chr(digit)}\n")
        for i in range(start, len(input) - 3, 13):
            output_xor = digit ^ input[i]
            dict[digit].append(output_xor)
        dict[digit] = set(dict[digit])
        for results in dict[digit]:
            outFile.write(f"{chr(results)} ")
        outFile.write("\n\n")

outFile.write("TESTARE CARACTER #1:\n\n\n")
eligible_char(0)

# Exista caractere eligibile. Continuam testarea pana nu mai gasim caractere eligibile sau ajungem la ultimul caracter
# Caractere eligibile : P, S
pass_dict[1] = ('P', 'S')

outFile.write("TESTARE CARACTER #2 : \n\n\n")
eligible_char(1)
#Caractere eligibile : q, r, u
pass_dict[2] = ('q', 'r', 'u')

outFile.write("TESTARE CARACTER #3 : \n\n\n")
eligible_char(2)
#Caractere eligibile : h, l, o 
pass_dict[3] = ('h','l', 'o')

outFile.write("TESTARE CARACTER #4 : \n\n\n")
eligible_char(3)
#Caractere eligibile : i, j 
pass_dict[4] = ('i','j')

# La incercarea testului pentru caracterul #5 depasim capatul fisierului
# Pentru a trece peste aceasta problema voi crea alta functie 
# Modific functia eligible_char pentru a testa fisierul de output fara ultimele 4 caractere

outFile.write("TESTARE CARACTER #5 : \n\n\n")
eligible_char_v2(4)
#Caractere eligibile : e , f  
pass_dict[5] = ('e','f')

outFile.write("TESTARE CARACTER #6 : \n\n\n")
eligible_char_v2(5)
#Caractere eligibile : c  
pass_dict[6] = ('c')

outFile.write("TESTARE CARACTER #7 : \n\n\n")
eligible_char_v2(6)
#Caractere eligibile : t , w  
pass_dict[7] = ('t','w')

outFile.write("TESTARE CARACTER #8 : \n\n\n")
eligible_char_v2(7)
#Caractere eligibile : A, B, F  
pass_dict[8] = ('A','B','F')

outFile.write("TESTARE CARACTER #9 : \n\n\n")
eligible_char_v2(8)
#Caractere eligibile : P, S, T  
pass_dict[9] = ('P','S', 'T')

outFile.write("TESTARE CARACTER #10 : \n\n\n")
eligible_char_v2(9)
#Caractere eligibile : C, D  
pass_dict[10] = ('C','D')

outFile.write("TESTARE CARACTER #11 : \n\n\n")
eligible_char_v2(10)
#Caractere eligibile : 1 , 2   
pass_dict[11] = ('1','2')

outFile.write("TESTARE CARACTER #12 : \n\n\n")
eligible_char_v2(11)
#Caractere eligibile : 1, 2, 5  
pass_dict[12] = ('1','2','5')

outFile.write("TESTARE CARACTER #13 : \n\n\n")
eligible_char_v2(12)
#Caractere eligibile : 0, 3
pass_dict[13] = ('0','3')

# Am gasit caracterele eligibile pentru fiecare pozitie din parola noastra
# Cu aceasta metoda am redus posibilitatile de la 60^15 la 31104

inFile.close()
outFile.close()

passwords = open("pass.txt", 'w')

for i1 in pass_dict[1]:
    for i2 in pass_dict[2]:
        for i3 in pass_dict[3]:
            for i4 in pass_dict[4]:
                for i5 in pass_dict[5]:
                    for i6 in pass_dict[6]:
                        for i7 in pass_dict[7]:
                            for i8 in pass_dict[8]:
                                for i9 in pass_dict[9]:
                                    for i10 in pass_dict[10]:
                                        for i11 in pass_dict[11]:
                                            for i12 in pass_dict[12]:
                                                for i13 in pass_dict[13]:
                                                    passwords.write(f"{i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13}\n")