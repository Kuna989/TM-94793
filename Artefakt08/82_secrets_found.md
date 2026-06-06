# 🛡️ RAPORT ANALIZY WYCIEKÓW (SECRETS)
**Student:** Jakub Lasinski
**Indeks:** 94793 06.06.2026

---

## 🛑 1. Trzy najbardziej groźne znaleziska (High Risk)
*Poniższe elementy wymagają natychmiastowej zmiany w kodzie źródłowym:*

1. **[URL_Endpoint] -> `http://www.example.com/lala/foobar@example.com`**
   - *Uzasadnienie:* Zawiera adres e-mail w ścieżce URL, co sugeruje wyciek danych
     użytkownika lub twardo zakodowane poświadczenia testowe.

2. **[Potential_Secret] -> `password`**
   - *Uzasadnienie:* Obecność tego słowa w `strings.xml` sugeruje, że deweloper mógł
     tam zapisać domyślne hasło do bazy lub usługi.


## 🟢 2. Trzy znaleziska typu "False Positive" (Low/No Risk)
*Poniższe elementy zostały błędnie sklasyfikowane jako zagrożenie:*

1. **[URL_Endpoint] -> `http://www.google.com`**
   - *Uzasadnienie:* To standardowy adres URL wyszukiwarki, powszechnie używany
     do testowania łączności internetowej.

2. **[API_Key_Format] -> `table_layout_1_triple_star`**
   - *Uzasadnienie:* Mimo że pasuje do wzorca długiego ciągu, jest to po prostu
     nazwa identyfikatora elementu UI (Layoutu).

3. **[API_Key_Format] -> `abc_font_family_display_3_material`**
   - *Uzasadnienie:* Jest to nazwa zasobu systemowego związanego z czcionkami
     biblioteki Material Design.

---

## 🎓 Wnioski końcowe
Automatyczne skanowanie RegEx jest skuteczne, ale wymaga **manualnej weryfikacji inżyniera**,
ponieważ skrypt nie rozumie kontekstu biznesowego aplikacji.