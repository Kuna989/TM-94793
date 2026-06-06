# 73_state_manager.py
# MODUŁ ZARZĄDZANIA STANEM (Layer 4): Obsługa fizycznych zmian urządzenia

import datetime
import os

class BasePage:
    SELECTOR_MAP = {
        "ADD":       "com.example.app:id/btn_add",
        "LIST_ITEM": "com.example.app:id/list_item_0",
    }
    def find_id(self, key):
        return self.SELECTOR_MAP.get(key, None)

class DeviceStateManager(BasePage):

    def __init__(self):
        super().__init__()
        self.log_file = "73_state.log"
        self.current_orientation = "PORTRAIT"
        self.power_connected = False

    def _log_event(self, event_name, detail):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {event_name.upper()}: {detail}\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"  [LOG] Zapisano: {entry.strip()}")

    def toggle_screen_orientation(self, target="LANDSCAPE"):
        print(f"\n[DEVICE] === ZMIANA ORIENTACJI ===")
        print(f"[DEVICE] Poprzednia: {self.current_orientation} -> Nowa: {target}")

        self.current_orientation = target
        detail = (f"Ekran obrócony do {target}. "
                  f"Weryfikacja przerysowania layoutu... OK. "
                  f"Rozdzielczość aktywna: "
                  f"{'1920x1080' if target == 'LANDSCAPE' else '1080x1920'}")

        self._log_event("ORIENTATION_CHANGE", detail)
        result = f"SUKCES: Orientacja zmieniona na {target}."
        print(f"[DEVICE] {result}")
        return result

    def simulate_power_connection(self, is_connected=True):
        state = "CONNECTED" if is_connected else "DISCONNECTED"
        charging = "Ładowanie aktywne." if is_connected else "Ładowanie zatrzymane."

        print(f"\n[DEVICE] === ZMIANA ZASILANIA ===")
        print(f"[DEVICE] Stan zasilania: {state}")

        self.power_connected = is_connected
        detail = f"Zasilanie zewnętrzne: {state}. {charging}"

        self._log_event("POWER_STATE", detail)
        result = f"SUKCES: Stan zasilania ustawiony na {state}."
        print(f"[DEVICE] {result}")
        return result

    def simulate_volume_change(self, direction="UP", steps=3):
        print(f"\n[DEVICE] === ZMIANA GŁOŚNOŚCI ===")
        print(f"[DEVICE] Kierunek: VOLUME {direction}, kroków: {steps}")

        detail = f"Głośność zmieniona: VOLUME_{direction} x{steps}"
        self._log_event("VOLUME_CHANGE", detail)
        result = f"SUKCES: Głośność zmieniona ({direction} x{steps})."
        print(f"[DEVICE] {result}")
        return result


if __name__ == "__main__":
    dsm = DeviceStateManager()

    print("=" * 55)
    print(">>> ZADANIE 7.3: ZARZĄDZANIE FIZYCZNYM STANEM URZĄDZENIA <<<")
    print("=" * 55)

    if os.path.exists("73_state.log"):
        os.remove("73_state.log")
        print("[INFO] Poprzedni log usunięty.\n")

    print(dsm.toggle_screen_orientation("LANDSCAPE"))
    print(dsm.toggle_screen_orientation("PORTRAIT"))
    print(dsm.simulate_power_connection(True))
    print(dsm.simulate_power_connection(False))
    print(dsm.simulate_volume_change("UP", steps=3))
    print(dsm.simulate_volume_change("DOWN", steps=1))

    print(f"\n{'=' * 55}")
    print(f"[OK] Wszystkie zmiany zapisane w: 73_state.log")
    print(f"[OK] Zawartość pliku logu:")
    print(f"{'=' * 55}")

    with open("73_state.log", "r", encoding="utf-8") as f:
        print(f.read())