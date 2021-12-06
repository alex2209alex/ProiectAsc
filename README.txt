Numele echipei noastre: The Robotors
Numele echipei adverse: XorT11am
Cheia echipei adverse: ProiectASC123

Rezolvare cerinta 1:
Printr-o xor-are a primelor 30 de caractere din fisierelor de input_oponenti.txt si output_oponenti caracter cu caracter s-a obtinut un fisier in care apare parola oponentilor
repetata. Acest lucru este facut in scriptul cerinta1.py

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Rezolvare cerinta 2:
Presupun prin absurd ca parola adversarilor are doar 10 caractere. Atunci incerc toate caracterele posibile sa se afle pe prima pozitie a parolei(A...Z, a...z si 0...9) si decriptez
caracterele aflate in fisierul de output_oponenti pe pozitii criptate de prima cifra si afisez in fisierul cerinta2_parola_10_output.txt pentru fiecare caracter ce caractere rezulta
daca l-as folosi pe prima pozitie. Studiind fisierul cerinta2_parola_10_output.txt am observat ca niciun caracter din A...Z, a...z sau 0...9 nu se poate afla pe prima pozitie deoarece
acestea dau cel putin un caracter special care nu ar trebui sa fie in inputul oponentilor. Deci presupunerea facuta este falsa si parola oponentilor nu are 10 caractere. Acest lucru
este efectuat de scriptul cerinta2_parola_10.py.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Presupun prin absurd ca parola adversarilor are doar 11 caractere. Atunci incerc toate caracterele posibile sa se afle pe prima pozitie a parolei(A...Z, a...z si 0...9) si decriptez
caracterele aflate in fisierul de output_oponenti pe pozitii criptate de prima cifra si afisez in fisierul cerinta2_parola_11_output.txt pentru fiecare caracter ce caractere rezulta
daca l-as folosi pe prima pozitie. Studiind fisierul cerinta2_parola_11_output.txt am observat ca niciun caracter din A...Z, a...z sau 0...9 nu se poate afla pe prima pozitie deoarece
acestea dau cel putin un caracter special care nu ar trebui sa fie in inputul oponentilor. Deci presupunerea facuta este falsa si parola oponentilor nu are 11 caractere. Acest lucru
este efectuat de scriptul cerinta2_parola_11.py.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Presupun prin absurd ca parola adversarilor are doar 12 caractere. Atunci incerc toate caracterele posibile sa se afle pe prima pozitie a parolei(A...Z, a...z si 0...9) si decriptez
caracterele aflate in fisierul de output_oponenti pe pozitii criptate de prima cifra si afisez in fisierul cerinta2_parola_12_output.txt pentru fiecare caracter ce caractere rezulta
daca l-as folosi pe prima pozitie. Studiind fisierul cerinta2_parola_12_output.txt am observat ca doar caracterele c si d pot fi eligibile sa se afle pe prima pozitie. Acum incerc sa gasesc
caracterele care ar putea fi pe a doua pozitie. Studiind fisierul cerinta2_parola_12_output.txt am observat ca niciun caracter din A...Z, a...z sau 0...9 nu se poate afla pe a doua
pozitie deoarece acestea dau cel putin un caracter special care nu ar trebui sa fie in inputul oponentilor. Deci presupunerea facuta este falsa si parola oponentilor nu are 12 caractere. Acest lucru
este efectuat de scriptul cerinta2_parola_12.py.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Presupun prin absurd ca parola adversarilor are 13 caractere. Am testat compatibilitatea primului caracter posibil al parolei parcurgand sirul din 13 in 13. Dupa prima parcurgere am observat din analiza
fisierului parola_13.txt ca doar 'P' si 'S' sunt compatibile. Prin continuarea testelor pentru fiecare pozitie in parola, am obtinut un set de caractere eligibile. Prin metoda backtraking am generat toate
parolele posibile corecte in fisierul pass.txt. Acest fisier este generat cu ajutorul script-ului cerinta2_parola_13.py. Cu fiecare parola din fisier am decriptat primele 200 de caractere din output_oponenti.
Am afisat rezultatele in fisierul fisier_verificare_parole.txt. Prin analiza rezultatelor am constatat ca textul incepe cu "SURSA: http". Folosind functia de search din editor am gasit 6 parole care generau acest
output. Prin analiza celor 6 parole am constat ca cea corecta se afla pe linia 8668 in fisierul pass.txt, adica 'ProiectASC123'. Pentru a ne verifica am decriptat fisierul output_oponenti in fisierul
input_recuperat_oponenti.txt si am constat ca textul era corect in limba romana. De aici rezulta ca parola oponentilor este 'ProiectASC123' si nu are rost sa continuam testarea pentru parole de 14, respectiv 15
caractere.

----------------------------------------------------------------------------------------------------------------
Parola aleasa de noi hashuita cu sha256:
3f1a2bcaca2f02a8cd826b57caa7fa8a3214da1856aedb1a2c24ef29c3ea3771

Erori care au aparut:
Din caracterele care au codul asci peste 128 pot rezulta o eroare cand le xorez cu parola
dand coduri asci care nu pot fi convertite in caractere precum 129, 141, 143, 144, 157,160
si 173
Pentru a rezolva aceasta problema am sters din inputul original toate caracterele cu codul 
asci > 128, care nu sunt incluse in litere mari mici sau semne de punctuatie uzuale.




Impartire initiala a muncii:
Partea de criptare: Tanase Flavian
Partea de decriptare: Pavel Alexandru

Linkuri utile:
https://en.wikipedia.org/wiki/XOR_cipher
https://www.ascii-code.com/
https://medium.com/@dwernychukjosh/sha256-encryption-with-python-bf216db497f9
