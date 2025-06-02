import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
st.set_page_config(layout="wide")


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
    "30.90%",
    "16.20%",
    "24.00%",
    "4.70%",
    "6.90%",
    "2.60%",
    "2.30%",
    "3.10%",
    "4.30%",
    "0.00%",
    "0.13%",
    "1.74%",
    "0.21%",
    "0.29%",
    "0.16%",
    "0.19%",
    "0.52%",
    "0.24%",
    "1.40%",
    "0.11%",
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
    "30.40%",
    "23.90%",
    "17.80%",
    "5.90%",
    "2.90%",
    "1.90%",
    "5.90%",
    "4.10%",
    "4.40%",
    "0.00%",
    "0.09%",
    "1.00%",
    "0.18%",
    "0.28%",
    "0.09%",
    "0.18%",
    "0.17%",
    "0.28%",
    "0.54%",
    "0.09%",
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
    "25.30%",
    "22.40%",
    "12.70%",
    "10.80%",
    "0.50%",
    "1.60%",
    "9.40%",
    "6.10%",
    "8.40%",
    "0.00%",
    "0.06%",
    "0.41%",
    "0.18%",
    "0.06%",
    "0.03%",
    "0.11%",
    "0.08%",
    "0.24%",
    "0.20%",
    "0.06%",
    "0.00%",
    "0.00%",
    "0.01%",
    "0.02%",
    "0.00%",
    "0.04%",
    "78.50%",
    "584525"
  ],
  "Hedmark": [
    "38.20%",
    "11.40%",
    "17.50%",
    "5.50%",
    "13.90%",
    "1.70%",
    "2.10%",
    "1.50%",
    "4.80%",
    "0.00%",
    "0.09%",
    "1.13%",
    "0.07%",
    "0.25%",
    "0.14%",
    "0.11%",
    "0.18%",
    "0.18%",
    "1.25%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "76.10%",
    "171890"
  ],
  "Oppland": [
    "35.30%",
    "12.30%",
    "17.70%",
    "5.50%",
    "15.90%",
    "1.70%",
    "1.90%",
    "1.70%",
    "4.40%",
    "0.00%",
    "0.12%",
    "1.39%",
    "0.10%",
    "0.29%",
    "0.19%",
    "0.12%",
    "0.31%",
    "0.27%",
    "0.81%",
    "0.08%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "75.00%",
    "144052"
  ],
  "Buskerud": [
    "30.40%",
    "18.40%",
    "24.60%",
    "4.50%",
    "7.30%",
    "1.30%",
    "3.50%",
    "2.60%",
    "4.20%",
    "0.00%",
    "0.09%",
    "1.34%",
    "0.08%",
    "0.28%",
    "0.19%",
    "0.16%",
    "0.22%",
    "0.30%",
    "0.35%",
    "0.08%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "75.20%",
    "215155"
  ],
  "Vestfold": [
    "30.70%",
    "20.80%",
    "22.20%",
    "5.00%",
    "3.90%",
    "3.60%",
    "3.90%",
    "2.10%",
    "4.10%",
    "0.00%",
    "0.12%",
    "1.42%",
    "0.05%",
    "0.30%",
    "0.31%",
    "0.15%",
    "0.51%",
    "0.29%",
    "0.45%",
    "0.09%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "76.50%",
    "206304"
  ],
  "Telemark": [
    "32.60%",
    "12.50%",
    "22.90%",
    "5.40%",
    "5.30%",
    "4.50%",
    "2.20%",
    "2.30%",
    "6.90%",
    "0.00%",
    "0.15%",
    "1.88%",
    "0.12%",
    "0.28%",
    "0.84%",
    "0.15%",
    "0.89%",
    "0.39%",
    "0.59%",
    "0.11%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "74.50%",
    "143336"
  ],
  "Aust-Agder": [
    "26.00%",
    "16.80%",
    "25.10%",
    "4.40%",
    "7.50%",
    "6.50%",
    "3.20%",
    "1.20%",
    "3.90%",
    "0.00%",
    "0.09%",
    "1.79%",
    "0.00%",
    "0.37%",
    "0.54%",
    "0.20%",
    "1.11%",
    "0.44%",
    "0.74%",
    "0.13%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "75.80%",
    "100920"
  ],
  "Vest-Agder": [
    "25.00%",
    "16.80%",
    "26.50%",
    "4.30%",
    "3.00%",
    "11.10%",
    "3.20%",
    "1.90%",
    "2.70%",
    "0.00%",
    "0.06%",
    "2.76%",
    "0.06%",
    "0.16%",
    "0.37%",
    "0.16%",
    "0.99%",
    "0.46%",
    "0.52%",
    "0.07%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "77.00%",
    "151621"
  ],
  "Rogaland": [
    "24.20%",
    "20.80%",
    "26.00%",
    "3.60%",
    "5.60%",
    "7.90%",
    "2.10%",
    "1.30%",
    "5.10%",
    "0.00%",
    "0.08%",
    "0.95%",
    "0.09%",
    "0.18%",
    "0.59%",
    "0.14%",
    "0.50%",
    "0.32%",
    "0.47%",
    "0.08%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "78.10%",
    "385280"
  ],
  "Hordaland": [
    "26.60%",
    "18.90%",
    "21.40%",
    "7.00%",
    "4.20%",
    "4.50%",
    "4.80%",
    "3.80%",
    "5.70%",
    "0.00%",
    "0.06%",
    "0.83%",
    "0.08%",
    "0.13%",
    "0.50%",
    "0.14%",
    "0.40%",
    "0.16%",
    "0.67%",
    "0.08%",
    "0.00%",
    "0.00%",
    "0.03%",
    "0.03%",
    "0.00%",
    "0.00%",
    "79.90%",
    "429219"
  ],
  "Sogn og Fjordane": [
    "32.50%",
    "12.80%",
    "17.50%",
    "5.90%",
    "14.00%",
    "2.90%",
    "4.20%",
    "1.80%",
    "5.60%",
    "0.00%",
    "0.08%",
    "0.89%",
    "0.00%",
    "0.17%",
    "0.55%",
    "0.09%",
    "0.49%",
    "0.28%",
    "0.35%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "79.70%",
    "86091"
  ],
  "Møre og Romsdal": [
    "23.70%",
    "15.20%",
    "30.50%",
    "6.00%",
    "7.50%",
    "5.40%",
    "2.30%",
    "1.90%",
    "4.40%",
    "0.00%",
    "0.07%",
    "1.00%",
    "0.04%",
    "0.16%",
    "0.63%",
    "0.10%",
    "0.47%",
    "0.17%",
    "0.45%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "77.60%",
    "214398"
  ],
  "Sør-Trøndelag": [
    "32.60%",
    "16.40%",
    "18.00%",
    "9.10%",
    "6.00%",
    "2.20%",
    "2.60%",
    "3.40%",
    "5.30%",
    "0.00%",
    "0.12%",
    "0.96%",
    "0.00%",
    "0.19%",
    "0.38%",
    "0.14%",
    "0.17%",
    "0.26%",
    "1.93%",
    "0.12%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.03%",
    "0.00%",
    "0.00%",
    "78.50%",
    "274004"
  ],
  "Nord-Trøndelag": [
    "36.10%",
    "12.60%",
    "15.00%",
    "6.00%",
    "14.60%",
    "2.30%",
    "1.90%",
    "0.80%",
    "5.30%",
    "0.00%",
    "0.17%",
    "1.64%",
    "0.04%",
    "0.31%",
    "0.79%",
    "0.13%",
    "0.39%",
    "0.29%",
    "1.43%",
    "0.11%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "76.60%",
    "111357"
  ],
  "Nordland": [
    "31.60%",
    "16.20%",
    "22.40%",
    "6.30%",
    "7.40%",
    "2.60%",
    "0.70%",
    "2.70%",
    "7.90%",
    "0.00%",
    "0.06%",
    "0.98%",
    "0.00%",
    "0.19%",
    "0.31%",
    "0.10%",
    "0.17%",
    "0.11%",
    "0.30%",
    "0.07%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.02%",
    "0.00%",
    "0.00%",
    "74.20%",
    "193595"
  ],
  "Troms": [
    "34.00%",
    "12.00%",
    "24.60%",
    "8.10%",
    "4.80%",
    "1.60%",
    "1.90%",
    "2.90%",
    "6.50%",
    "0.00%",
    "0.10%",
    "1.76%",
    "0.17%",
    "0.28%",
    "0.40%",
    "0.23%",
    "0.23%",
    "0.22%",
    "0.00%",
    "0.11%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "75.00%",
    "136080"
  ],
  "Finnmark": [
    "31.10%",
    "6.70%",
    "23.30%",
    "7.90%",
    "5.50%",
    "0.80%",
    "2.30%",
    "0.70%",
    "5.20%",
    "0.00%",
    "0.12%",
    "1.50%",
    "0.00%",
    "0.25%",
    "0.41%",
    "0.15%",
    "0.31%",
    "0.15%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "0.00%",
    "11.41%",
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
###  Diagram for prognostisert mandatfordeling presenteres nederst i hovedsiden. For å se venstremnyen fra mobile enheter: utvid med pilen til venstre. Da kan du justere prosentfordeling og valgdeltakelse per distrikt.
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
st.warning("""
**Viktig melding:**
Per siste oppdatering 28. mai 2025 er eldste meningsmåling fra 22. mai 2025 og nyeste fra 26. mai 2025.
Nyere data vil bli inkludert etterhvert som de blir tilgjengelige. Oppdateringer vil bli gjort rundt en gang i måneden frem til sommeren 2025, og hyppigere rett før valget, som er i september 2025.
Merk også at kategorien "Andre" i Poll of polls omfatter flere partier. Dette fordeles proporsjonelt til "Andre" partier som deltok ved forrige valg, ifølge stemmene de fikk. Dette er ikke presis, men det er bedre enn å behandle hele kategorien "Andre" som ett parti.
""")

# Diagram og instruksjoner
st.markdown("### Diagram og simulering")
st.markdown("Juster prognoser for valgresultater for valgdistriktene i venstremenyen. Valgdeltagelse per distrikt kan også oppgis nederst i venstremenyen. \n"
            "Utgangspunktet baseres på raden 'Siste lokale måling' som publiseres i [Poll of Polls](https://www.pollofpolls.no/?cmd=Stortinget&fylke=0), "
            "siste oppdatering per 28. mai 2025, med estimater for antall personer med stemmerett per valgdistrikt basert på tall for 2023 og ekstrapolering av befolkningsvekst (kilde SSB). Diagram for prognostisert mandatfordeling presenteres nederst i hovedsiden.  \n"
            "Det kan ta litt tid før dette vises. Kategorien 'Andre' (partier), fra Poll of polls (Dvs. mindre partier, som ikke er R, SV, Ap, Sp, MDG, V, KrF, H og Frp) fordeles proporsjonelt til andre partier som deltok i Stortingsvalget 2021, basert på resultatet disse partiene fikk da. Du kan justere prosent for disse partiene, eller oppdatere prosenten til de store partiene i venstremenyen. For bedre resultater sørg for at prosentandel for alle partier i valgdistriktet summerer 100 prosent.")


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


st.sidebar.header("Her kan du endre prosent")
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
st.write("### Simulerte valgresultater")
st.dataframe(results_df)
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

    # 0) EKSKLUDER IKKE-POLITISKE RADER (f.eks. prognoser og velger-tall)
    ikke_partier = [
        'Prognostisert valgoppslutning per fylke - godkjente stemmer',
        'Personer med stemmerett 2025'
    ]
    real_data = data_input[~data_input['Parti'].isin(ikke_partier)].copy()

    # 1) NASJONALE STEMMER FOR ALLE “REELLE” PARTIER
    all_votes = real_data.groupby('Parti')['Stemmer'].sum()
    total_votes = all_votes.sum()

    # 2) FINN PARTIER SOM HAR ≥ 4 % NASJONALT OG STO PÅ LISTE I ALLE FYLKER (§ 11-7(2))
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

    # 3) HENT DISTRIKTSMANDATER FOR ALLE PARTIER (brukes til under4-trekking + overheng-sjekk)
    district_mandates_full = real_data.groupby('Parti')['Distriktmandater'].sum()

    # 4) KJØR NASJONAL SAINTE-LAGUË + OVERHENG-LOOP (§ 11-7(3–5))
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
            if district_mandates_4pct[P] > nasjonalt_df.loc[P, 'Mandater']
        ]

        if not overhang:
            break

        for P in overhang:
            st.info(
                f"Parti {P} fjernes fra utjevning (overheng: "
                f"{int(district_mandates_4pct[P])} distriktsmandater > "
                f"{int(nasjonalt_df.loc[P, 'Mandater'])} nasjonale mandater)."
            )
            gjeldende_partier.remove(P)

        if not gjeldende_partier:
            return pd.DataFrame(columns=['Distrikt', 'Parti', 'Utjevningsmandater'])

    # 5) BEREGN ENDLIG UTJEVNINGSBEHOV = nasjonalt_df[P] − district_mandates_4pct[P]
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

    # 6) FOR DYNAMISK FYLKESVIS UTVEILNGSMANDAT-TILDELING
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

    # 7) DEL UT 19 UTVEVNINGSMANDATER ÉN‐FOR‐ÉN (maks én per fylke, aldri mer enn behov per parti)
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
            st.info(f"Utjevningsmandat {len(levelling_list)}/19: Parti {best_P} tildeles i fylke {best_D}.")
            leveling_needs[best_P] -= 1
            used_districts.add(best_D)
            district_mandates_by_PD[(best_P, best_D)] = district_mandates_by_PD.get((best_P, best_D), 0) + 1
        else:
            break

    # 8) MELDINGER OG RETUR
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
st.write("Data med beregnede 'Distriktmandater':")
st.write(results_df)
levelling_mandates_df = distribute_levelling_mandates(results_df, fixed_districts, national_result)

validate_used_districts(set(levelling_mandates_df['Distrikt']))

st.write("Utjevningsmandater per distrikt:")
st.write(levelling_mandates_df)
results_df = results_df.merge(levelling_mandates_df, on=['Distrikt', 'Parti'], how='left')
results_df['Utjevningsmandater'] = results_df['Utjevningsmandater'].fillna(0).astype(int)
st.write("Data med beregnede'Utjevningsmandater':")
st.write(results_df)
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
st.subheader('Resultat etter valgdistrikt')
st.write(results_df)
aggregated_data = results_df.groupby(['Parti']).agg({
    'Stemmer': 'sum',
    'Distriktmandater': 'sum',
    'Utjevningsmandater': 'sum',
    'TotalMandater': 'sum',
    'Kategori': 'first'  
}).reset_index()
st.subheader('Resultat for hele landet')
st.write(aggregated_data)
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


plot_half_circle_chart(aggregated_data, color_mapping)
