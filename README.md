# Futbolowo
![Strona Główna](/IMG/strona.png?raw=true "Strona Główna")

### O serwisie
Naszym głównym celem była pomoc przeciętnemu urzytkownikowi przy orientowaniu się w wynikach meczy i przekazywaniu wiadomości bezpośrednio od prowadzących zespołów niższych lig

## Jak uruchomić

_Przykład uruchomienia na ubuntu._

1. zainstaluj wymagane oprogramowanie
    ```sh
    sudo apt install python3 python3-pip git
    ```
2. Sklonuj repozytorium
    ```sh
    git clone https://github.com/github_username/repo_name.git
    ```
3. Stwórz środowisko wirtualne python i je aktywuj
    ```sh
    python3 -m venv myenv
    ```
    ```sh
    source myenv/bin/activate
    ```
4. Wejdź w folder z projektem
    ```sh
    cd Futbolowo
    ```
5. Zainstaluj wymaganie pakiety
    ```sh
    pip install -r requirements.txt
    ```
6. Uruchom program
    ```sh
    python manage.py runserver
    ```