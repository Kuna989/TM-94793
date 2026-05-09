from MainPage import MainPage
import datetime

def run_engineered_test():
    """
    SCENARIUSZ TESTOWY (Layer 3): Czysta logika biznesowa.
    Tester nie operuje na selektorach, tylko na akcjach MainPage.
    """
    print(">>> ZADANIE 6.3: TEST SCENARIUSZA W ARCHITEKTURZE POM <<<")

    # 1. Inicjalizacja (Zauważ: tester nie musi ładować JSON-a ręcznie)
    main_page = MainPage()

    # 2. Definicja kroków scenariusza
    execution_steps = []

    # KROK 1: Sprawdzenie gotowości ekranu
    step1 = main_page.get_main_title_status()
    execution_steps.append(step1)

    # KROK 2: Próba nawigacji do sekcji dodawania
    step2 = main_page.navigate_to_add_content()
    execution_steps.append(step2)

    # KROK 3: Symulacja wyszukiwania (Action with parameter)
    step3 = main_page.perform_search_action("Automatyzacja Mobilna")
    execution_steps.append(step3)

    # 3. Wyświetlanie przebiegu testu i zapis do audytu
    print("\n--- PRZEBIEG SCENARIUSZA TESTOWEGO ---")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("64_pom_audit.log", "w", encoding="utf-8") as audit_file:
        audit_file.write(f"AUDYT WYKONANIA POM - {timestamp}\n")
        audit_file.write("="*40 + "\n")

        for i, step in enumerate(execution_steps, 1):
            formatted_step = f"KROK {i}: {step}"
            print(formatted_step)
            audit_file.write(formatted_step + "\n")

    print("\n" + "\033[92m" + "[OK] Scenariusz wykonany. Log audytu zapisany w 64_pom_audit.log" + "\033[0m")

if __name__ == "__main__":
    run_engineered_test()
 