import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
st.set_page_config(layout="wide")
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        overflow-x: auto !important;
    }

    .main .block-container {
        overflow-x: auto !important;
        width: auto !important;
    }

    .st-emotion-cache-z5fcl4 {
        max-width: none !important;
    }
    </style>
""", unsafe_allow_html=True)


siste_oppdatering_dato = "5. september 2025"
siste_meningsmåling_dato = "5. september 2025"
første_meningsmåling_dato = "27. august 2025"  # Python 3 supports Unicode variable names


default_values = {
  "Parti": [
    "Ap",
    "H",
    "FrP",
    "SV",
    "Sp",
    "KrF",
    "V",
    "MDG",
    "R",
    "A",
    "AfN",
    "D",
    "FNTB",
    "Hp",
    "IN",
    "Lb",
    "PdK",
    "PS",
    "Pp",
    "PiP",
    "Gp",
    "RN",
    "Kp",
    "NKP",
    "PF",
    "FI",
    "Prognostisert valgoppslutning per fylke - godkjente stemmer",
    "Personer med stemmerett 2025"
  ],
  "Kategori": [
    4,
    8,
    10,
    3,
    5,
    7,
    6,
    5.5,
    1,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    0,
    0
  ],
  "Østfold": [
    "30.00%",
    "10.50%",
    "25.60%",
    "5.30%",
    "7.10%",
    "4.60%",
    "2.80%",
    "4.60%",
    "5.40%",
    "0.00%",
    "0.11%",
    "1.46%",
    "0.18%",
    "0.24%",
    "0.14%",
    "0.16%",
    "0.43%",
    "0.20%",
    "1.18%",
    "0.09%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "73.00%",
    "253308"
  ],
  "Akershus": [
    "27.50%",
    "20.10%",
    "20.40%",
    "6.10%",
    "3.50%",
    "3.10%",
    "4.90%",
    "4.90%",
    "4.90%",
    "0.34%",
    "0.00%",
    "1.01%",
    "0.00%",
    "1.01%",
    "0.67%",
    "0.67%",
    "0.34%",
    "0.34%",
    "0.34%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "79.10%",
    "575258"
  ],
  "Oslo": [
    "24.70%",
    "21.00%",
    "11.90%",
    "11.80%",
    "1.20%",
    "1.60%",
    "7.00%",
    "11.60%",
    "7.70%",
    "0.07%",
    "0.46%",
    "0.13%",
    "0.13%",
    "0.07%",
    "0.07%",
    "0.20%",
    "0.07%",
    "0.07%",
    "0.07%",
    "0.07%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.07%",
    "0.07%",
    "78.50%",
    "584525"
  ],
  "Hedmark": [
    "36.80%",
    "8.70%",
    "16.90%",
    "5.60%",
    "14.70%",
    "1.40%",
    "2.00%",
    "3.20%",
    "5.40%",
    "0.10%",
    "1.22%",
    "1.32%",
    "0.31%",
    "0.20%",
    "0.10%",
    "0.10%",
    "0.10%",
    "0.20%",
    "1.63%",
    "0.10%",
    "0.10%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "76.10%",
    "171890"
  ],
  "Oppland": [
    "31.20%",
    "9.60%",
    "18.20%",
    "5.90%",
    "17.30%",
    "2.50%",
    "2.80%",
    "2.90%",
    "5.40%",
    "0.10%",
    "0.90%",
    "0.50%",
    "0.20%",
    "0.20%",
    "0.10%",
    "0.10%",
    "0.10%",
    "0.20%",
    "1.60%",
    "0.10%",
    "0.00%",
    "0.00%",
    "0.10%",
    "0.00%",
    "0.00%",
    "0.00%",
    "75.00%",
    "134162"
  ],
  "Buskerud": [
    "27.00%",
    "13.60%",
    "26.20%",
    "6.80%",
    "4.70%",
    "3.30%",
    "3.60%",
    "5.10%",
    "4.60%",
    "0.09%",
    "1.19%",
    "0.34%",
    "0.26%",
    "0.17%",
    "0.17%",
    "0.17%",
    "0.17%",
    "0.26%",
    "1.96%",
    "0.09%",
    "0.09%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.09%",
    "0.09%",
    "75.20%",
    "215155"
  ],
  "Vestfold": [
    "27.80%",
    "14.80%",
    "25.40%",
    "4.60%",
    "5.10%",
    "5.20%",
    "3.30%",
    "4.40%",
    "4.70%",
    "0.06%",
    "0.80%",
    "0.25%",
    "0.18%",
    "0.31%",
    "0.18%",
    "0.18%",
    "0.06%",
    "0.18%",
    "2.15%",
    "0.06%",
    "0.06%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.06%",
    "0.06%",
    "76.50%",
    "206304"
  ],
  "Telemark": [
    "32.20%",
    "10.10%",
    "20.20%",
    "5.10%",
    "7.20%",
    "6.40%",
    "2.70%",
    "2.40%",
    "8.00%",
    "0.06%",
    "0.87%",
    "0.25%",
    "0.12%",
    "0.44%",
    "0.37%",
    "0.06%",
    "0.37%",
    "0.19%",
    "2.81%",
    "0.06%",
    "0.06%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.06%",
    "0.06%",
    "74.50%",
    "143336"
  ],
  "Aust-Agder": [
    "25.50%",
    "13.00%",
    "22.90%",
    "5.10%",
    "6.70%",
    "9.70%",
    "4.40%",
    "3.60%",
    "6.10%",
    "0.02%",
    "0.29%",
    "0.12%",
    "0.06%",
    "0.19%",
    "0.08%",
    "0.04%",
    "0.08%",
    "0.06%",
    "1.80%",
    "0.02%",
    "0.00%",
    "0.00%",
    "0.02%",
    "0.00%",
    "0.00%",
    "0.00%",
    "75.80%",
    "89235"
  ],
  "Vest-Agder": [
    "21.10%",
    "13.80%",
    "24.40%",
    "4.80%",
    "4.10%",
    "16.50%",
    "4.50%",
    "2.80%",
    "5.20%",
    "0.01%",
    "0.37%",
    "0.07%",
    "0.03%",
    "0.13%",
    "0.04%",
    "0.03%",
    "0.04%",
    "0.07%",
    "1.96%",
    "0.01%",
    "0.01%",
    "0.00%",
    "0.01%",
    "0.01%",
    "0.00%",
    "0.00%",
    "77.00%",
    "163306"
  ],
  "Rogaland": [
    "21.40%",
    "15.80%",
    "29.00%",
    "4.90%",
    "3.80%",
    "10.20%",
    "2.20%",
    "2.70%",
    "5.70%",
    "0.03%",
    "0.33%",
    "0.16%",
    "0.07%",
    "0.16%",
    "0.20%",
    "0.07%",
    "0.20%",
    "0.13%",
    "2.66%",
    "0.03%",
    "0.03%",
    "0.00%",
    "0.03%",
    "0.03%",
    "0.03%",
    "0.03%",
    "78.10%",
    "385280"
  ],
  "Hordaland": [
    "24.40%",
    "17.60%",
    "21.90%",
    "6.50%",
    "4.70%",
    "5.70%",
    "3.50%",
    "7.00%",
    "5.40%",
    "0.04%",
    "0.32%",
    "0.28%",
    "0.07%",
    "0.18%",
    "0.21%",
    "0.07%",
    "0.21%",
    "0.07%",
    "1.72%",
    "0.04%",
    "0.04%",
    "0.00%",
    "0.00%",
    "0.04%",
    "0.04%",
    "0.00%",
    "79.90%",
    "435130"
  ],
  "Sogn og Fjordane": [
    "27.40%",
    "8.80%",
    "19.40%",
    "5.40%",
    "17.00%",
    "5.60%",
    "3.40%",
    "4.70%",
    "5.20%",
    "0.05%",
    "0.32%",
    "0.14%",
    "0.05%",
    "0.18%",
    "0.23%",
    "0.05%",
    "0.23%",
    "0.09%",
    "1.73%",
    "0.05%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "79.70%",
    "80181"
  ],
  "Møre og Romsdal": [
    "22.90%",
    "9.00%",
    "30.60%",
    "4.70%",
    "8.90%",
    "7.30%",
    "3.20%",
    "5.20%",
    "4.10%",
    "0.03%",
    "0.38%",
    "0.16%",
    "0.06%",
    "0.16%",
    "0.22%",
    "0.03%",
    "0.22%",
    "0.06%",
    "1.68%",
    "0.03%",
    "0.03%",
    "0.00%",
    "0.00%",
    "0.03%",
    "0.00%",
    "0.00%",
    "77.60%",
    "214398"
  ],
  "Sør-Trøndelag": [
    "30.40%",
    "13.20%",
    "20.20%",
    "8.40%",
    "6.40%",
    "3.00%",
    "3.20%",
    "6.10%",
    "6.80%",
    "0.03%",
    "0.30%",
    "0.57%",
    "0.07%",
    "0.07%",
    "0.10%",
    "0.07%",
    "0.10%",
    "0.07%",
    "0.73%",
    "0.03%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.03%",
    "0.03%",
    "0.00%",
    "78.50%",
    "281649"
  ],
  "Nord-Trøndelag": [
    "35.50%",
    "10.80%",
    "15.80%",
    "6.50%",
    "15.30%",
    "3.00%",
    "1.00%",
    "3.00%",
    "5.80%",
    "0.05%",
    "0.55%",
    "0.44%",
    "0.11%",
    "0.11%",
    "0.27%",
    "0.05%",
    "0.27%",
    "0.11%",
    "1.26%",
    "0.05%",
    "0.00%",
    "0.00%",
    "0.05%",
    "0.05%",
    "0.00%",
    "0.00%",
    "76.60%",
    "103712"
  ],
  "Nordland": [
    "29.70%",
    "11.30%",
    "22.80%",
    "6.90%",
    "10.50%",
    "2.30%",
    "1.80%",
    "3.40%",
    "7.70%",
    "0.06%",
    "0.77%",
    "0.24%",
    "0.18%",
    "0.12%",
    "0.24%",
    "0.12%",
    "0.24%",
    "0.12%",
    "1.19%",
    "0.06%",
    "0.00%",
    "0.00%",
    "0.06%",
    "0.06%",
    "0.06%",
    "0.00%",
    "74.20%",
    "193595"
  ],
  "Troms": [
    "27.20%",
    "10.00%",
    "21.50%",
    "8.10%",
    "5.90%",
    "4.40%",
    "2.60%",
    "5.20%",
    "10.80%",
    "0.08%",
    "1.16%",
    "0.00%",
    "0.15%",
    "0.15%",
    "0.23%",
    "0.15%",
    "0.23%",
    "0.15%",
    "1.70%",
    "0.08%",
    "0.08%",
    "0.00%",
    "0.08%",
    "0.08%",
    "0.08%",
    "0.00%",
    "75.00%",
    "136080"
  ],
  "Finnmark": [
    "31.50%",
    "5.00%",
    "19.90%",
    "6.30%",
    "5.00%",
    "2.30%",
    "1.20%",
    "2.10%",
    "10.30%",
    "0.09%",
    "1.53%",
    "0.00%",
    "0.27%",
    "0.36%",
    "0.45%",
    "0.18%",
    "0.45%",
    "0.18%",
    "1.53%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.09%",
    "11.46%",
    "0.00%",
    "72.00%",
    "59383"
  ]
}
df = pd.DataFrame(default_values)

districts = [col for col in df.columns if col not in ['Parti', 'Kategori']]
email_address = "alberto@vthoresen.no"


st.title("Stortingsvalgsimulator")
st.markdown("""
## Innholdsfortegnelse

