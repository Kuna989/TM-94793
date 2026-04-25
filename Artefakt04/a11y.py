import xml.etree.ElementTree as ET
import glob
import json
def check_accessibility():
    gaps = []
    ns = '{http://schemas.android.com/apk/res/android}'
    path = "../Artefakt02/decompiled_apk/res/layout/*.xml"
    for file in glob.glob(path):
        tree = ET.parse(file)
        for elem in tree.iter():
            node_text = elem.get(f'{ns}text')
            node_desc = elem.get(f'{ns}contentDescription')
            node_id = elem.get(f'{ns}id', 'no-id')
            # Luka: Jest tekst, ale nie ma opisu (contentDescription)
            if node_text and not node_desc:
                gaps.append({
                    "file": file.split('/')[-1],
                    "id": node_id.split('/')[-1],
                    "text": node_text,
                    "issue": "Brak atrybutu contentDescription"
                })
    with open('a11y_report.json', 'w') as f:
        json.dump(gaps, f, indent=4)
    print(f"Znaleziono {len(gaps)} luk w dostępności. Raport zapisany.")

if __name__ == "__main__":
    check_accessibility()