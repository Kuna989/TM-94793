import os
import xml.etree.ElementTree as ET
import json

def build_ui_map():
    print(">>> ZADANIE 5.3: BUDOWA MAPY SELEKTORÓW (UI MAPPING) <<<")

    layout_dir = "../Artefakt02/decompiled_apk/res/layout/"
    output_file = "53_selectors.json"\

    ui_map = {
        "metadata": {"source": "de-compiled apk", "block": "5.3"},
        "selectors": {}
    }

    if not os.path.exists(layout_dir):
        print(f"BŁĄD: Folder layoutów nie istnieje: {layout_dir}")
        return

    # Iterujemy po plikach layoutów
    for file_name in os.listdir(layout_dir):
        if file_name.endswith(".xml"):
            try:
                tree = ET.parse(os.path.join(layout_dir, file_name))
                root = tree.getroot()

                # Szukamy wszystkich elementów z atrybutem id
                for element in root.iter():
                    res_id = element.attrib.get('{http://schemas.android.com/apk/res/android}id')
                    if res_id:
                        # Oczyszczamy ID (np. @id/button -> button)
                        clean_id = res_id.split('/')[-1]
                        # Tworzymy nazwę biznesową (np. LOGIN_BTN)
                        business_name = clean_id.upper()
                        ui_map["selectors"][business_name] = clean_id
            except:
                continue

    # Zapisujemy do JSON - to będzie nasz "mózg" dla Appium w kroku 5.5
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(ui_map, f, indent=4)

    print(f"\033[92m[OK] Zmapowano {len(ui_map['selectors'])} unikalnych elementów UI.\033[0m")
    print(f"Artefakt zapisany: {output_file}")

if __name__ == "__main__":
    build_ui_map()
 