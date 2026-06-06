# 71_gestures.py
# MODUŁ GESTÓW (Layer 4): Symulacja fizyki dotyku

class BasePage:
    """Klasa zastępcza – normalnie dziedziczymy z Artefakt06"""
    SELECTOR_MAP = {
        "ADD":       "com.example.app:id/btn_add",
        "LIST_ITEM": "com.example.app:id/list_item_0",
        "MENU":      "com.example.app:id/menu_button",
    }
    def find_id(self, key):
        return self.SELECTOR_MAP.get(key, None)

class GestureAutomator(BasePage):
    """
    MODUŁ GESTÓW (Layer 4): Rozszerzenie Page Objectu o fizykę dotyku.
    """

    def scroll_down_logic(self, start_y=0.8, end_y=0.2, duration_ms=1000):
        """
        Symulacja gestu SCROLL DOWN (procentowo).
        W Appium: driver.swipe(startX, startY, endX, endY, duration)
        """
        print(f"[GESTURE] === SCROLL DOWN ===")
        print(f"[GESTURE] Start Swipe: Y={start_y} -> End Y={end_y} (t={duration_ms}ms)")
        print(f"[GESTURE] Przeliczenie: start={int(start_y*100)}% ekranu, end={int(end_y*100)}% ekranu")

        if duration_ms < 200:
            result = "BŁĄD: Gest zbyt szybki - grozi brakiem reakcji UI (Flick)."
        else:
            scroll_percent = int((start_y - end_y) * 100)
            result = f"SUKCES: Przewinięto listę o {scroll_percent}% wysokości ekranu."

        print(f"[GESTURE] Wynik: {result}\n")
        return result

    def long_press_element(self, element_key, press_duration_ms=2000):
        """
        Symulacja Long Press na Resource ID.
        W Appium: TouchAction(driver).long_press(element, duration=2000).perform()
        """
        print(f"[GESTURE] === LONG PRESS ===")
        print(f"[GESTURE] Szukam elementu: '{element_key}' w mapie selektorów...")

        selector = self.find_id(element_key)

        if selector:
            print(f"[GESTURE] Znaleziono: {selector}")
            print(f"[GESTURE] Wykonuję Long Press ({press_duration_ms}ms)...")
            result = f"SUKCES: Wykonano LONG PRESS ({press_duration_ms}ms) na elemencie: {selector}"
        else:
            result = f"BŁĄD: Nie odnaleziono elementu '{element_key}' w mapie selektorów."

        print(f"[GESTURE] Wynik: {result}\n")
        return result

    def swipe_left(self, start_x=0.8, end_x=0.2, y_position=0.5, duration_ms=600):
        """
        Symulacja gestu SWIPE LEFT (np. usunięcie elementu listy).
        W Appium: driver.swipe(startX, y, endX, y, duration)
        """
        print(f"[GESTURE] === SWIPE LEFT ===")
        print(f"[GESTURE] Swipe: X={start_x} -> X={end_x}, Y={y_position} (t={duration_ms}ms)")
        result = f"SUKCES: Element przesunięty w lewo o {int((start_x - end_x)*100)}% szerokości."
        print(f"[GESTURE] Wynik: {result}\n")
        return result


if __name__ == "__main__":
    ga = GestureAutomator()
    print("=" * 50)
    print(">>> ZADANIE 7.1: TESTY FIZYKI DOTYKU <<<")
    print("=" * 50)

    # Test 1: Poprawny scroll
    ga.scroll_down_logic(start_y=0.8, end_y=0.2, duration_ms=800)

    # Test 2: Zbyt szybki gest (błąd)
    ga.scroll_down_logic(start_y=0.9, end_y=0.5, duration_ms=100)

    # Test 3: Long press na istniejący element
    ga.long_press_element("LIST_ITEM")

    # Test 4: Long press na nieistniejący element
    ga.long_press_element("NON_EXISTENT")

    # Test 5: Swipe left
    ga.swipe_left()

    print("=" * 50)
    print("[KONIEC] Wszystkie testy gestów zakończone.")
    print("=" * 50)