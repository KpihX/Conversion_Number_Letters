def NeL(n):
    """Ecris un nombre en lettres"""
    if type(n) == str:
        if n == "":
            m = "   Vous n'avez rien saisi!"
        else:
            m = "   '" + n + "'" + " est une chaine de caractère et non un nombre entier positif!"
    elif type(n) == float:
        m = "   " + str(n) + " est un floatant et non un nombre entier positif!"
    elif n < 0:
        m = "   " + str(n) + " est un nombre entier négatif et non un nombre entier positif!"
    else:
        i = 13
        j = 0
        k = 0
        l = 12
        m = ''
        n = str(n)
        T = []
        T1 = ['', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf']
        T2 = ['dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf']
        T3 = ['', '', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante', 'soixante', 'quatre-vingt', 'quatre-vingt']
        T4 = ['', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf']
        T5 = ['mille ', 'mille ', 'un million ', 'millions ', 'un milliard ', 'milliards ']
                
        for h in n:
            T.append(int(h))
        
        t = len(T)

        while i < t+1:
            T5 += (T5 + T5)
            l += 12
            i += 12

        while j < l-t:
            T.insert(0, 0)    
            j += 1
        
        while k < l/2:
            q = T[k]
            T[k] = T[l-1-k]
            T[l-1-k] = q
            k += 1

        if n == '0':
            m = 'zéro'
        else:
            while l > 2:
                if T[l-3] == 1 and T[l-2] == 0 and T[l-1] == 0:
                    if T[0] == 1 and l == 3:
                        m += ' un'  
                    else:
                        m += T5[int((l/3-2)*2)]
                elif T[l-1] != 0 or T[l-2] != 0 or T[l-3] != 0:
                    if T[l-2] == 1:
                        s = T2[T[l-3]]
                    elif T[l-2] == 7 or T[l-2] == 9:
                        if T[0] == 1 and l == 3:
                            s = T3[T[1]]  + '-et-onze'
                        else:
                            s = T3[T[l-2]] + '-' + T2[T[l-3]]
                    else:
                        if T[1] == 8 and T[0] == 0 and l == 3:
                            s = 'quatre-vingts'
                        elif T[1] != 8 and T[0] == 1 and l == 3:
                            s = T3[T[1]]  + '-et-un' 
                        else:
                            s = T3[T[l-2]]  + ' ' + T1[T[l-3]]

                    if T[l-1] != 0:
                        if T[2] != 1 and T[1] == 0 and T[0] == 0 and l == 3:
                            s = T4[T[l-1]-1] + ' cents'
                        else:
                            s = T4[T[l-1]-1] + ' cent ' + s 
                    
                    if l != 3:
                        m += s + ' ' + T5[int((l/3-2)*2+1)]
                    else:
                        m += s
                        
                if l != 3 and (l-3) % 12 == 0 and T[l-4] == 0 and T[l-5] == 0 and T[l-6] == 0:
                    m += 'milliards '
                
                l -= 3
        m = "   " + n + ' = ' + m
    return m

r = 'o'

while r.lower() == 'o':
    a = input("Indiquez le nombre à écrire en lettres (entier positif) : ")
    try:
        print(NeL(int(a)))
    except ValueError:
        try:
            print(NeL(float(a)))
        except ValueError:
            print(NeL(str(a)))
    
    r = input("Voulez-vous entrer à nouveau un nombre ? ('o' ou 'n') ")

q = input("Tapez 'Entrer' pour quitter")
