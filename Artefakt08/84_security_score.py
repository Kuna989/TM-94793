import json
import xml.etree.ElementTree as ET
import os

def calculate_security_score():
    print(">>> ZADANIE 8.4: OBLICZANIE SECURITY SCORE (ALGORITHM V1) <<<")
    score = 100
    deductions = []
    xml_path = "RiskyPermission.xml"
    if os.path.exists(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        debuggable = root.find(".//Debuggable").text
        if debuggable == "true":
            score -= 30
            deductions.append("[-30] Flaga Debuggable jest AKTYWNA (High Risk)")
    json_path = "83_vulnerabilities.json"
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            vulnerabilities = json.load(f)
            for v in vulnerabilities:
                if v['severity'] == "CRITICAL":
                    score -= 40
                    deductions.append(f"[-40] Krytyczna luka w {v['library']} (Critical)")
                elif v['severity'] == "HIGH":
                    score -= 20
                    deductions.append(f"[-20] Poważna luka w {v['library']} (High)")
                elif v['severity'] == "MEDIUM":
                    score -= 10
                    deductions.append(f"[-10] Średnia luka w {v['library']} (Medium)")
    final_score = max(0, score)
    with open("84_risk_score.txt", "w", encoding="utf-8") as f:
        f.write(f"FINAL SECURITY SCORE: {final_score}/100\n")
        f.write("-" * 30 + "\n")
        f.write("LISTA KAR PUNKTOWYCH:\n")
        f.write("\n".join(deductions))
    print(f"\n[📊] WYNIK KOŃCOWY: {final_score}/100")
    if final_score < 50:
        print("[❌] STATUS: REJECTED (Aplikacja niebezpieczna)")
    else:
        print("[✅] STATUS: ACCEPTED (Aplikacja dopuszczona)")

if __name__ == "__main__":
    calculate_security_score()