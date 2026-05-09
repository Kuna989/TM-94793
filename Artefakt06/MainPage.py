from BasePage import BasePage

class MainPage(BasePage):
    """
    PAGE OBJECT (Layer 2): Reprezentuje konkretny ekran aplikacji (Główny ekran ApiDemos).
    Dziedziczy po BasePage, zyskując dostęp do słownika selektorów.
    """

    def __init__(self):
        # Wywołujemy konstruktor klasy bazowej
        super().__init__()
        print("[MAIN_PAGE] Ekran główny zainicjalizowany.")

    def navigate_to_add_content(self):
        """
        Logika biznesowa: wejście w sekcję dodawania treści.
        Zamiast operować na ID, metoda mówi CO chcemy zrobić.
        """
        selector = self.find_id("ADD")
        if selector:
            # W prawdziwym Appium tu byłoby: self.driver.find_element(By.ID, selector).click()
            return f"SUKCES: Wykonano kliknięcie w element UI o ID: '{selector}'"
        return "BŁĄD: Nie można nawigować - brak selektora 'ADD' w mapie!"

    def get_main_title_status(self):
        """
        Logika biznesowa: sprawdzenie statusu nagłówka.
        """
        selector = self.find_id("TITLE")
        if selector:
            return f"SUKCES: Odnaleziono nagłówek strony (ID: {selector}). Status: Widoczny."
        return "INFORMACJA: Element 'TITLE' nie jest zdefiniowany dla tego ekranu."

    def perform_search_action(self, query):
        """
        Logika biznesowa: symulacja wyszukiwania.
        """
        selector = self.find_id("SEARCH_BUTTON")
        if selector:
            return f"SUKCES: Wpisano '{query}' do pola {selector} i zatwierdzono."
        return f"BŁĄD: Przycisk wyszukiwania nie został zmapowany."

# TEST JEDNOSTKOWY OBIEKTU (Weryfikacja przez studenta)
if __name__ == "__main__":
    main_page = MainPage()
    print("-" * 30)
    print(main_page.navigate_to_add_content())
    print(main_page.get_main_title_status())
    print("-" * 30)
 