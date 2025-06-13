from datetime import datetime

def este_cnp_valid(cnp):
    if len(cnp) != 13 or not cnp.isdigit():
        return False

    # Cifra de control
    control = "279146358279"
    suma = sum(int(cnp[i]) * int(control[i]) for i in range(12))
    cifra_control = suma % 11
    if cifra_control == 10:
        cifra_control = 1
    if cifra_control != int(cnp[-1]):
        return False

    # Validare dată
    try:
        anul = int(cnp[1:3])
        luna = int(cnp[3:5])
        ziua = int(cnp[5:7])
        if cnp[0] in "12":  # 1900-1999
            anul += 1900
        elif cnp[0] in "56":
            anul += 2000

        datetime(anul, luna, ziua)
    except ValueError:
        return False

    return True
