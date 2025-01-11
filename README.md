# Stortingsvalgsimulator

Velkommen til Stortingsvalgsimulatoren! Dette prosjektet er laget for å simulere valgresultater basert på siste lokale målinger i hvert valgdistrikt, gjennom den modifiserte Sainte-Lagues-metoden som gjelder for det norske valgsystemet. Simuleringen omfatter også utjevningsmandater.

## Formål

Stortingsvalgsimulatoren er ment å:

- **Informere**: Gi brukere mulighet til å utforske hvordan endringer i stemmegivning eller fordeling av stemmer kan påvirke valgresultater.
  
- **Engasjere**: Bidra til økt forståelse av valgsystemet i Norge.

## Funksjoner

- Interaktiv simulering av valgresultater.
- Justering av parametere som stemmeandel og sperregrense.
- Visualisering av mandatfordeling.

## Hvordan å bruke

1. **Åpne nettleseren din**: Du trenger ikke å installere noe programvare eller laste ned skript.
2. **Gå til Streamlit-appen**: [Klikk på denne lenken for å starte simulatoren](https://valgsimulator.streamlit.app/)
3. **Utforsk**: Bruk menyene og valgene i appen for å simulere ulike valgscenarier. Juster parametere som stemmeandeler for partiene og se hvordan endringene påvirker mandatfordelingen.

### Hvordan å kjøre lokalt

1. **Installer Python**: Forsikre deg om at du har Python 3 installert på maskinen din.
2. **Last ned prosjektet**: Gå til GitHub-repositoriet og last ned hele prosjektmappen som en ZIP-fil: [Stortingsvalgsimulator](https://github.com/albertovth/albertovth_stortingsvalgsimulator). Pakk ut filene på datamaskinen din.
3. **Installer avhengigheter**: Åpne terminalen, naviger til mappen der prosjektfilene ligger, og kjør:
   ```bash
   pip install -r requirements.txt
4. **Start appen**: Kjør Streamlit-serveren ved å skrive:
   ```bash
   streamlit run Stortingsvalgsimulator_interaktiv.py
   ```
5. **Bruk appen lokalt**: Åpne lenken som vises i terminalen (som standard er det `http://localhost:8501`).

## Eksempel

Her er et eksempel på hvordan du kan bruke simulatoren:

1. Start skriptet.
2. Juster stemmeandeler for ulike partier.
3. Se hvordan endringene påvirker mandatfordelingen.

## Bidra

Dette prosjektet er åpent for forbedringer. Hvis du har forslag, finner feil eller ønsker å bidra, kan du:

1. Opprette en [issue](https://github.com/albertovth/albertovth_stortingsvalgsimulator/issues).
2. Lage en fork og sende inn en pull request.
3. Kontakte meg direkte gjennom GitHub.

## Lisens

Dette prosjektet er lisensiert under [MIT-lisensen](https://opensource.org/licenses/MIT). Du står fritt til å bruke, endre og distribuere koden, så lenge opprinnelig forfatter krediteres.

## Kontakt

Har du spørsmål eller tilbakemeldinger? Kontakt meg gjerne gjennom [GitHub-profilen min](https://github.com/albertovth).

Takk for at du bruker Stortingsvalgsimulatoren, og lykke til med simuleringene!
