# MUI_seminar_XGBoostRegressor_Solubility

## Opis Projekta
Projekt `MUI_seminar_XGBoostRegressor_Solubility` fokusira se na kvantitativnu strukturno-aktivnostnu analizu (QSAR) za predviđanje topljivosti spojeva. Cilj projekta je razviti i optimizirati model strojnog učenja koji precizno predviđa topljivost na osnovu različitih kemijskih deskriptora i otisaka molekula (fingerprints).

### Glavne Aktivnosti i Postignuća:
1. **Proći Marijev Tutorial - Kemija u Industriji:**
   - Lovrić, M. (2018). Molekulsko modeliranje odnosa strukturnih svojstava i aktivnosti molekula s pomoću programskog jezika Python (prvi dio). Kemija u industriji: Časopis kemičara i kemijskih inženjera Hrvatske, 67(9-10), 409-419.

2. **Izračun RDKit 2D Deskriptora i Treniranje XGBoost Regression Modela:**
   - Uspješno izvedeno, postignuta dobra početna točnost.

3. **Rad s Fingerprints i Varijancama:**
   - Fingerprints bez varijance nisu pronađeni, no uklonjeni su oni s varijancom manjom od 0.01. 
   - Rezultati poboljšani (R2: 0.77 u odnosu na osnovni R2: 0.71).

4. **Optimizacija Modela pomoću GridSearch:**
   - Provedene optimizacije modela, prilagođavanje hiperparametara.

5. **Kontrolirani Train/Test Split i Histogram Topljivosti:**
   - Primijećena anomalija u distribuciji topljivosti, upotrijebljen parametar `stratify`.

### Ključni Kodovi i Postupci:

#### A. Preprocesiranje Podataka
- Učitavanje i analiza podataka.
- Izračunavanje 2D deskriptora i fingerprints.
- Primjena VarianceThreshold selektora za filtriranje značajki.

#### B. Treniranje Osnovnog Modela
- Podjela podataka na trening i test skupove.
- Treniranje XGBoost modela s GridSearch optimizacijom.
- Evaluacija modela putem MSE i R2 Score.

#### C. Napredni Model s Fingerprints
- Treniranje poboljšanog modela s dodatnim fingerprints značajkama.
- GridSearch optimizacija s povećanim brojem hiperparametara.
- Vizualizacija stvarnih naspram predviđenih vrijednosti.

#### D. Stratificirani Model s Kontrolom Distribucije
- Korištenje stratifikacije za bolju reprezentaciju raspona topljivosti.
- Ponovna optimizacija modela s TransformedTargetRegressor.
- Detaljna vizualna analiza rezultata.

### Zaključak
Projekt `MUI_seminar_XGBoostRegressor_Solubility` uspješno demonstrira primjenu i optimizaciju modela strojnog učenja u kontekstu predviđanja topljivosti kemijskih spojeva. Kroz iterativni proces, projekt ukazuje na važnost preciznog preprocesiranja podataka, izbora relevantnih značajki i hiperparametara, te potrebu za razumijevanjem distribucije ciljne varijable u kontekstu QSAR modeliranja.