import xml.etree.ElementTree as ET
import os
from xml.dom import minidom

def save_pretty_xml(element, filename):
    raw_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(raw_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(pretty_xml)
    print(f"[SUCCESS] Wygenerowano czytelny raport: {filename}")

def scan_manifest_for_risks(input_path="../Artefakt02/decompiled_apk/AndroidManifest.xml"):
    print(f">>> URUCHAMIANIE AUDYTU: {input_path} <<<")
    if not os.path.exists(input_path):
        print(f"BŁĄD KRYTYCZNY: Nie znaleziono pliku manifestu w: {input_path}")
        print("Upewnij się, że Blok 2 (Dekompilacja) został wykonany poprawnie.")
        return
    try:
        tree = ET.parse(input_path)
        root = tree.getroot()
        risky_permissions = []
        is_debuggable = "false"
        dangerous_list = [
            'READ_CONTACTS',
            'WRITE_EXTERNAL_STORAGE',
            'ACCESS_FINE_LOCATION',
            'INTERNET',
            'CAMERA',
            'RECORD_AUDIO'
        ]
        for perm in root.findall('uses-permission'):
            name = perm.get('{http://schemas.android.com/apk/res/android}name')
            if name:
                short_name = name.split('.')[-1]
                if short_name in dangerous_list:
                    risky_permissions.append(name)
        application = root.find('application')
        if application is not None:
            is_debuggable = application.get(
                '{http://schemas.android.com/apk/res/android}debuggable', 'false')
        risky_root = ET.Element("SecurityAudit")
        risky_root.set("app", "ApiDemos_Security_Check")
        risky_root.set("status", "ReviewRequired")
        flags = ET.SubElement(risky_root, "Flags")
        ET.SubElement(flags, "Debuggable").text = is_debuggable
        perms_node = ET.SubElement(risky_root, "RiskyPermissions")
        for p in risky_permissions:
            ET.SubElement(perms_node, "Permission").text = p
        save_pretty_xml(risky_root, "RiskyPermission.xml")
        print(f"[INFO] Znaleziono {len(risky_permissions)} podejrzanych uprawnień.")
        if is_debuggable == "true":
            print("[⚠️ ALERT] Wykryto aktywną flagę DEBUGGABLE!")
    except Exception as e:
        print(f"BŁĄD PODCZAS PARSOWANIA: {e}")

if __name__ == "__main__":
    scan_manifest_for_risks()