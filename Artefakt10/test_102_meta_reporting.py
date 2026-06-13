import pytest
import allure

@allure.epic("Epic: Platforma Edukacyjna Artefakt")
@allure.feature("Feature:Moduł Kursy i Lekcje")
class TestCourseFlow:

    @allure.story("Story 1: Przeglądanie listy lekcji")
    @allure.title("Weryfikacja ładowania lekcji w Bloku 10")
    @allure.severity(allure.severity_level.NORMAL)
    def test_lesson_load(self):
        with allure.step("Krok 1: Otwarcie katalogu kursów"):
            # Symulacja akcji
            allure.attach("Użytkownik wszedł na /courses", name="Log Systemowy")

        with allure.step("Krok 2: Wybór lekcji 'Automatyzacja'"):
            assert True

    @allure.story("Story 2: Przeglądanie listy lekcji")
    @allure.title("Błąd: Brak uprawnień do lekcji premium")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_lesson_access_denied(self):
        with allure.step("Krok 1: Próba wejścia do lekcji bez logowania"):
            error_code = 403
            assert error_code == 403
            allure.attach("Access Denied: Please Login", name="Server Response")
 