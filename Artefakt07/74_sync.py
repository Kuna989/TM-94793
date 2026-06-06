# 74_sync.py
# MODUŁ SYNCHRONIZACJI (Layer 4): Inteligentne czekanie na elementy UI

import time

class BasePage:
    SELECTOR_MAP = {
        "ADD":       "com.example.app:id/btn_add",
        "LIST_ITEM": "com.example.app:id/list_item_0",
        "MENU":      "com.example.app:id/menu_button",
        "SEARCH":    "com.example.app:id/search_bar",
    }
    def find_id(self, key):
        return self.SELECTOR_MAP.get(key, None)

class WebDriverWait:
    def __init__(self, driver, timeout, poll_frequency=0.5):
        self.driver = driver
        self.timeout = timeout
        self.poll = poll_frequency
        print(f"[WebDriverWait] Inicjalizacja: timeout={timeout}s, poll={poll_frequency}s")

    def until(self, condition_fn, element_key):
        start = time.time()
        attempt = 0

        while True:
            attempt += 1
            elapsed = round(time.time() - start, 1)
            result = condition_fn(element_key)

            print(f"[WebDriverWait] Próba #{attempt} (t={elapsed}s): "
                  f"{'ZNALEZIONO' if result else 'czekam...'}")

            if result:
                return result

            if time.time() - start >= self.timeout:
                raise TimeoutError(
                    f"TIMEOUT: Element '{element_key}' nie pojawił się w ciągu {self.timeout}s!"
                )
            time.sleep(self.poll)


class SyncManager(BasePage):

    def _is_element_present(self, element_key):
        if not hasattr(self, '_start_time'):
            self._start_time = time.time()
        elapsed = time.time() - self._start_time
        if elapsed >= 1.5:
            return self.find_id(element_key)
        return None

    def wait_for_element_and_click(self, business_key, timeout=10):
        print(f"\n[SYNC] === EXPLICIT WAIT: '{business_key}' ===")

        selector = self.find_id(business_key)
        if not selector:
            return f"BŁĄD: Brak klucza '{business_key}' w mapie selektorów!"

        print(f"[SYNC] Selector: {selector}")
        print(f"[SYNC] Rozpoczynam oczekiwanie (max {timeout}s, polling co 0.5s)...")

        if hasattr(self, '_start_time'):
            del self._start_time

        start_time = time.time()

        try:
            wait = WebDriverWait(driver=self, timeout=timeout, poll_frequency=0.5)
            found_selector = wait.until(self._is_element_present, business_key)
            duration = round(time.time() - start_time, 2)
            result = f"SUKCES: Element '{found_selector}' odnaleziony i kliknięty po {duration}s."

        except TimeoutError as e:
            result = str(e)

        print(f"[SYNC] Wynik: {result}")
        return result

    def implicit_wait_bad_example(self, seconds=5):
        print(f"\n[SYNC] === IMPLICIT WAIT (ZŁA PRAKTYKA) ===")
        print(f"[SYNC] Czekam sztywno {seconds}s... (marnowanie czasu)")
        time.sleep(seconds)
        print(f"[SYNC] Koniec czekania. Czas zmarnowany bez względu na stan UI.")
        return f"Element kliknięty po sztywnym {seconds}s (nieefektywne)."


if __name__ == "__main__":
    sm = SyncManager()

    print("=" * 55)
    print(">>> ZADANIE 7.4: TESTY SYNCHRONIZACJI DYNAMICZNEJ <<<")
    print("=" * 55)

    print(sm.wait_for_element_and_click("ADD"))
    print(sm.wait_for_element_and_click("MENU"))
    print(sm.wait_for_element_and_click("NON_EXISTENT_BUTTON"))
    print(sm.implicit_wait_bad_example(seconds=2))

    print("\n" + "=" * 55)
    print("[KONIEC] Testy synchronizacji zakończone.")
    print("=" * 55)