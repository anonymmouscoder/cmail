import time
import requests
import json

logo = r"""
#  _____                             _____ 
# ( ___ )---------------------------( ___ )
#  |   |                             |   | 
#  |   |   ____                 _ _  |   | 
#  |   |  / ___|_ __ ___   __ _(_) | |   | 
#  |   | | |   | '_ ` _ \ / _` | | | |   | 
#  |   | | |___| | | | | | (_| | | | |   | 
#  |   |  \____|_| |_| |_|\__,_|_|_| |   |  
#  |   |                             |   | 
#  |   |                             |   | 
#  |   |   Auteur: Aliou - V0.0.1    |   |  
#  |___|                             |___| 
# (_____)---------------------------(_____)

"""
aliou = r"""
⠀⢠⣶⣿⣿⣗⡢⠀⠀⠀⠀⠀⠀⢤⣒⣿⣿⣷⣆⠀⠀
⠀⠋⠉⠉⠙⠻⣿⣷⡄⠀⠀⠀⣴⣿⠿⠛⠉⠉⠉⠃⠀
⠀⠀⢀⡠⢤⣠⣀⡹⡄⠀⠀⠀⡞⣁⣤⣠⠤⡀⠀⠀⠀
⢐⡤⢾⣿⣿⢿⣿⡿⠀⠀⠀⠀⠸⣿⣿⢿⣿⣾⠦⣌⠀
⠁⠀⠀⠀⠉⠈⠀⠀⣸⠀⠀⢰⡀⠀⠈⠈⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⣀⡔⢹⠀⠀⢸⠳⡄⡀⠀⠀⠀⠀⠀⠀          
⠸⡦⣤⠤⠒⠋⠘⢠⡸⣀⣀⡸⣠⠘⠉⠓⠠⣤⢤⡞⠀
⠀⢹⡜⢷⣄⠀⣀⣀⣾⡶⢶⣷⣄⣀⡀⢀⣴⢏⡾⠁⠀
⠀⠀⠹⡮⡛⠛⠛⠻⠿⠥⠤⠽⠿⠛⠛⠛⣣⡾⠁⠀⠀
⠀⠀⠀⠙⢄⠁⠀⠀⠀⣄⣀⡄⠀⠀⠀⢁⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠂⠀⠀⠀⢸⣿⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                               
                                                                    
"""

EMAIL_ICON = "✉"
SUCCESS_ICON = "✔"
FAILURE_ICON = "✘"

def send_email(to, subject, message):
    url = "https://codingmailer.onrender.com/send-email"
    data = {"to": to, "subject": subject, "message": message}
    payload = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=payload, headers=headers)

    if response.ok:
        return True, f"{SUCCESS_ICON} E-mail envoyé avec succès."
    else:
        error_message = response.json().get("message", "Erreur lors de l'envoi de l'e-mail.")
        return False, f"{FAILURE_ICON} Erreur : {error_message}"

def display_menu():
    lines = [
        f"\033[1;32m{logo}\033[0m",
        "\033[1;36m1. \033[1;33mEnvoyer un e-mail\033[0m",
        "\033[1;36m2. \033[1;33mÀ propos du développeur\033[0m",
        "\033[1;36m3. \033[1;33mQuitter\033[0m"
    ]

    for line in lines:
        print(line)
        time.sleep(0.9)

def send_email_option():
    print("\033[1;31m»»————-　★　————-««\033[0m")
    print("\033[1;36mOption 1 : Envoyer un e-mail\033[0m")

    to = input("\033[1;33mEntrez l'e-mail du destinataire\033[0m: ")
    subject = input("\033[1;33mEntrez le sujet de l'e-mail\033[0m: ")
    message = input("\033[1;33mEntrez le message de l'e-mail\033[0m: ")

    print(f"\033[1;36m{EMAIL_ICON} Envoi de l'e-mail... \033[0m", end='', flush=True)

    for progress in range(1, 6):
        time.sleep(0.5)
        print(f"\033[1;32m{'.'}\033[0m", end='', flush=True)

    success, result_message = send_email(to, subject, message)

    print("\r\033[K", end='', flush=True)

    if success:
        print(f"\033[1;32m{SUCCESS_ICON} " + result_message + "\033[0m")
    else:
        print(f"\033[1;31m{FAILURE_ICON} " + result_message + "\033[0m")

def about_developer_option():
    lines = [
        "\033[1;31m»»————-　★　————-««\033[0m",
        "\033[1;36m2 : À propos du développeur\033[0m",
        f"\033[1;36m{aliou}\033[0m",
        "Cmail est un outil Python qui sert à envoyer des e-mails à la base développé par @A_liou sur Telegram.",
        "Rejoignez notre chaîne Telegram pour plus de contenu : https://t.me/codingtutotech"
    ]

    for line in lines:
        print(line)
        time.sleep(0.5)


if __name__ == "__main__":
    display_menu()

    while True:
        choice = input("\033[1;33mSélectionnez une option (1-3)\033[0m: ")

        if choice == '1':
            send_email_option()
        elif choice == '2':
            about_developer_option()
        elif choice == '3':
            print("\033[1;32mAu revoir !\033[0m")
            break
        else:
            print("\033[1;31mOption invalide. Veuillez sélectionner une option valide.\033[0m")
