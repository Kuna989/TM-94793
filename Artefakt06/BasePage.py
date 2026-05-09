import json
import os

class BasePage:
    """
    KLASA BAZOWA (Layer 1): Odpowiada za dostęp do zasobów i współdzielone 
    mechanizmy dla wszystkich ekranów aplikacji.
    """

    def __init__(self, selectors_path="../Artefakt05/53_selectors.json"):
        """
        Konstruktor wczytuje mapę selektorów wygenerowaną w procesie 
        automatycznego miningu (Blok 5).
        """
        self.selectors_path = selectors_path
        self.selectors = {}
        self._load_selectors()

    def _load_selectors(self):
        """
        Prywatna metoda parsująca plik JSON. 
        Implementuje podstawową obsługę błędów (Error Handling).
        """
        if not os.path.exists(self.selectors_path):
            print(f"BŁĄD INŻYNIERSKI: Brak pliku zasobów w {self.selectors_path}")
            return

        try:
            with open(self.selectors_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.selectors = data.get("selectors", {})
                print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(self.selectors)} elementów.")
        except Exception as e:
            print(f"BŁĄD PARSOWANIA: {e}")

    def find_id(self, business_key):
        """
        Zwraca Resource ID na podstawie klucza biznesowego.
        Jeśli klucz nie istnieje, zwraca None - pozwala to uniknąć 
        twardych błędów aplikacji podczas testu.
        """
        resource_id = self.selectors.get(business_key)
        if not resource_id:
            print(f"OSTRZEŻENIE: Brak klucza '{business_key}' w mapie selektorów!")
        return resource_id

# TEST JEDNOSTKOWY MODUŁU (Tylko do weryfikacji)
if __name__ == "__main__":
    bp = BasePage()
    # Przykładowe sprawdzenie czy system "widzi" selektor z poprzedniego bloku
    test_key = "ADD"
    print(f"Weryfikacja klucza '{test_key}': {bp.find_id(test_key)}")