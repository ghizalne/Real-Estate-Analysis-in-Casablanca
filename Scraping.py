from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Lancer le navigateur
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://yakeey.com/fr-ma/location/biens/casablanca?isNew=USED")

wait = WebDriverWait(driver, 10)

elements = 18
models_data = []

for idx in range(1, elements + 1):
    try:
        xpath = f'//*[@id="top-listing"]/div[2]/div[1]/div[{idx}]'
        model_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        raw_text = model_element.text
        lines = raw_text.split('\n')
        print(lines)

        # Extraction des informations de base
        type_bien = lines[0] if len(lines) > 0 else ""
        prix = lines[1].replace("•", "").strip() if len(lines) > 1 else ""
        quartier = lines[2] if len(lines) > 2 else ""
        specs_lines = lines[3:]

        superficie = ""
        chambres = "N/A"
        meuble = "Non meublé"
        sdb = "1"

        for part in specs_lines:
            clean = part.replace("•", "").strip()
            if "m²" in clean:
                superficie = clean
            elif "Chambre" in clean:
                chambres = clean
            elif "Sdb" in clean:
                sdb = clean
            elif "Meublé" in clean or "Non meublé" in clean:
                meuble = clean

        models_data.append({
            "id": idx,
            "type": type_bien,
            "prix": prix,
            "quartier": quartier,
            "ville": "Casablanca",
            "superficie": superficie,
            "chambres": chambres,
            "sdb": sdb,
            "meublé": meuble
        })

    except Exception as e:
        print(f"Erreur lors de l'extraction du modèle {idx} : {e}")

driver.quit()

# Convertir en DataFrame
df = pd.DataFrame(models_data)

# Sauvegarder dans un fichier Excel
df.to_excel("annonces_maisons.xlsx", index=False)

print("Fichier Excel sauvegardé sous 'annonces_casablanca.xlsx'")
