import json
import os
def run_descriptive_validation():
    print(">>> ZADANIE 5.5: GENEROWANIE RAPORTU FEEDBACKU DLA DEWELOPERA <<<")

    try:
        with open("51_caps.json", "r") as f: caps = json.load(f)
        with open("53_selectors.json", "r") as f: ui_map = json.load(f)

        current_pkg = caps.get("appPackage") or caps.get("appium:appPackage")
        feedback_report = []

        # 1. Weryfikacja Pakietu
        if current_pkg == "io.appium.android.apis":
            feedback_report.append({
                "feature": "Identyfikacja Aplikacji",
                "status": "ZGODNY",
                "message": f"Pakiet {current_pkg} poprawnie zmapowany."
            })
        else:
            feedback_report.append({
                "feature": "Identyfikacja Aplikacji",
                "status": "DO POPRAWY",
                "message": f"Niezgodność pakietu. Wykryto {current_pkg}, sprawdź konfigurację manifestu."
            })

        # 2. Weryfikacja Dostępności Elementów (Klucz do precyzyjnej komunikacji)
        target_element = "ACCESSIBILITY"
        if target_element in ui_map["selectors"]:
            feedback_report.append({
                "feature": "Dostępność UI",
                "status": "ZGODNY",
                "message": f"Element {target_element} jest dostępny w layoutach."
            })
        else:
            # Tutaj student uczy się raportowania braku bez negatywnego oceniania
            feedback_report.append({
                "feature": "Dostępność UI",
                "status": "INFORMACJA",
                "message": f"Nie odnaleziono ID '{target_element}'. Sugestia: Zweryfikuj czy element nie zmienił nazwy na jedną z dostępnych: {list(ui_map['selectors'].keys())[:3]}."
            })

        # GENEROWANIE RAPORTU XML (Z opisowymi komunikatami)
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<test_report project="Appium_Audit">\n'

        print("\n--- FEEDBACK DLA TWÓRCÓW APLIKACJI ---")
        for item in feedback_report:
            print(f"[{item['status']}] {item['feature']}: {item['message']}")
            xml += f'    <issue feature="{item["feature"]}" status="{item["status"]}">{item["message"]}</issue>\n'

        xml += '</test_report>'

        with open("55_result.xml", "w", encoding="utf-8") as f:
            f.write(xml)

        print(f"\n\033[94m[INFO] Blok 5 zakończony. Raport opisowy gotowy: 55_result.xml\033[0m")
    except Exception as e:
        print(f"BŁĄD SYSTEMOWY: {e}")
if __name__ == "__main__":
    run_descriptive_validation()
 