import xml.etree.ElementTree as ET
import glob
import json
import os
ANDROID_NS = '{http://schemas.android.com/apk/res/android}'
def mine_ids(path):
    report = []
    for file in glob.glob(path + "/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file)
            root = tree.getroot()

            for elem in root.iter():
                res_id = elem.get(ANDROID_NS + 'id')
                if res_id:
                    report.append({
                        "file": os.path.basename(file),
                        "id": res_id.split('/')[-1],
                        "tag": elem.tag
                    })

        except ET.ParseError:
            continue
    return report
if __name__ == "__main__":
    data = mine_ids("../Artefakt02/decompiled_apk/res/layout")
    with open("miner_report.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"[OK] Extracted {len(data)} IDs")

 