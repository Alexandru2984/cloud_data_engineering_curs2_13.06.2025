import re

def valideaza_email(email):
    """
    Verifică dacă o adresă de email este corectă din punct de vedere al formei,
    folosind o expresie regulată.

    Args:
        email (str): Adresa de email de verificat.

    Returns:
        bool: True dacă emailul este valid din punct de vedere al formei, False altfel.
    """
    # Expresia regulată pentru validarea unei adrese de email.
    # Aceasta este o expresie destul de standard și cuprinzătoare.
    # Explicatie pe scurt:
    # ^                  - începutul șirului
    # [a-zA-Z0-9._%+-]+  - un sau mai multe caractere (litere, cifre, punct, underscore, %, +, -)
    # @                  - simbolul '@'
    # [a-zA-Z0-9.-]+     - un sau mai multe caractere (litere, cifre, punct, -) pentru numele de domeniu
    # \.                 - un punct (escapat pentru că '.' e caracter special în regex)
    # [a-zA-Z]{2,}       - două sau mai multe litere pentru TLD (top-level domain, ex: com, org, ro)
    # $                  - sfârșitul șirului
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # re.match() încearcă să potrivească regex-ul de la începutul șirului.
    # Dacă găsește o potrivire, returnează un obiect match; altfel, returnează None.
    if re.match(regex, email):
        return True
    else:
        return False

# --- Exemple de utilizare ---

print("--- Teste de validare ---")

email_valid1 = "test@exemplu.com"
print(f"'{email_valid1}' este valid: {valideaza_email(email_valid1)}")

email_valid2 = "prenume.nume123@domeniu.co.uk"
print(f"'{email_valid2}' este valid: {valideaza_email(email_valid2)}")

email_valid3 = "user_name+tag@sub.domeniu.ro"
print(f"'{email_valid3}' este valid: {valideaza_email(email_valid3)}")

print("\n--- Teste de invalidare ---")

email_invalid1 = "email_fara_@domeniu.com"
print(f"'{email_invalid1}' este valid: {valideaza_email(email_invalid1)}")

email_invalid2 = "email@domeniu" # Fără TLD
print(f"'{email_invalid2}' este valid: {valideaza_email(email_invalid2)}")

email_invalid3 = "@domeniu.com" # Fără user
print(f"'{email_invalid3}' este valid: {valideaza_email(email_invalid3)}")

email_invalid4 = "email@.com" # Domeniu invalid
print(f"'{email_invalid4}' este valid: {valideaza_email(email_invalid4)}")

email_invalid5 = "email@domeniu..com" # Dublu punct
print(f"'{email_invalid5}' este valid: {valideaza_email(email_invalid5)}")

email_invalid6 = "email@domeniu.c" # TLD prea scurt
print(f"'{email_invalid6}' este valid: {valideaza_email(email_invalid6)}")

email_invalid7 = "invalid email@"
print(f"'{email_invalid7}' este valid: {valideaza_email(email_invalid7)}")