# Form-test

# 🏆 Automatyczne Testy Selenium – Formularz Rejestracji

## 📌 Opis projektu  
Projekt zawiera **automatyczne testy UI** dla formularza rejestracyjnego na stronie [DemoQA](https://demoqa.com/automation-practice-form).  
Testy sprawdzają **poprawność walidacji pól**, komunikaty błędów oraz kolory pól błędów.

---

### 🚀 **Technologie**  
Projekt został stworzony w oparciu o:
- **Python 3.9+**
- **Selenium WebDriver**
- **Pytest**
- **WebDriverWait**


#### ⚙️ **Instalacja**
Aby uruchomić testy lokalnie, wykonaj następujące kroki:
1️⃣ Klonowanie repozytorium
```bash
git clone https://github.com/grzegorzplowiec/Form-test.git
cd Form-tests
2️⃣ Utworzenie i aktywacja wirtualnego środowiska
bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
3️⃣ Instalacja zależności
bash
pip install -r requirements.txt
4️⃣ Uruchomienie testów
bash
pytest -m form
