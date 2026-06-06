import re
import os

def find_secrets(strings_path="../Artefakt02/decompiled_apk/res/values/strings.xml"):
    print(f">>> SKANOWANIE ZASOBÓW: {strings_path} <<<")
    if not os.path.exists(strings_path):
        print(f"BŁĄD: Nie odnaleziono pliku zasobów: {strings_path}")
        return
    try:
        with open(strings_path, 'r', encoding='utf-8') as f:
            content = f.read()
        patterns = {
            "IP_Address":       r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
            "URL_Endpoint":     r'https?://[^\s<>"]+|www\.[^\s<>"]+',
            "Potential_Secret": r'(?i)key|token|secret|password|auth|api_key',
            "API_Key_Format":   r'[a-zA-Z0-9_-]{20,}'
        }
        results = []
        for label, pattern in patterns.items():
            matches = re.findall(pattern, content)
            for match in set(matches):
                if len(match) > 3 and not match.endswith('.xml'):
                    results.append(f"[{label}] -> {match}")
        output_file = "82_secrets_found.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("=== RAPORT ZNALEZIONYCH WRAŻLIWYCH DANYCH ===\n")
            if results:
                f.write("\n".join(results))
            else:
                f.write("Nie znaleziono oczywistych wycieków danych w strings.xml.")
        print(f"[INFO] Analiza zakończona. Znaleziono {len(results)} potencjalnych punktów wycieku.")
        for r in results:
            print(f"  {r}")
    except Exception as e:
        print(f"BŁĄD PODCZAS SKANOWANIA: {e}")

if __name__ == "__main__":
    find_secrets()