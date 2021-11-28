Parola aleasa de noi hashuita cu sha256:
3f1a2bcaca2f02a8cd826b57caa7fa8a3214da1856aedb1a2c24ef29c3ea3771

Erori care au aparut:
Din caracterele care au codul asci peste 128 pot rezulta o eroare cand le xorezcu parola
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