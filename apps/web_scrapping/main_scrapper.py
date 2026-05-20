# %%
from playwright.sync_api import sync_playwright
import json



def scrape_laczynaspilka(sezon, liga, runda, kolejka):
    """
    Pobiera wybraną przez nas tabele ligową do pliku JSON
    Funkcja symuluje użytkownika biblioteką playwright przez to cały proces chwile zajmuje
    WSZYSTKIE ARGUMENTY MUSZĄ BYĆ TAK SAMO WPISANE JAK NA STRONIE LACZYNASPILKA
    ARGS:
        sezon (str) - np.2025/2026
        liga (str) - np. Ekstraklasa
        runda (str) - np. Wiosenna
        kolejka (str) = np. 33


    """
    with sync_playwright() as p:
        browser = p.chromium.launch(
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

        print("Ładuję główną stronę rozgrywek w tle...")
        page.goto("https://www.laczynaspilka.pl/rozgrywki", wait_until="networkidle")

        try:
            page.locator("text=Sezon").first.wait_for(state="visible", timeout=15000)

            print("Sprawdzam i klikam ciasteczka...")
            try:
                ciastka = page.locator("button:has-text('Zaakceptuj wszystkie')")
                ciastka.wait_for(state="visible", timeout=6000)
                ciastka.click(force=True)
                print("Cookies accepted")
            except Exception:
                print("Ciasteczka nie wyskoczyły")

            print("Zaczęło zmieniać filtry")

            def wybierz_parametr(nazwa, wartosc):
                print(f" -> Ustawiam: {nazwa} = {wartosc}")
                pole = page.get_by_text(nazwa, exact=True).first
                pole.locator("..").click(force=True)
                page.wait_for_timeout(1000)

                page.get_by_text(wartosc, exact=True).last.click(force=True)
                page.wait_for_timeout(2000)

            wybierz_parametr("Sezon", sezon)
            wybierz_parametr("Liga", liga)
            wybierz_parametr("Runda", runda)
            wybierz_parametr("Kolejka", kolejka)

            print("Pobieram Tabele")
            page.wait_for_timeout(1000)

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
            print(f"WYSTĄPIŁ BŁĄD SZUKAJ HEADLESS PNG")
            page.screenshot(path="error_headless.png")
            browser.close()
            raise e

#PRZYKŁADOWE UŻYCIE
dane_json = scrape_laczynaspilka(
    sezon="2025/2026",
    liga="Ekstraklasa",
    runda="Wiosenna",
    kolejka="33 (bieżąca)"
)

print(json.dumps(dane_json, indent=4, ensure_ascii=False))