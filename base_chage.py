CYFRY = '0123456789abcdef'

def zmien_podstawe(liczba_dziesietna, podstawa):
    stos_reszt = []

    while liczba_dziesietna > 0:
        reszta = liczba_dziesietna % podstawa
        stos_reszt.append(reszta)
        liczba_dziesietna = liczba_dziesietna // podstawa

    nowe_cyfry = []
    while stos_reszt:
        nowe_cyfry.append(CYFRY[stos_reszt.pop()])

    return ''.join(nowe_cyfry)