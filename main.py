from copy import deepcopy
import sys


def tabla_kirajzolasa(tabla):
    print(tabla[0] + "(00)----------------------" + tabla[1] +
          "(01)----------------------" + tabla[2] + "(02)")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|       " + tabla[8] + "(08)--------------" +
          tabla[9] + "(09)--------------" + tabla[10] + "(10)     |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |        " + tabla[16] + "(16)-----" +
          tabla[17] + "(17)-----" + tabla[18] + "(18)       |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(tabla[3] + "(03)---" + tabla[11] + "(11)----" + tabla[19] + "(19)               " +
          tabla[20] + "(20)----" + tabla[12] + "(12)---" + tabla[4] + "(04)")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |        " + tabla[21] + "(21)-----" +
          tabla[22] + "(22)-----" + tabla[23] + "(23)       |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       " + tabla[13] + "(13)--------------" +
          tabla[14] + "(14)--------------" + tabla[15] + "(15)     |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(tabla[5] + "(05)----------------------" + tabla[6] +
          "(06)----------------------" + tabla[7] + "(07)")
    print("\n")

# megallapitja, hogy az egyes poziciokkal melyik mezok szomszedosak
def szomszedos_poziciok(pozicio):
    szomszedok = [
        [1, 3],
        [0, 2, 9],
        [1, 4],
        [0, 5, 11],
        [2, 7, 12],
        [3, 6],
        [5, 7, 14],
        [4, 6],
        [9, 11],
        [1, 8, 10, 17],
        [9, 12],
        [3, 8, 13, 19],
        [4, 10, 15, 20],
        [11, 14],
        [6, 13, 15, 22],
        [12, 14],
        [17, 19],
        [9, 16, 18],
        [17, 20],
        [11, 16, 21],
        [12, 18, 23],
        [19, 22],
        [21, 23, 14],
        [20, 22]
    ]
    return szomszedok[pozicio]

# malomképzéshez ellenörzi,hogy egy sorban 1 játékos korongjai vannak
def jatekos_egy_sorban(jatekos, tabla, p1, p2):
    if tabla[p1] == jatekos and tabla[p2] == jatekos:
        return True
    else:
        return False

# true or false
def malom_a_kovetkezo_korben(pozicio, tabla, jatekos):
    mal = [
        (jatekos_egy_sorban(jatekos, tabla, 1, 2) or jatekos_egy_sorban(jatekos, tabla, 3, 5)),
        (jatekos_egy_sorban(jatekos, tabla, 0, 2) or jatekos_egy_sorban(jatekos, tabla, 9, 17)),
        (jatekos_egy_sorban(jatekos, tabla, 0, 1) or jatekos_egy_sorban(jatekos, tabla, 4, 7)),
        (jatekos_egy_sorban(jatekos, tabla, 0, 5) or jatekos_egy_sorban(jatekos, tabla, 11, 19)),
        (jatekos_egy_sorban(jatekos, tabla, 2, 7) or jatekos_egy_sorban(jatekos, tabla, 12, 20)),
        (jatekos_egy_sorban(jatekos, tabla, 0, 3) or jatekos_egy_sorban(jatekos, tabla, 6, 7)),
        (jatekos_egy_sorban(jatekos, tabla, 5, 7) or jatekos_egy_sorban(jatekos, tabla, 14, 22)),
        (jatekos_egy_sorban(jatekos, tabla, 2, 4) or jatekos_egy_sorban(jatekos, tabla, 5, 6)),
        (jatekos_egy_sorban(jatekos, tabla, 9, 10) or jatekos_egy_sorban(jatekos, tabla, 11, 13)),
        (jatekos_egy_sorban(jatekos, tabla, 8, 10) or jatekos_egy_sorban(jatekos, tabla, 1, 17)),
        (jatekos_egy_sorban(jatekos, tabla, 8, 9) or jatekos_egy_sorban(jatekos, tabla, 12, 15)),
        (jatekos_egy_sorban(jatekos, tabla, 3, 19) or jatekos_egy_sorban(jatekos, tabla, 8, 13)),
        (jatekos_egy_sorban(jatekos, tabla, 20, 4) or jatekos_egy_sorban(jatekos, tabla, 10, 15)),
        (jatekos_egy_sorban(jatekos, tabla, 8, 11) or jatekos_egy_sorban(jatekos, tabla, 14, 15)),
        (jatekos_egy_sorban(jatekos, tabla, 13, 15) or jatekos_egy_sorban(jatekos, tabla, 6, 22)),
        (jatekos_egy_sorban(jatekos, tabla, 13, 14) or jatekos_egy_sorban(jatekos, tabla, 10, 12)),
        (jatekos_egy_sorban(jatekos, tabla, 17, 18) or jatekos_egy_sorban(jatekos, tabla, 19, 21)),
        (jatekos_egy_sorban(jatekos, tabla, 1, 9) or jatekos_egy_sorban(jatekos, tabla, 16, 18)),
        (jatekos_egy_sorban(jatekos, tabla, 16, 17) or jatekos_egy_sorban(jatekos, tabla, 20, 23)),
        (jatekos_egy_sorban(jatekos, tabla, 16, 21) or jatekos_egy_sorban(jatekos, tabla, 3, 11)),
        (jatekos_egy_sorban(jatekos, tabla, 12, 4) or jatekos_egy_sorban(jatekos, tabla, 18, 23)),
        (jatekos_egy_sorban(jatekos, tabla, 16, 19) or jatekos_egy_sorban(jatekos, tabla, 22, 23)),
        (jatekos_egy_sorban(jatekos, tabla, 6, 14) or jatekos_egy_sorban(jatekos, tabla, 21, 23)),
        (jatekos_egy_sorban(jatekos, tabla, 18, 20) or jatekos_egy_sorban(jatekos, tabla, 21, 22))
    ]

    return mal[pozicio]

