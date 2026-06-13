import pytest
import allure
from allure_commons.types import AttachmentType

@allure.epic("Platforma Edukacyjna Artefakt")
@allure.feature("10.3: Dowody wizualne (Załączniki)")
class TestVisualEvidence:

    @allure.title("Test ze zrzutem ekranu (Symulacja)")
    def test_screenshot_on_fail(self):
        with allure.step("Krok 1: Próba kliknięcia w przycisk 'Zapisz'"):
            # Symulujemy błąd znalezienia elementu
            try:
                element_found = False
                if not element_found:
                    raise Exception("ElementNotVisibleException")
            except Exception as e:
                # TUTAJ DZIEJE SIĘ MAGIA:
                # W rzeczywistym teście byłoby: driver.get_screenshot_as_png()
                allure.attach(
                    "Tutaj byłby obraz z telefonu", 
                    name="Screenshot_Error_01", 
                    attachment_type=AttachmentType.TEXT # Zmienimy na PNG w pełnym Appium
                )
                allure.attach(
                    "JSON Error Data: {'code': 404, 'msg': 'Not Found'}", 
                    name="API_Response", 
                    attachment_type=AttachmentType.JSON
                )
                pytest.fail(f"Test padł, ale mamy dowody! Log: {e}")

    @allure.title("Załączanie pliku tekstowego (Logi)")
    def test_log_attachment(self):
        allure.attach("DEBUG: Urządzenie podpięte, port 4723 aktywny.", name="Device Log", attachment_type=AttachmentType.TEXT)
        assert True
 