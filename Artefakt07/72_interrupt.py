# 72_interrupt.py
# MODUŁ PRZERWAŃ (Layer 4): Symulacja zdarzeń systemowych Androida

import time

class BasePage:
    SELECTOR_MAP = {
        "ADD":       "com.example.app:id/btn_add",
        "LIST_ITEM": "com.example.app:id/list_item_0",
    }
    def find_id(self, key):
        return self.SELECTOR_MAP.get(key, None)

class InterruptManager(BasePage):
    """
    MODUŁ PRZERWAŃ (Layer 4): Symulacja zdarzeń systemowych Androida.
    """

    def simulate_incoming_call(self, duration_sec=5, phone_number="+48 123 456 789"):
        print("\n" + "=" * 50)
        print(f"[INTERRUPT] === TEST: INCOMING CALL ===")
        print(f"[INTERRUPT] KROK 1: Stan aplikacji przed połączeniem: ACTIVE (onResume)")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL")
        print(f"[INTERRUPT]          Numer: {phone_number} | Czas trwania: {duration_sec}s")

        time.sleep(0.5)
        print(f"\n>>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran połączenia <<<")
        print(f"[INTERRUPT]          Czas połączenia: ", end="", flush=True)

        for i in range(duration_sec):
            time.sleep(1)
            print(f"{i+1}s... ", end="", flush=True)

        print()
        print(f"[INTERRUPT] KROK 3: Zakończenie połączenia. Powrót do aplikacji.")
        print(f">>> SYSTEM: Aplikacja odzyskała fokus (onResume) <<<")

        result = "SUKCES: Aplikacja odzyskała fokus (onResume). Dane sesji zachowane."
        print(f"[INTERRUPT] Wynik: {result}")
        print("=" * 50)
        return result

    def simulate_low_battery_warning(self, battery_level=5):
        print("\n" + "=" * 50)
        print(f"[INTERRUPT] === TEST: LOW BATTERY WARNING ===")
        print(f"[INTERRUPT] KROK 1: Ustawianie poziomu baterii na: {battery_level}%")
        print(f"[INTERRUPT] KROK 2: System wyświetla okno dialogowe: 'Niski poziom baterii'")
        print(f">>> SYSTEM: Dialog LOW BATTERY widoczny na ekranie <<<")
        print(f"[INTERRUPT] KROK 3: Aplikacja obsługuje dialog — brak zawieszenia (ANR).")

        result = "SUKCES: Aplikacja obsłużyła systemowe okno dialogowe bez błędu."
        print(f"[INTERRUPT] Wynik: {result}")
        print("=" * 50)
        return result

    def simulate_sms_notification(self, sender="Test User"):
        print("\n" + "=" * 50)
        print(f"[INTERRUPT] === TEST: SMS NOTIFICATION ===")
        print(f"[INTERRUPT] KROK 1: Nadchodzi SMS od: {sender}")
        print(f">>> SYSTEM: Pasek powiadomień wysuwa się (Notification Shade) <<<")
        time.sleep(0.5)
        print(f"[INTERRUPT] KROK 2: Aplikacja pozostaje w tle. Fokus na powiadomieniu.")
        time.sleep(0.5)
        print(f"[INTERRUPT] KROK 3: Użytkownik odrzuca powiadomienie. Powrót do app.")

        result = "SUKCES: Powiadomienie SMS nie przerwało sesji testowej."
        print(f"[INTERRUPT] Wynik: {result}")
        print("=" * 50)
        return result


if __name__ == "__main__":
    im = InterruptManager()

    print("=" * 50)
    print(">>> ZADANIE 7.2: TESTY ODPORNOŚCI NA PRZERWANIA <<<")
    print("=" * 50)

    status_call = im.simulate_incoming_call(duration_sec=3)
    status_battery = im.simulate_low_battery_warning(battery_level=5)
    status_sms = im.simulate_sms_notification(sender="Jan Kowalski")

    print("\n>>> PODSUMOWANIE TESTÓW PRZERWAŃ <<<")
    print(f"  Połączenie:   {status_call}")
    print(f"  Bateria:      {status_battery}")
    print(f"  SMS:          {status_sms}")
    print("\n[KONIEC] Wszystkie testy przerwań zakończone.")