# igazzal vagy hamissal tér vissza(az első és a második fázisban is lehet malom)
def malom(pozicio, tabla):
    p = tabla[pozicio]
    if p != 'x':
        return malom_a_kovetkezo_korben(pozicio, tabla, p)
    else:
        return False

# ellenőrzi egy játékos korongjainak számát(ha 3, akkor engedélyezett az ugrálás a táblán, 3-nál kevesebb, akkor a másik játékos nyert)
def korongok_szama(tabla, jatekos):
    return tabla.count(jatekos)


def korong_eltavolitasa(tabla_masolat, tabla_lista, jatekos):
    for i in range(len(tabla_masolat)):
        if jatekos == '1':
            opp = '2'
        else:
            opp = '1'
        if tabla_masolat[i] == opp:
            if not malom(i, tabla_masolat):
                uj_tabla = deepcopy(tabla_masolat)
                uj_tabla[i] = 'x'
                tabla_lista.append(uj_tabla)
    return tabla_lista


def lepesek_szakasz2ben(tabla, jatekos):
    tabla_lista = []
    for i in range(len(tabla)):
        if tabla[i] == jatekos:
            szomszedok = szomszedos_poziciok(i)

            for poz in szomszedok:
                if tabla[poz] == 'x':
                    tabla_masolat = deepcopy(tabla)
                    tabla_masolat[i] = 'x'
                    tabla_masolat[poz] = jatekos

                    if malom(poz, tabla_masolat):
                        tabla_lista = korong_eltavolitasa(tabla_masolat, tabla_lista, jatekos)
                    else:
                        tabla_lista.append(tabla_masolat)
    return tabla_lista


def lepesek_szakasz3ban(tabla, jatekos):
    tabla_lista = []

    for i in range(len(tabla)):
        if tabla[i] == jatekos:
            for j in range(len(tabla)):
                if tabla[j] == 'x':
                    tabla_masolat = deepcopy(tabla)
                    tabla_masolat[i] = 'x'
                    tabla_masolat[j] = jatekos

                    if malom(j, tabla_masolat):
                        tabla_lista = korong_eltavolitasa(tabla_masolat, tabla_lista, jatekos)
                    else:
                        tabla_lista.append(tabla_masolat)
    return tabla_lista


def lepesek_szakasz2_vagy_szakasz3ban(tabla, jatekos='1'):
    if korongok_szama(tabla, jatekos) == 3:
        return lepesek_szakasz3ban(tabla, jatekos)
    else:
        return lepesek_szakasz2ben(tabla, jatekos)