- [Simulerte valgresultater](#simulerte-valgresultater)
- [Resultat etter valgdistrikt](#resultat-etter-valgdistrikt)
- [Resultat for hele landet](#resultat-for-hele-landet)
- [Diagram](#diagram)
- [Simulert eller prognostisert mandatfordeling per valgdistrikt (kartvisning)](#simulert-eller-prognostisert-mandatfordeling-per-valgdistrikt-kartvisning)
""")

st.markdown("""
###  Diagram og kart for prognostisert mandatfordeling presenteres nederst i hovedsiden. For å se venstremenyen: utvid med pilen til venstre. Da kan du justere prosentfordeling og valgdeltakelse per distrikt.
""")

# Sammendrag
st.markdown("""
Dette verktøyet lar deg simulere valgresultater, basert på meningsmålinger per valgdistrikt. 
Verktøyet bruker den modifiserte Sainte-Laguës-metoden som benyttes i det norske valgsystemet. 
Målet er å øke forståelsen for valgprosesser, og vise hvordan Python og Streamlit kan brukes til dataanalyse.
""")

# Lenker til GitHub og kontakt
st.markdown("### Ressurser")
st.markdown("[Se kildekoden på GitHub](https://github.com/albertovth/albertovth_stortingsvalgsimulator)")
st.markdown(f"Kontakt: [Alberto Valiente Thoresen](mailto:{email_address})")

# Viktig melding
st.warning(f"""
**Viktig melding:**
Per siste oppdatering {siste_oppdatering_dato} er eldste meningsmåling fra {første_meningsmåling_dato} og nyeste fra {siste_meningsmåling_dato}.
Nyere data vil bli inkludert etterhvert som de blir tilgjengelige. Oppdateringer vil bli gjort rundt en gang i måneden frem til sommeren 2025, og hyppigere rett før valget, som er i september 2025.
Merk også at kategorien "Andre" i Poll of polls omfatter flere partier. Dette fordeles proporsjonelt til "Andre" partier som deltok ved forrige valg, ifølge stemmene de fikk. Dette er ikke presis, men det er bedre enn å behandle hele kategorien "Andre" som ett parti.
""")

# Diagram og instruksjoner
st.markdown("### Diagram og simulering")
st.markdown(f"""Juster prognoser for valgresultater for valgdistriktene i venstremenyen. Valgdeltagelse per distrikt kan også oppgis nederst i venstremenyen. 
            Utgangspunktet baseres på raden 'Siste lokale måling' som publiseres i [Poll of Polls](https://www.pollofpolls.no/?cmd=Stortinget&fylke=0), 
            siste oppdatering per {siste_oppdatering_dato}, med estimater for antall personer med stemmerett per valgdistrikt basert på tall for 2023 og ekstrapolering av befolkningsvekst (kilde SSB). Diagram for prognostisert mandatfordeling presenteres nederst i hovedsiden.  
            Det kan ta litt tid før dette vises. Kategorien 'Andre' (partier), fra Poll of polls (Dvs. mindre partier, som ikke er R, SV, Ap, Sp, MDG, V, KrF, H og Frp) fordeles proporsjonelt til andre partier som deltok i Stortingsvalget 2021, basert på resultatet disse partiene fikk da. Du kan justere prosent for disse partiene, eller oppdatere prosenten til de store partiene i venstremenyen. For bedre resultater sørg for at prosentandel for alle partier i valgdistriktet summerer 100 prosent.""")

st.markdown("""
### Feilmarginer

Feilmarginene i distriktsmålingene varierer etter utvalgsstørrelse og parti, men ligger i snitt rundt ±1,7 prosentpoeng.  
Medianen er noe lavere, på ±1,55 prosentpoeng (per juni 2025).

For detaljer per måling og distrikt, se kildedata fra [Poll of polls](https://www.pollofpolls.no/?cmd=Stortinget&fylke=0).
""")

# Kilder
st.markdown("### Kilder")
st.write("[Tall fra SSB for personer med stemmerett i 2023 finner du her](https://www.ssb.no/statbank/table/12638/tableViewLayout1/)")
st.write("[Tall fra SSB for personer med stemmerett i 2021 finner du her](https://www.ssb.no/statbank/table/09839/tableViewLayout1/)")
st.write("[Tall fra SSB for å beregne befolkningsvekst per valgdistrikt](https://www.ssb.no/statbank/table/06913)")
st.write("[Poll of Polls](https://www.pollofpolls.no/?cmd=Stortinget&fylke=0)")

percentage_dict = {}
participation_dict = {}

def validate_percentage_sums(percentage_dict, districts, partier):
    issues_found = False
    for distrikt in districts:
        total = sum([
            float(percentage_dict.get((parti, distrikt), '0%').strip('%'))
            for parti in partier
        ])
        if abs(total - 100.0) > 0.1:
            st.warning(f"Prosentene i {distrikt} summerer til {total:.2f}% – ikke 100%.")
            issues_found = True
    if not issues_found:
        st.success("Alle distriktsprosentene summerer til 100 % ± 0.1 %.")


st.sidebar.header("Her kan du endre oppslutning og valgdeltagelse (nederst) i prosent")
st.sidebar.header("Juster partioppslutning i valgdistriktene")
for distrikt in districts:
    if distrikt not in ['Prognostisert valgoppslutning per fylke - godkjente stemmer', 'Personer med stemmerett 2025']:
        st.sidebar.subheader(distrikt)
        for index, row in df.iterrows():
            if row['Parti'] not in ['Prognostisert valgoppslutning per fylke - godkjente stemmer', 'Personer med stemmerett 2025']:
                default_percentage = float(row[distrikt].strip('%'))
                modified_percentage = st.sidebar.slider(f"{row['Parti']} ({distrikt})", 0.0, 100.0, default_percentage)
                percentage_dict[(row['Parti'], distrikt)] = f"{modified_percentage}%"
st.sidebar.header("Her kan du endre deltagelse")
for distrikt in districts:
    if distrikt not in ['Personer med stemmerett 2025']:
        participation_row = df[df['Parti'] == 'Prognostisert valgoppslutning per fylke - godkjente stemmer']
        default_participation = float(participation_row[distrikt].values[0].strip('%'))
        modified_participation = st.sidebar.slider(f"Deltagelse ({distrikt})", 0.0, 100.0, default_participation)
        participation_dict[distrikt] = f"{modified_participation}%"

ekte_partier = [p for p in df['Parti'] if p not in 
                 ['Prognostisert valgoppslutning per fylke - godkjente stemmer', 
                  'Personer med stemmerett 2025']]
validate_percentage_sums(percentage_dict, districts, ekte_partier)


def validate_used_districts(used_districts):
    if len(used_districts) > 19:
        st.error(f"Flere enn 19 fylker har fått utjevningsmandater: {len(used_districts)}. Dette bryter med valgloven.")
    else:
        st.info(f"{len(used_districts)} fylker har fått utjevningsmandat, som forventet.")
def calculate_stemmer(row, percentage_dict, participation_dict):
    stemmer_data = []
    for distrikt in districts:
        percentage = percentage_dict.get((row['Parti'], distrikt), row[distrikt])
        valgdeltakelse = participation_dict.get(distrikt, df[df['Parti'] == 'Prognostisert valgoppslutning per fylke - godkjente stemmer'][distrikt].values[0])
        personer_med_stemmerett = df[df['Parti'] == 'Personer med stemmerett 2025'][distrikt].values[0]
        
        if pd.notna(percentage) and pd.notna(valgdeltakelse) and pd.notna(personer_med_stemmerett):
            percentage_value = float(percentage.strip('%')) / 100
            valgdeltakelse_value = float(valgdeltakelse.strip('%')) / 100
            personer_value = float(personer_med_stemmerett.replace(',', ''))
            stemmer = percentage_value * valgdeltakelse_value * personer_value
            stemmer_data.append(stemmer)
        else:
            stemmer_data.append(np.nan)
    return stemmer_data
results = {'Parti': [], 'Distrikt': [], 'Stemmer': [], 'Kategori': []}

for index, row in df.iterrows():
    if row['Parti'] not in ['Prognostisert valgoppslutning per fylke - godkjente stemmer', 'Personer med stemmerett 2025']:
        stemmer_data = calculate_stemmer(row, percentage_dict, participation_dict)
        
        for distrikt, stemmer in zip(districts, stemmer_data):
            results['Parti'].append(row['Parti'])
            results['Distrikt'].append(distrikt)
            results['Stemmer'].append(stemmer)
            results['Kategori'].append(row['Kategori'])
results_df = pd.DataFrame(results)
results_display = results_df.copy()
results_display["Stemmer"] = results_display["Stemmer"].round(0).astype(int)
display_results = results_display.drop(columns=["Kategori"])
st.write("### Simulerte valgresultater")
st.dataframe(display_results)
fixed_districts = pd.DataFrame({
    'Fylke': [
        'Oslo', 'Akershus', 'Hordaland', 'Rogaland', 'Sør-Trøndelag', 'Østfold', 'Nordland', 'Buskerud',
        'Møre og Romsdal', 'Hedmark', 'Vestfold', 'Oppland',
        'Telemark', 'Vest-Agder', 'Troms', 'Nord-Trøndelag',
        'Finnmark', 'Aust-Agder', 'Sogn og Fjordane'
    ],
    'Distriktmandater': [
        19, 19, 15, 13, 9, 8, 8, 7, 7, 6, 6, 5, 5, 5, 5, 4, 3, 3, 3
    ],
    'Utjevningsmandater': [1] * 19
})
def adjusted_sainte_lague(votes, seats, first_divisor=1.4):
    parties = len(votes)
    quotients = [[votes[i] / (first_divisor if j == 0 else 2 * j + 1) for j in range(seats)] for i in range(parties)]
    flat_quotients = sorted([(quotients[i][j], i) for i in range(parties) for j in range(seats)], reverse=True)
    seat_allocation = [0] * parties
    for i in range(seats):
        seat_allocation[flat_quotients[i][1]] += 1
    return seat_allocation
def national_seats(votes, total_seats, first_divisor=1.4):
    parties = len(votes)
    quotients = [[votes[i] / (first_divisor if j == 0 else 2 * j + 1) for j in range(total_seats)] for i in range(parties)]
   
    flat_quotients = sorted([(quotients[i][j], i) for i in range(parties) for j in range(total_seats)], reverse=True)
    seat_allocation = [0] * parties
    for i in range(total_seats):
        seat_allocation[flat_quotients[i][1]] += 1
   
    return seat_allocation

def distribute_levelling_mandates(data_input, fixed_districts, _dummy_national_result=None, threshold=0.04):
    import streamlit as st
    import pandas as pd

    # 0) Ekskluder ikke-politiske rader (f.eks. prognoser og velger-tall)
    ikke_partier = [
        'Prognostisert valgoppslutning per fylke - godkjente stemmer',
        'Personer med stemmerett 2025'
    ]
    real_data = data_input[~data_input['Parti'].isin(ikke_partier)].copy()

    # 1) Nasjonale stemmer for alle "reelle" partier
    all_votes = real_data.groupby('Parti')['Stemmer'].sum()
    total_votes = all_votes.sum()

    # 2) Finn partier som har ≥ 4 % nasjonalt og sto på liste i alle fylker (§ 11-7(2))
    fylker = fixed_districts['Fylke'].tolist()

    def har_stilt_i_alle_fylker(parti):
        for D in fylker:
            sub = real_data[
                (real_data['Parti'] == parti) &
                (real_data['Distrikt'] == D)
            ]
            if sub.empty:
                return False
        return True

    four_percent_parties = [
        parti
        for parti, v in all_votes.items()
        if (v / total_votes) >= threshold and har_stilt_i_alle_fylker(parti)
    ]

    if not four_percent_parties:
        # Ingen som oppfyller § 11-7(2)
        return pd.DataFrame(columns=['Distrikt', 'Parti', 'Utjevningsmandater'])

    # 3) Hent distriktsmandater for alle partier (brukes til under4-trekking + overheng-sjekk)
    district_mandates_full = real_data.groupby('Parti')['Distriktmandater'].sum()

    # 4) Kjør nasjonal Sainte-Laguë + overheng-loop (§ 11-7(3–5))
    gjeldende_partier = four_percent_parties.copy()

    while True:
        # 4a) Summer distriktsmandater vunnet av partier som IKKE er i gjeldende_partier
        under4_partier = [p for p in all_votes.index if p not in gjeldende_partier]
        under4_distrikt_sum = int(district_mandates_full.reindex(under4_partier, fill_value=0).sum())

        # 4b) Antall nasjonale seter som gjenstår til gjeldende_partier
        total_national_seats = 169 - under4_distrikt_sum
        if total_national_seats <= 0:
            st.error("Alle nasjonale seter er opptatt av under 4 %-partier. Ingen utjevningsmandater.")
            return pd.DataFrame(columns=['Distrikt', 'Parti', 'Utjevningsmandater'])

        # 4c) Stemmetall kun for gjeldende_partier, sortert alfabetisk
        votes_4pct = all_votes.loc[gjeldende_partier].sort_index()

        # 4d) Nasjonal Sainte-Laguë på total_national_seats seter
        nasjonalt_array = adjusted_sainte_lague(
            votes_4pct.values,
            seats=total_national_seats,
            first_divisor=1.4
        )
        nasjonalt_df = pd.DataFrame({
            'Parti': votes_4pct.index,
            'Mandater': nasjonalt_array
        }).set_index('Parti')

        # 4e) Hvor mange distriktsmandater vant hver av gjeldende_partier?
        district_mandates_4pct = district_mandates_full.reindex(gjeldende_partier, fill_value=0)

        # 4f) Overheng-sjekk: dersom noen har distriktsmandater > nasjanalt tildelte, fjern dem
        overhang = [
            P for P in gjeldende_partier
            if district_mandates_4pct[P] >= nasjonalt_df.loc[P, 'Mandater']
        ]

        if not overhang:
            break

        for P in overhang:
            st.info(
                f"Parti {P} fjernes fra utjevning (overheng: "
                f"{int(district_mandates_4pct[P])} distriktsmandater >= "
                f"{int(nasjonalt_df.loc[P, 'Mandater'])} nasjonale mandater)."
            )
            gjeldende_partier.remove(P)

        if not gjeldende_partier:
            return pd.DataFrame(columns=['Distrikt', 'Parti', 'Utjevningsmandater'])

    # 5) Beregn endelig utjevningsbehov = nasjonalt_df[P] − district_mandates_4pct[P]
    leveling_needs = {
        P: int(nasjonalt_df.loc[P, 'Mandater']) - int(district_mandates_4pct[P])
        for P in nasjonalt_df.index
    }

    total_needs = sum(leveling_needs.values())
    if total_needs != 19:
        st.error(
            f"Feil i utjevningsberegningen: Summen av behovene er {total_needs}, "
            "men skal være 19 i henhold til § 11-7."
        )
        return pd.DataFrame(columns=['Distrikt', 'Parti', 'Utjevningsmandater'])

    # 6) For dynamisk tildeling av distriktmandat per distrikt
    #    a) Total stemmetall per fylke
    total_stemmer_per_fylke = {
        D: real_data[real_data['Distrikt'] == D]['Stemmer'].sum()
        for D in fylker
    }
    #    b) Antall distriktsmandater i hvert fylke
    distriktsmandater_map = {
        row['Fylke']: int(row['Distriktmandater'])
        for _, row in fixed_districts.iterrows()
    }
    #    c) Hvor mange distriktsmandater hvert parti har i hvert fylke
    per_district_df = calculate_district_mandates(real_data, fixed_districts)
    district_mandates_by_PD = {
        (P, D): int(per_district_df.at[D, P])
        for P in per_district_df.columns
        for D in per_district_df.index
    }

    # 7) Del ut 19 utjevningsmandater én-for-én (maks én per valgdistrikt, aldri mer enn behov per parti)
    used_districts = set()
    levelling_list = []

    while sum(leveling_needs.values()) > 0:
        best_value = -1
        best_P = None
        best_D = None

        for D in fylker:
            if D in used_districts:
                continue
            d_D = total_stemmer_per_fylke[D] / distriktsmandater_map[D]

            for P, behov in leveling_needs.items():
                if behov <= 0:
                    continue
                m_PD = district_mandates_by_PD.get((P, D), 0)
                v_PD = real_data[
                    (real_data['Parti'] == P) & (real_data['Distrikt'] == D)
                ]['Stemmer'].sum()

                # Sainte‐Laguë‐kvotient for neste mandat i (P, D)
                current_value = v_PD / (d_D * (2*m_PD + 1))
                if current_value > best_value:
                    best_value = current_value
                    best_P = P
                    best_D = D

        if best_P is not None and best_D is not None:
            levelling_list.append({
                'Distrikt': best_D,
                'Parti': best_P,
                'Utjevningsmandater': 1
            })
            st.info(f"Utjevningsmandat {len(levelling_list)}/19: Parti {best_P} tildeles i valgdistrikt {best_D}.")
            leveling_needs[best_P] -= 1
            used_districts.add(best_D)
            district_mandates_by_PD[(best_P, best_D)] = district_mandates_by_PD.get((best_P, best_D), 0) + 1
        else:
            break

    # 8) Meldinger og retur
    antall_fylker = len(used_districts)
    if antall_fylker < 19:
        st.success(
            f"Totalt ble {len(levelling_list)} utjevningsmandater delt ut. "
            f"{antall_fylker} fylker har minst ett mandat."
        )
    else:
        st.success(
            "Totalt ble 19 utjevningsmandater delt ut, fordelt på 19 ulike fylker "
            "(ingen fylke fikk mer enn ett mandat)."
        )

    return pd.DataFrame(levelling_list)

def calculate_district_mandates(data_input, fixed_districts):
    districts = fixed_districts['Fylke'].unique()
    parties = sorted(data_input['Parti'].unique())
    district_mandates = pd.DataFrame(index=districts, columns=parties)

    for district in districts:
        district_data = data_input[data_input['Distrikt'] == district]
        district_data = district_data.set_index('Parti').reindex(parties).fillna(0).reset_index()
        votes = district_data['Stemmer'].values
        seats = int(fixed_districts[fixed_districts['Fylke'] == district]['Distriktmandater'].values[0])

        if len(votes) == 0:
            continue

        mandates = adjusted_sainte_lague(votes, seats)
        for i, party in enumerate(parties):
            district_mandates.at[district, party] = mandates[i]

    return district_mandates.fillna(0).astype(int)


def plot_half_circle_chart(data, colors):
    
    aggregated_data = data.groupby(['Parti', 'Kategori']).sum().reset_index()
   
   
    aggregated_data = aggregated_data.sort_values(by='Kategori', ascending=False)
   
    
    fictitious_party = pd.DataFrame({
        'Parti': ['Fiktivt Parti'],
        'Kategori': [0],
        'TotalMandater': [sum(aggregated_data['TotalMandater'])]
    })
   
    aggregated_data = pd.concat([aggregated_data, fictitious_party], ignore_index=True)
   
    total_mandates = sum(aggregated_data['TotalMandater'])
   
   
    if total_mandates == 0:
        st.error("Total mandater kan ikke være null.")
        return
   
    angles = aggregated_data['TotalMandater'] / total_mandates * 360  
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))
    startangle = 270  
    wedges, texts = ax.pie(
        angles,
        startangle=startangle,
        colors=[colors.get(kategori, "#FFFFFF") if kategori != 0 else "#FFFFFF" for kategori in aggregated_data['Kategori']],
        wedgeprops=dict(width=0.3, edgecolor='none')  
    )
   
    labels = []
    for i, wedge in enumerate(wedges):
        if aggregated_data['Parti'].iloc[i] == 'Fiktivt Parti':
            continue  
        angle = (wedge.theta2 - wedge.theta1) / 2.0 + wedge.theta1
        x = np.cos(np.radians(angle))
        y = np.sin(np.radians(angle))

        label = ax.text(
            x * 0.7, y * 0.7, 
            f"{aggregated_data['Parti'].iloc[i]}: {aggregated_data['TotalMandater'].iloc[i]}",
            horizontalalignment='center', 
            verticalalignment='center', 
            fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.6),
            rotation=90
        )
        labels.append(label)

        
    plt.gca().set_aspect('equal')
    fig.tight_layout()
    plt.gca().set_position([0, 0, 1, 1])
    fig.canvas.draw()
    
    trans_data = Affine2D().rotate_deg(90) + ax.transData
    for text in texts:
        text.set_transform(trans_data)
    for wedge in wedges:
        wedge.set_transform(trans_data)
    for label in labels:
        label.set_transform(trans_data)
   
    ax.set(aspect="equal", title="Mandatfordeling")
    st.pyplot(fig)
votes_per_party = results_df.groupby('Parti')['Stemmer'].sum().reset_index()
votes_per_party = votes_per_party.sort_values(by='Parti').reset_index(drop=True)
parties = votes_per_party['Parti']
votes = votes_per_party['Stemmer'].values
total_seats = 169
district_seats = 150
levelling_seats = 19
national_result = national_seats(votes, total_seats, first_divisor=1.4)
national_result_df = pd.DataFrame({
    'Parti': parties,
    'Mandater': national_result
})
st.write("Hele landet som valgdistrikt, kun som en referanse (alle partier, inkludert under sperregrensen):")
st.write(national_result_df)
district_mandates_df = calculate_district_mandates(results_df, fixed_districts)
st.write("Distriktmandater:")
st.write(district_mandates_df)
district_mandates_df = district_mandates_df.reset_index().melt(id_vars='index', var_name='Parti', value_name='Distriktmandater')
district_mandates_df.rename(columns={'index': 'Distrikt'}, inplace=True)
st.write("Omformet tabell med distriktmandater:")
st.write(district_mandates_df)
results_df = results_df.merge(district_mandates_df, on=['Distrikt', 'Parti'], how='left')
results_display = results_df.copy()
results_display["Stemmer"] = results_display["Stemmer"].round(0).astype(int)
display_df = results_display.drop(columns=["Kategori"])
st.write("Data med beregnede 'Distriktmandater':")
st.write(display_df)
levelling_mandates_df = distribute_levelling_mandates(results_df, fixed_districts, national_result)

validate_used_districts(set(levelling_mandates_df['Distrikt']))

st.write("Utjevningsmandater per distrikt:")
st.write(levelling_mandates_df)
results_df = results_df.merge(levelling_mandates_df, on=['Distrikt', 'Parti'], how='left')
results_df['Utjevningsmandater'] = results_df['Utjevningsmandater'].fillna(0).astype(int)
results_display = results_df.copy()
results_display["Stemmer"] = results_display["Stemmer"].round(0).astype(int)
display_df = results_display.drop(columns=["Kategori"])
st.write("Data med beregnede'Utjevningsmandater':")
st.write(display_df)
results_df['TotalMandater'] = results_df['Distriktmandater'] + results_df['Utjevningsmandater']
total_district_mandates = results_df['Distriktmandater'].sum()
total_levelling_mandates = results_df['Utjevningsmandater'].sum()
total_mandates = results_df['TotalMandater'].sum()
if total_district_mandates != district_seats:
    st.error("Totale distriktmandater summerer ikke 150. Sjekk beregningene dine.")
if total_levelling_mandates != levelling_seats:
    st.error("Totale utjevningsmandater summerer ikke 19. Sjekk beregningene dine.")
if total_mandates != total_seats:
    st.error("Totale mandater summerer ikke 169. Sjekk beregningene dine.")
results_display = results_df.copy()
results_display["Stemmer"] = results_display["Stemmer"].round(0).astype(int)
display_results = results_display.drop(columns=["Kategori"])
st.subheader('Resultat etter valgdistrikt')
st.write(display_results)
aggregated_data = results_df.groupby(['Parti']).agg({
    'Stemmer': 'sum',
    'Distriktmandater': 'sum',
    'Utjevningsmandater': 'sum',
    'TotalMandater': 'sum',
    'Kategori': 'first'  
}).reset_index()
aggregated_display = aggregated_data.copy()
aggregated_display["Stemmer"] = aggregated_display["Stemmer"].round(0).astype(int)
display_aggregated = aggregated_display.drop(columns=["Kategori"])
st.subheader('Resultat for hele landet')
st.write(display_aggregated)
color_mapping = {
    1: '#8B0000', 2: '#A52A2A', 3: '#CD5C5C', 4: '#F08080', 5: '#FFA07A', 5.5: '#355E3B',
    6: '#ADD8E6', 7: '#6495ED', 8: '#4169E1', 9: '#0000CD', 10: '#0000FF',
    11: '#FFA500'
}

aggregated_data = aggregated_data[aggregated_data['TotalMandater'] > 0]


rodgronne_partier = ["R", "SV", "Ap", "Sp", "MDG"]
borgerlige_partier = ["V", "KrF", "H", "FrP"]

rodgronne_mandater = aggregated_data[aggregated_data['Parti'].isin(rodgronne_partier)]['TotalMandater'].sum()
borgerlige_mandater = aggregated_data[aggregated_data['Parti'].isin(borgerlige_partier)]['TotalMandater'].sum()


st.markdown(f"**Rødgrønne: {rodgronne_mandater} mandater**")
st.markdown(f"**Borgerlige: {borgerlige_mandater} mandater**")

st.subheader('Diagram')
plot_half_circle_chart(aggregated_data, color_mapping)

import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import matplotlib.patches as patches

geojson_path = "https://raw.githubusercontent.com/albertovth/albertovth_stortingsvalgsimulator/main/data/Basisdata_0000_Norge_4258_Valgdistrikter_GeoJSON.geojson"
gdf = gpd.read_file(geojson_path)
gdf = gdf.to_crs(epsg=4258)

# Normalize district names in map
gdf['valgdistriktsnavn'] = gdf['valgdistriktsnavn'].replace({
    'Finnmark – Finnmárku – Finmarkku': 'Finnmark',
    'Troms – Romsa – Tromssa': 'Troms',
    'Nordland – Nordlánnda': 'Nordland'
})

def create_matrix_dots(results_df, gdf, max_cols=6, margin_ratio=0.2):
    all_dots = []
    preferred_order = ["R", "SV", "Ap", "Sp", "MDG", "V", "KrF", "H", "FrP"]

    for district_name in results_df['Distrikt'].unique():
        geom_row = gdf[gdf['valgdistriktsnavn'] == district_name]
        if geom_row.empty:
            continue

        geom = geom_row.geometry.values[0]
        centroid = geom.centroid
        x0, y0 = centroid.x, centroid.y

        # Special shift for selected districts
        if district_name == "Oslo":
            x0 += 2.5
            y0 += 1.0
        elif district_name == "Akershus":
            x0 += 2.5
            y0 -= 1.0
        elif district_name == "Vestfold":
            x0 += 1
            y0 -= 1.0
        elif district_name == "Østfold":
            x0 += 0.5
            y0 -= 0.5    
        elif district_name == "Hedmark":
            x0 += 0.75
            y0 -= 0
        elif district_name == "Hordaland":
            x0 += 0.0
            y0 += 0.5
        elif district_name == "Rogaland":
            x0 += 0.0
            y0 += 0.25
        elif district_name == "Aust-Agder":
            x0 += 0.75
            y0 -= 0 
        elif district_name == "Telemark":
            x0 += 0.24
            y0 -= 0.15
        elif district_name == "Buskerud":
            x0 += 0
            y0 += 0.15
        elif district_name == "Sør-Trøndelag":
            x0 += 0
            y0 -= 0.15
        elif district_name == "Nord-Trøndelag":
            x0 += 0.30
            y0 += 0.15
        elif district_name == "Nordland":
            x0 += 0
            y0 += 0.15
        elif district_name == "Troms":
            x0 += 0.45
            y0 += 0
        elif district_name == "Finnmark":
            x0 += 1.0
            y0 += 0

        
        minx, miny, maxx, maxy = geom.bounds
        district_width = maxx - minx
        spacing = (district_width / max_cols) * (1 - margin_ratio)
        spacing = max(spacing, 0.1)  

        
        if district_name in ["Oslo", "Akershus", "Vestfold", "Østfold","Sør-Trøndelag"]:
            spacing = max(spacing, 0.25)

        
        mandates_per_party = (
            results_df[results_df['Distrikt'] == district_name]
            .groupby('Parti')['TotalMandater']
            .sum()
            .astype(int)
            .to_dict()
        )

        party_list = []
        for party in preferred_order:
            party_list.extend([party] * mandates_per_party.get(party, 0))
        for party in mandates_per_party:
            if party not in preferred_order:
                party_list.extend([party] * mandates_per_party[party])

        for i, party in enumerate(party_list):
            col = i % max_cols
            row = i // max_cols
            x = x0 + (col - max_cols / 2) * spacing
            y = y0 - row * spacing

            subset = results_df[(results_df['Parti'] == party) & (results_df['Distrikt'] == district_name)]
            if not subset.empty and pd.notna(subset['Kategori'].values[0]):
                kategori = subset['Kategori'].values[0]
            else:
                kategori = df[df['Parti'] == party]['Kategori'].values[0]  # fallback

            all_dots.append({
                'Distrikt': district_name,
                'Parti': party,
                'geometry': Point(x, y),
                'Farge': color_mapping.get(kategori, '#CCCCCC')
            })

    return gpd.GeoDataFrame(all_dots, geometry='geometry', crs="EPSG:4258")



dots_gdf = create_matrix_dots(results_df, gdf, max_cols=6)


st.subheader("Simulert eller prognostisert mandatfordeling per valgdistrikt (kartvisning)")


fig, ax = plt.subplots(figsize=(12, 16))
gdf.boundary.plot(ax=ax, color="black", linewidth=0.5)
dots_gdf.plot(ax=ax, color=dots_gdf["Farge"], markersize=20)


for district_name in dots_gdf['Distrikt'].unique():
    district_dots = dots_gdf[dots_gdf['Distrikt'] == district_name]
    if district_dots.empty:
        continue

    minx, miny, maxx, maxy = district_dots.total_bounds
    width = maxx - minx
    height = maxy - miny

    rect = patches.Rectangle(
        (minx - 0.01, miny - 0.01),
        width + 0.02,
        height + 0.02,
        linewidth=0.5,
        edgecolor='gray',
        facecolor='none',
        linestyle='--'
    )
    ax.add_patch(rect)


for district_name in dots_gdf['Distrikt'].unique():
    district_geom_row = gdf[gdf['valgdistriktsnavn'] == district_name]
    district_dots = dots_gdf[dots_gdf['Distrikt'] == district_name]

    if district_geom_row.empty or district_dots.empty:
        continue

    map_centroid = district_geom_row.geometry.values[0].centroid
    dot_center = district_dots.geometry.unary_union.centroid

    ax.plot(
        [map_centroid.x, dot_center.x],
        [map_centroid.y, dot_center.y],
        color='gray',
        linewidth=0.5,
        linestyle='dotted'
    )


ax.set_title("Mandatfordeling per valgdistrikt", fontsize=14)
ax.axis("off")
st.pyplot(fig)












