import os
import xml.etree.ElementTree as ET

def analyze_manifest():
    print(">>> ZADANIE 5.2: ANALIZA MANIFESTU (POŁĄCZENIE Z ARTEFAKTEM 02) <<<")

    # Twoje sprawdzone ścieżki
    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    output_path = "52_inspection.log"

    if not os.path.exists(manifest_path):
        print(f"BŁĄD: Nie znaleziono manifestu w: {manifest_path}")
        return

    try:
        tree = ET.parse(manifest_path)
        root = tree.getroot()

        # Pobieramy nazwę paczki (niezbędna do Appium w przyszłości)
        package = root.attrib.get('package')

        # Wyciągamy uprawnienia (Permissions)
        permissions = [elem.attrib.get('{http://schemas.android.com/apk/res/android}name') 
                       for elem in root.findall('uses-permission')]

        # Wyciągamy aktywności (Activities)
        activities = [elem.attrib.get('{http://schemas.android.com/apk/res/android}name') 
                      for elem in root.findall('.//activity')]

        report = [
            "=== ARTEFAKT 5.2: RAPORT ANALIZY SYSTEMOWEJ ===",
            f"Pakiet główny: {package}",
            f"Liczba Activity: {len(activities)}",
            "\nKluczowe Uprawnienia (Co aplikacja chce robić?):"
        ]
        # Dodajemy listę uprawnień (pierwsze 5, żeby log był czytelny)
        report.extend([f"- {p}" for p in permissions[:5]])

        final_report = "\n".join(report)
        print("\033[92m" + final_report + "\033[0m")

        with open(output_path, 'w') as f:
            f.write(final_report)

        print(f"\n[OK] Sukces! Artefakt zapisany jako: {output_path}")

    except Exception as e:
        print(f"BŁĄD PODCZAS ANALIZY: {e}")

if __name__ == "__main__":
    analyze_manifest()

 