def main():

    # tábla feltöltése mindenhol x-el
    tabla = []
    for i in range(24):
        tabla.append('x')

    tabla_kirajzolasa(tabla)

    # 1. szakasz mindkét játékos felhelyez 9 bábut a táblára
    for i in range(9):

        # 1. játékos

        kesz_jatekos1 = False
        while not kesz_jatekos1:
            try:
                poz1 = int(input("\n 1. JÁTÉKOS: Kérem helyezzen el egy '1'-es korongot a táblára: "))
                print()
                if poz1 == 99:
                    sys.exit()
                if tabla[poz1] == 'x':
                    tabla[poz1] = '1'

                    # már itt is lehet malmot adni
                    if malom(poz1, tabla):
                        korong_elhelyezve = False
                        while not korong_elhelyezve:
                            try:
                                poz2 = int(input('\nMalom!\nKérem távolítson el egy "2"-es korongot: '))
                                # nem lehet olyan korongot eltávolítani ami malomban van
                                if tabla[poz2] == '2' and not malom(poz2, tabla) or (malom(poz2, tabla) and korongok_szama(tabla, '1') == 3):
                                    tabla[poz2] = 'x'
                                    korong_elhelyezve = True
                                else:
                                    print("Érvénytelen pozició, kérem próbálja újra!")
                            except Exception as e:
                                print("Érvénytelen input!")
                                print(str(e))

                    kesz_jatekos1 = True

                else:
                    print("A pozició foglalt!")
            except Exception as e:
                print("Érvénytelen input!")
                print(str(e))

        tabla_kirajzolasa(tabla)

        # 2. játékos

        kesz_jatekos2 = False
        while not kesz_jatekos2:
            try:
                poz1 = int(input("\n 2. JÁTÉKOS: Kérem helyezzen el egy '2'-es korongot a táblára: "))
                print()
                if poz1 == 99:
                    sys.exit()
                if tabla[poz1] == 'x':
                    tabla[poz1] = '2'
                    if malom(poz1, tabla):
                        korong_elhelyezve = False
                        while not korong_elhelyezve:
                            try:
                                poz2 = int(input('\nMalom!\nKérem távolítson el egy "1"-es korongot: '))
                                if tabla[poz2] == '1' and not malom(poz2, tabla) or (malom(poz2, tabla) and korongok_szama(tabla, '2') == 3):
                                    tabla[poz2] = 'x'
                                    korong_elhelyezve = True
                                else:
                                    print("Érvénytelen pozició, kérem próbálja újra!")
                            except Exception as e:
                                print("Érvénytelen input!")
                                print(str(e))

                    kesz_jatekos2 = True

                else:
                    print("A pozició foglalt")
            except Exception as e:
                print("Érvénytelen input!")
                print(str(e))

        tabla_kirajzolasa(tabla)

    print('\n')
    print("2. szakasz")
    print('\n')

    while True:

        # 1. játékos

        tabla_kirajzolasa(tabla)
        lepes = False
        while not lepes:
            try:
                szabad = False

                if korongok_szama(tabla, '1') == 3:
                    korong_3 = True
                else:
                    korong_3 = False

                while not szabad:
                    poz1 = int(input("\n 1. JÁTÉKOS: Melyik '1'-es korongot szeretné mozgatni?: "))

                    while tabla[poz1] != '1':
                        print("Érvénytelen. Próbálja újra.")
                        poz1 = int(input("\n 1. JÁTÉKOS: Melyik '1'-es korongot szeretné mozgatni?: "))

                    if korong_3:
                        szabad = True
                        print("3. SZAKASZ az 1. JÁTÉKOS számára. Ugrás engedélyezve")
                        break

                    lehetseges_lepesek = szomszedos_poziciok(poz1)

                    for szpoz in lehetseges_lepesek:
                        if tabla[szpoz] == 'x':
                            szabad = True
                            break
                    if szabad == False:
                        print("Nincs szabad szomszédos mező!")

                szakasz_2_lepes = False

                while not szakasz_2_lepes:
                    uj_poz = int(input("'1' Az új pozició : "))

                    if uj_poz in szomszedos_poziciok(poz1) or korong_3:

                        if tabla[uj_poz] == 'x':
                            tabla[poz1] = 'x'
                            tabla[uj_poz] = '1'

                            if malom(uj_poz, tabla):
                                eltavolitott = False
                                while not eltavolitott:
                                    try:
                                        tabla_kirajzolasa(tabla)
                                        eltavolitott_poz = int(input("\nMalom!\nKérem távolítson el egy '2'-es korongot: "))

                                        if tabla[eltavolitott_poz] == '2' and not malom(eltavolitott_poz, tabla) or (malom(eltavolitott_poz, tabla) and korongok_szama(tabla, "1") == 3):
                                            tabla[eltavolitott_poz] = 'x'
                                            eltavolitott = True
                                        else:
                                            print("Érvénytelen pocició")
                                    except Exception as e:
                                        print(str(e))
                                        print("Érvénytelen input")

                            szakasz_2_lepes = True
                            lepes = True

                        else:
                            print("Érvénytelen pozició")

                    else:
                        print("Nem szomszédos mező. Próbálja újra.")

            except Exception as e:
                print(str(e))

        if len(lepesek_szakasz2_vagy_szakasz3ban(tabla, '1')) == 0:
            print("DÖNTETLEN")
            sys.exit()

        elif korongok_szama(tabla, '2') < 3:
            print("1. JÁTÉKOS NYERT")
            sys.exit()

        else:
            tabla_kirajzolasa(tabla)

        # 2. játékos

        lepes = False
        while not lepes:
            try:
                szabad = False

                if korongok_szama(tabla, '2') == 3:
                    korong_3 = True
                else:
                    korong_3 = False

                while not szabad:
                    poz1 = int(
                        input("\n2. JÁTÉKOS: Melyik '2'-es korongot szeretné mozgatni?: "))

                    while tabla[poz1] != '2':
                        print("Érvénytelen. Próbálja újra.")
                        poz1 = int(input("\n2. JÁTÉKOS: Melyik '1'-es korongot szeretné mozgatni?:"))

                    if korong_3:
                        szabad = True
                        print("3. SZAKASZ az 2. JÁTÉKOS számára. Ugrás engedélyezve")
                        break

                    lehetseges_lepesek = szomszedos_poziciok(poz1)

                    for szpoz in lehetseges_lepesek:
                        if tabla[szpoz] == 'x':
                            szabad = True
                            break
                    if szabad == False:
                        print("Nincs szabad szomszédos mező!")

                szakasz_2_lepes = False

                while not szakasz_2_lepes:
                    uj_poz = int(input("'2' Az új pozició : "))

                    if uj_poz in szomszedos_poziciok(poz1) or korong_3:

                        if tabla[uj_poz] == 'x':
                            tabla[poz1] = 'x'
                            tabla[uj_poz] = '2'

                            if malom(uj_poz, tabla):
                                eltavolitott = False
                                while not eltavolitott:
                                    try:
                                        tabla_kirajzolasa(tabla)
                                        eltavolitott_poz = int(input("\nMalom!\nKérem távolítson el egy '1'-es korongot: "))

                                        if tabla[eltavolitott_poz] == '1' and not malom(eltavolitott_poz, tabla) or (malom(eltavolitott_poz, tabla) and korongok_szama(tabla, "2") == 3):
                                            tabla[eltavolitott_poz] = 'x'
                                            eltavolitott = True
                                        else:
                                            print("Érvénytelen pocició")
                                    except Exception as e:
                                        print(str(e))
                                        print("Érvénytelen input")

                            szakasz_2_lepes = True
                            lepes = True

                        else:
                            print("Érvénytelen pozició")

                    else:
                        print("Nem szomszédos mező. Próbálja újra.")

            except Exception as e:
                print(str(e))

        if len(lepesek_szakasz2_vagy_szakasz3ban(tabla, '2')) == 0:
            print("DÖNTETLEN")
            sys.exit()

        elif korongok_szama(tabla, '1') < 3:
            print("2. JÁTÉKOS NYERT")
            sys.exit()

        else:
            tabla_kirajzolasa(tabla)


if __name__ == "__main__":
    main()

