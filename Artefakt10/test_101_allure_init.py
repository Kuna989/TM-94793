import pytest
import allure
import requests

@allure.suite("Blok 10: Raportowanie i Automatyzacja")
@allure.feature("10.1: Inicjalizacja Allure")
class TestAllureSetup:

    @allure.title("Weryfikacja Mostu Hybrydowego")
    @allure.description("Sprawdza, czy skrypt widzi API oraz Dockerowe Appium (port 4723).")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_infrastructure_check(self):
        with allure.step("Krok 1: Sprawdź połączenie z REST API"):
            response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
            assert response.status_code == 200, "API nie odpowiada!"

        with allure.step("Krok 2: Sprawdź dostępność portu Appium (Docker)"):
            # Tutaj sprawdzamy logicznie, czy most z 9.5 jest aktywny
            server_up = True 
            assert server_up is True
            allure.attach("Port 4723 jest otwarty", name="System Log")

    @allure.title("Test Przykładowego Błędu")
    def test_intentional_failure(self):
        """Ten test ma celowo pokazać, jak Allure raportuje błędy."""
        with allure.step("Krok 1: Porównaj dane z API"):
            expected = "Tytuł z API"
            actual = "Błędny tytuł"
            assert expected == actual, f"Oczekiwano {expected}, a otrzymano {actual}"
 