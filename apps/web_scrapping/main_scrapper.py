# %%
from playwright.sync_api import sync_playwright
import json
import re


def scrape_laczynaspilka(liga, runda=None, kolejka=None, wojewodztwo=None, klasa=None, grupa=None):
    """
        Pobiera i zapisuje tabele ligowe z strony PZPN

        Funkcja wykorzystuje bibliotekę Playwright do symulowania prawdziwej przeglądarki
        Google Chrome w trybie w tle (headless). Sezon rozgrywek jest ustawiony na sztywno na "2025/2026".
        Logika funkcji automatycznie wybiera ścieżkę klikania filtrów w zależności od
        głównego argumentu `liga` dlatego możliwa jest do wyboru tylko ekstraklasa i Niższe Ligi

        Args:
            liga (str): Główna kategoria rozgrywek ("Ekstraklasa" lub "Niższe ligi" na innych nie testowane).
            runda (str, optional): Nazwa rundy (np. "Wiosenna", "Jesienna").
                                   [Wymagane dla ścieżki: "Ekstraklasa"]
            kolejka (str, optional): Numer kolejki, dokładnie jak na stronie (np. "33 (bieżąca)").
                                     [Wymagane dla ścieżki: "Ekstraklasa"]
            wojewodztwo (str, optional): Nazwa województwa (np. "dolnośląskie").
                                         [Wymagane dla ścieżki: "Niższe ligi"]
            klasa (str, optional): Klasa rozgrywkowa (np. "Klasa B").
                                   [Wymagane dla ścieżki: "Niższe ligi"]
            grupa (str, optional): Nazwa przypisanej grupy (np. "Wałbrzych: Klasa B").
                                   Nie wymaga wpisywania kropek na końcu, skrypt sam
                                   dopasuje najdłuższy ciąg znaków.
                                   [Wymagane dla ścieżki: "Niższe ligi"]

        Returns:
            list[dict]: Lista słowników, gdzie każdy słownik to jeden wiersz (klub) w tabeli.
                        Klucze słownika to m.in.: "Pozycja", "Druzyna", "Mecze", "Punkty",
                        "Wygrane", "Remisy", "Porazki", "Gole_Zdobyte", "Gole_Stracone", "Bilans".

        Raises:
            ValueError: Jeśli użytkownik nie poda wszystkich parametrów wymaganych dla danej ligi.
            Exception: Zwraca błąd wykonania i automatycznie tworzy zrzut ekranu error_headless i wiecie
            jak się wywróci dajcie znać na mess to będę konntynuował moje dalsze walki z tym cloudflarem
        """

    sezon = "2025/2026"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=True,
            slow_mo=300,
            args=["--disable-blink-features=AutomationControlled"]
        )

        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        )

        context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        page = context.new_page()

        print("Ładuję główną stronę w tle (inicjalizacja sesji)...")
        page.goto("https://www.laczynaspilka.pl/", wait_until="networkidle")

        try:
            print("Sprawdzam i klikam ciasteczka...")
            ciastka = page.locator("button:has-text('Zaakceptuj wszystkie')")
            ciastka.wait_for(state="visible", timeout=6000)
            ciastka.click(force=True)
            print(" -> Ciasteczka ZAŁATWIONE!")
            page.wait_for_timeout(1000)
        except Exception:
            print(" -> Brak ciasteczek, jedziemy dalej.")

        print("Wymuszam przejście do zakładki Rozgrywki...")
        page.evaluate('''() => {
            let linki = document.querySelectorAll("a[href='/rozgrywki'], a[href='https://www.laczynaspilka.pl/rozgrywki']");
            if (linki.length > 0) {
                linki[0].click();
            } else {
                window.location.href = '/rozgrywki';
            }
        }''')

        try:
            page.get_by_text("Sezon", exact=True).locator("visible=true").first.wait_for(state="visible", timeout=15000)

            print(f"Zmieniam filtry dla ścieżki: {liga}...")

            def wybierz_parametr(nazwa, wartosc):
                print(f" -> Ustawiam: {nazwa} = {wartosc}")

                regex_nazwa = re.compile(f"^\\s*{nazwa}\\s*$")
                pole = page.get_by_text(regex_nazwa).locator("visible=true").first
                opcja = page.get_by_text(wartosc).locator("visible=true").last

                rozwinieto = False
                for _ in range(4):
                    pole.locator("..").click(force=True)
                    page.wait_for_timeout(1000)

                    if opcja.is_visible():
                        rozwinieto = True
                        break

                    pole.click(force=True)
                    page.wait_for_timeout(1000)

                    if opcja.is_visible():
                        rozwinieto = True
                        break

                if not rozwinieto:
                    print(
                        f" [!] UWAGA: Nie udało się bezbłędnie rozwinąć listy '{nazwa}'. Próbuję kliknąć opcję siłowo.")

                opcja.click(force=True)
                page.wait_for_timeout(2000)

                # --- GŁÓWNA LOGIKA WYBORU ---

            wybierz_parametr("Sezon", sezon)
            wybierz_parametr("Liga", liga)

            if liga == "Ekstraklasa":
                if not runda or not kolejka:
                    raise ValueError("Dla Ekstraklasy musisz podać parametry: runda, kolejka!")

                wybierz_parametr("Runda", runda)
                wybierz_parametr("Kolejka", kolejka)

            elif liga == "Niższe ligi":
                if not wojewodztwo or not klasa or not grupa:
                    raise ValueError("Dla niższych lig musisz podać parametry: wojewodztwo, klasa, grupa!")

                wybierz_parametr("Województwa", wojewodztwo)
                wybierz_parametr("Klasa rozgrywkowa", klasa)
                wybierz_parametr("Grupa", grupa)

            else:
                print(f"Ostrzeżenie: Brak zdefiniowanej ścieżki dla ligi '{liga}'.")

            # ---------------------------

            print("Czekam na załadowanie się tabeli...")
            page.wait_for_timeout(2000)

            print("Pobieram wygenerowaną tabelę...")
            tabela_danych = page.evaluate(r'''() => {
                let wyniki = [];
                let wiersze = document.querySelectorAll('div.row-hover');

                for (let wiersz of wiersze) {
                    let text = wiersz.innerText || "";
                    let komorki = text.split('\n').map(t => t.trim()).filter(t => t !== '');

                    if (komorki.length === 0 || komorki.includes('Pozycja')) continue;

                    if (komorki.length >= 9) {
                        let k = komorki.length;
                        wyniki.push({
                            "Pozycja": komorki[0],
                            "Druzyna": komorki.slice(1, k - 8).join(" "),
                            "Mecze": komorki[k - 8],
                            "Punkty": komorki[k - 7],
                            "Wygrane": komorki[k - 6],
                            "Remisy": komorki[k - 5],
                            "Porazki": komorki[k - 4],
                            "Gole_Zdobyte": komorki[k - 3],
                            "Gole_Stracone": komorki[k - 2],
                            "Bilans": komorki[k - 1]
                        });
                    }
                }
                return wyniki;
            }''')

            browser.close()
            return tabela_danych

        except Exception as e:
            print(f"\n!!! WYSTĄPIŁ BŁĄD !!! Robię zrzut ekranu do pliku 'error_headless.png'...")
            page.screenshot(path="error_headless.png")
            browser.close()
            raise e

#TESTY UŻYCIA

wybrana_liga = "Niższe ligi"  # Tutaj wpisujecie wybraną lige

if wybrana_liga == "Ekstraklasa":
    dane_json = scrape_laczynaspilka(
        liga="Ekstraklasa",
        runda="Wiosenna",
        kolejka="33 (bieżąca)"
    )
else:
    dane_json = scrape_laczynaspilka(
        liga="Niższe ligi",
        wojewodztwo="dolnośląskie",
        klasa="Klasa B",
        grupa="Wałbrzych: Klasa B"
    )

nazwa_pliku = f"tabela_{wybrana_liga.replace(' ', '_').lower()}.json"

with open(nazwa_pliku, "w", encoding="utf-8") as plik:
    json.dump(dane_json, plik, indent=4, ensure_ascii=False)

print(f"Dane pobrano do pliku: {nazwa_pliku}")