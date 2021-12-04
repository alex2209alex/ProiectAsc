Numele echipei noastre: The Robotors
Numele echipei adverse: XorT11am
Cheia echipei adverse: PPPPPPPPPP (10P) sau PPPPPPPPPPP (11P) sau PPPPPPPPPPPP (12P) sau PPPPPPPPPPPPP (13P) sau PPPPPPPPPPPPPP (14P) sau PPPPPPPPPPPPPPP (15P)
Aceasta nu poate fi identificata cu exactitate deoarece echipa oponenta nu a implementat validarea parolei pt criptare / decriptare si toate parolele de mai sus ar cripta
si decripta fisierele in mod identic.

Rezolvare cerinta 1:
Printr-o xor-are a primelor 30 de caractere din fisierelor de input_oponenti.txt si output_oponenti caracter cu caracter s-a obtinut un fisier in care apare parola oponentilor
repetata. Acest lucru este facut
in scriptul cerinta1.py

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