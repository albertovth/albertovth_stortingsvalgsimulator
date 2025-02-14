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
        "Personer med stemmerett 2021"
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
    "Oslo": [
        "15.80%",
        "29.00%",
        "10.60%",
        "12.40%",
        "1.20%",
        "1.60%",
        "11.90%",
        "7.10%",
        "8.20%",
        "0.00%",
        "0.19%",
        "1.28%",
        "0.55%",
        "0.19%",
        "0.11%",
        "0.34%",
        "0.23%",
        "0.75%",
        "0.62%",
        "0.19%",
        "0.00%",
        "0.00%",
        "0.04%",
        "0.06%",
        "0.00%",
        "0.13%",
        "78.50%",
        "519846.1824"
    ],
    "Akershus": [
        "24.20%",
        "25.30%",
        "10.80%",
        "7.60%",
        "8.10%",
        "2.60%",
        "8.70%",
        "6.10%",
        "4.40%",
        "0.00%",
        "0.17%",
        "1.86%",
        "0.34%",
        "0.51%",
        "0.17%",
        "0.34%",
        "0.32%",
        "0.51%",
        "1.01%",
        "0.17%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "79.10%",
        "382290.526"
    ],
    "Hordaland": [
        "14.30%",
        "24.90%",
        "24.40%",
        "10.50%",
        "4.80%",
        "4.20%",
        "6.10%",
        "2.70%",
        "4.40%",
        "0.00%",
        "0.14%",
        "1.94%",
        "0.20%",
        "0.32%",
        "1.17%",
        "0.34%",
        "0.93%",
        "0.38%",
        "1.56%",
        "0.18%",
        "0.00%",
        "0.00%",
        "0.08%",
        "0.06%",
        "0.00%",
        "0.00%",
        "79.90%",
        "405549.144"
    ],
    "Rogaland": [
        "13.70%",
        "23.50%",
        "29.10%",
        "5.90%",
        "6.40%",
        "6.40%",
        "5.00%",
        "1.10%",
        "4.90%",
        "0.00%",
        "0.17%",
        "2.15%",
        "0.21%",
        "0.40%",
        "1.33%",
        "0.33%",
        "1.13%",
        "0.73%",
        "1.08%",
        "0.17%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "78.10%",
        "354417.23"
    ],
    "Sør-Trøndelag": [
        "21.20%",
        "21.30%",
        "18.00%",
        "12.90%",
        "7.10%",
        "1.60%",
        "4.20%",
        "4.60%",
        "6.70%",
        "0.00%",
        "0.18%",
        "1.45%",
        "0.00%",
        "0.28%",
        "0.57%",
        "0.21%",
        "0.26%",
        "0.38%",
        "2.90%",
        "0.18%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.05%",
        "0.00%",
        "0.00%",
        "78.50%",
        "261366.4574"
    ],
    "Østfold": [
        "27.50%",
        "17.80%",
        "15.90%",
        "7.70%",
        "12.90%",
        "2.80%",
        "3.10%",
        "4.40%",
        "5.00%",
        "0.00%",
        "0.19%",
        "2.55%",
        "0.31%",
        "0.43%",
        "0.24%",
        "0.28%",
        "0.75%",
        "0.36%",
        "2.05%",
        "0.16%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "73.00%",
        "236306.764"
    ],
    "Nordland": [
        "16.70%",
        "17.60%",
        "28.70%",
        "9.50%",
        "9.50%",
        "2.60%",
        "3.00%",
        "2.50%",
        "5.10%",
        "0.00%",
        "0.20%",
        "3.41%",
        "0.00%",
        "0.65%",
        "1.08%",
        "0.33%",
        "0.60%",
        "0.40%",
        "1.03%",
        "0.23%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.08%",
        "0.00%",
        "0.00%",
        "74.20%",
        "190577.9025"
    ],
    "Buskerud": [
        "22.20%",
        "26.20%",
        "23.70%",
        "5.20%",
        "6.80%",
        "2.00%",
        "3.50%",
        "2.60%",
        "4.00%",
        "0.00%",
        "0.21%",
        "2.98%",
        "0.19%",
        "0.62%",
        "0.41%",
        "0.36%",
        "0.49%",
        "0.67%",
        "0.79%",
        "0.19%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "75.20%",
        "202694.4549"
    ],
    "Møre og Romsdal": [
        "17.30%",
        "19.80%",
        "30.80%",
        "6.50%",
        "7.40%",
        "5.80%",
        "3.30%",
        "2.40%",
        "3.50%",
        "0.00%",
        "0.15%",
        "2.23%",
        "0.09%",
        "0.36%",
        "1.39%",
        "0.21%",
        "1.05%",
        "0.39%",
        "1.01%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "77.60%",
        "202879.473"
    ],
    "Hedmark": [
        "23.20%",
        "17.60%",
        "21.00%",
        "7.60%",
        "14.80%",
        "1.40%",
        "3.70%",
        "2.80%",
        "3.90%",
        "0.00%",
        "0.19%",
        "2.52%",
        "0.15%",
        "0.55%",
        "0.32%",
        "0.25%",
        "0.40%",
        "0.40%",
        "2.79%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "76.10%",
        "159458.83"
    ],
    "Vestfold": [
        "21.90%",
        "28.00%",
        "21.00%",
        "5.50%",
        "4.40%",
        "2.80%",
        "3.30%",
        "4.20%",
        "4.60%",
        "0.00%",
        "0.25%",
        "3.02%",
        "0.11%",
        "0.64%",
        "0.66%",
        "0.32%",
        "1.09%",
        "0.61%",
        "0.95%",
        "0.20%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "76.50%",
        "192054.1617"
    ],
    "Oppland": [
        "18.40%",
        "14.70%",
        "25.80%",
        "8.20%",
        "16.10%",
        "2.00%",
        "8.20%",
        "2.80%",
        "6.20%",
        "0.00%",
        "0.14%",
        "1.61%",
        "0.12%",
        "0.34%",
        "0.22%",
        "0.15%",
        "0.36%",
        "0.31%",
        "0.94%",
        "0.10%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "75.00%",
        "139028.6266"
    ],
    "Telemark": [
        "28.30%",
        "15.70%",
        "11.30%",
        "7.70%",
        "16.20%",
        "4.30%",
        "2.60%",
        "3.20%",
        "5.50%",
        "0.00%",
        "0.26%",
        "3.25%",
        "0.21%",
        "0.47%",
        "1.44%",
        "0.26%",
        "1.53%",
        "0.67%",
        "1.02%",
        "0.19%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "74.50%",
        "137369.697"
    ],
    "Vest-Agder": [
        "14.30%",
        "27.50%",
        "20.00%",
        "6.70%",
        "3.80%",
        "12.90%",
        "4.70%",
        "2.50%",
        "3.80%",
        "0.00%",
        "0.09%",
        "4.48%",
        "0.10%",
        "0.27%",
        "0.60%",
        "0.26%",
        "1.60%",
        "0.75%",
        "0.84%",
        "0.12%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "77.00%",
        "144490.5126"
    ],
    "Troms": [
        "19.00%",
        "14.00%",
        "30.30%",
        "13.30%",
        "5.60%",
        "1.80%",
        "3.30%",
        "1.30%",
        "7.90%",
        "0.00%",
        "0.18%",
        "3.30%",
        "0.31%",
        "0.53%",
        "0.75%",
        "0.44%",
        "0.44%",
        "0.42%",
        "0.00%",
        "0.20%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "75.00%",
        "128763.672"
    ],
    "Nord-Trøndelag": [
        "25.40%",
        "16.80%",
        "19.00%",
        "5.30%",
        "15.90%",
        "2.40%",
        "3.20%",
        "1.80%",
        "6.70%",
        "0.00%",
        "0.22%",
        "2.14%",
        "0.06%",
        "0.41%",
        "1.02%",
        "0.17%",
        "0.50%",
        "0.37%",
        "1.86%",
        "0.15%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "76.60%",
        "105287.4756"
    ],
    "Finnmark": [
        "19.60%",
        "10.70%",
        "28.80%",
        "7.30%",
        "4.70%",
        "0.60%",
        "2.00%",
        "2.60%",
        "8.30%",
        "0.00%",
        "0.26%",
        "3.41%",
        "0.00%",
        "0.57%",
        "0.93%",
        "0.34%",
        "0.71%",
        "0.34%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "25.89%",
        "0.00%",
        "72.00%",
        "57862.6368"
    ],
    "Aust-Agder": [
        "20.60%",
        "24.00%",
        "18.70%",
        "8.10%",
        "5.60%",
        "7.60%",
        "4.10%",
        "1.40%",
        "5.60%",
        "0.00%",
        "0.14%",
        "2.84%",
        "0.00%",
        "0.58%",
        "0.86%",
        "0.32%",
        "1.76%",
        "0.70%",
        "1.18%",
        "0.20%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "75.80%",
        "925.2927"
    ],
    "Sogn og Fjordane": [
        "23.40%",
        "17.60%",
        "10.80%",
        "6.20%",
        "21.80%",
        "3.40%",
        "3.50%",
        "3.00%",
        "7.90%",
        "0.00%",
        "0.14%",
        "1.50%",
        "0.00%",
        "0.30%",
        "0.93%",
        "0.16%",
        "0.83%",
        "0.47%",
        "0.59%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "0.00%",
        "79.70%",
        "81742.0644"
    ]
}
df = pd.DataFrame(default_values)

districts = [col for col in df.columns if col not in ['Parti', 'Kategori']]
email_address = "alberto@vthoresen.no"
import streamlit as st

st.title("Stortingsvalgsimulator")


st.markdown("""
###  Diagram for prognostisert mandatfordeling presenteres nederst i hovedsiden. For å se venstremnyen fra mobile enheter: utvid med pilen til venstre, for å justere prosentfordeling og valgdeltakelse per distrikt.
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
Per siste oppdatering 12. februar 2025 mangler to valgdistrikter nyere meningsmålinger. 
De siste tilgjengelige dataene for disse distriktene er fra 2021 eller 2022. 
Dette kan påvirke nøyaktigheten av prognosen. 
Nyere data vil bli inkludert etterhvert som de blir tilgjengelige. Oppdateringer vil bli gjort rundt en gang i måneden frem til sommeren 2025, og hyppigere rett før valget, som er i september 2025.
""")

# Diagram og instruksjoner
st.markdown("### Diagram og simulering")
st.markdown("Juster prognoser for valgresultater for valgdistriktene i venstremenyen. Valgdeltagelse per distrikt kan også oppgis nederst i venstremenyen. \n"
            "Utgangspunktet baseres på raden 'Siste lokale måling' som publiseres i [Poll of Polls](https://www.pollofpolls.no/?cmd=Stortinget&fylke=0), "
            "siste oppdatering per 7. januar 2025, med befolkningsprognoser for 2025 per valgdistrikt fra SSB. Diagram for prognostisert mandatfordeling presenteres nederst i hovedsiden.  \n"
            "Det kan ta litt tid før dette vises. Kategorien 'Andre' (partier), fra Poll of polls (Dvs. mindre partier, som ikke er R, SV, Ap, Sp, MDG, V, KrF, H og Frp) er ikke tatt med i beregningene. Men du kan justere prosent for disse partiene, eller oppdatere prosenten til de store partiene. Bare sørg for at prosent for alle partier i valgdistriktet summerer 100 prosent.")


# Kilder
st.markdown("### Kilder")
st.write("[Befolkningsprognosene fra SSB finner du her](https://www.ssb.no/en/befolkning/befolkningsframskrivinger/artikler/norways-2022-national-population-projections/_/attachment/inline/37d9dfef-1cd6-4390-b6ab-1601e21b32a8:1061870b3633187b8e861856f85e2dcc6638f666/RAPP2022-28_nasjfram%20ENG.pdf)")
st.write("[Tabeller for befolkningsvekst etter valgdistrikt](https://www.ssb.no/befolkning/befolkningsframskrivinger)")
st.write("[Poll of Polls](https://www.pollofpolls.no/?cmd=Stortinget&fylke=0)")

percentage_dict = {}
participation_dict = {}
st.sidebar.header("Her kan du endre prosent")
for distrikt in districts:
    if distrikt not in ['Prognostisert valgoppslutning per fylke - godkjente stemmer', 'Personer med stemmerett 2021']:
        st.sidebar.subheader(distrikt)
        for index, row in df.iterrows():
            if row['Parti'] not in ['Prognostisert valgoppslutning per fylke - godkjente stemmer', 'Personer med stemmerett 2021']:
                default_percentage = float(row[distrikt].strip('%'))
                modified_percentage = st.sidebar.slider(f"{row['Parti']} ({distrikt})", 0.0, 100.0, default_percentage)
                percentage_dict[(row['Parti'], distrikt)] = f"{modified_percentage}%"
st.sidebar.header("Her kan du endre deltagelse")
for distrikt in districts:
    if distrikt not in ['Personer med stemmerett 2021']:
        participation_row = df[df['Parti'] == 'Prognostisert valgoppslutning per fylke - godkjente stemmer']
        default_participation = float(participation_row[distrikt].values[0].strip('%'))
        modified_participation = st.sidebar.slider(f"Deltagelse ({distrikt})", 0.0, 100.0, default_participation)
        participation_dict[distrikt] = f"{modified_participation}%"
def calculate_stemmer(row, percentage_dict, participation_dict):
    stemmer_data = []
    for distrikt in districts:
        percentage = percentage_dict.get((row['Parti'], distrikt), row[distrikt])
        valgdeltakelse = participation_dict.get(distrikt, df[df['Parti'] == 'Prognostisert valgoppslutning per fylke - godkjente stemmer'][distrikt].values[0])
        personer_med_stemmerett = df[df['Parti'] == 'Personer med stemmerett 2021'][distrikt].values[0]
        
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
    if row['Parti'] not in ['Prognostisert valgoppslutning per fylke - godkjente stemmer', 'Personer med stemmerett 2021']:
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

def distribute_levelling_mandates(data_input, fixed_districts, national_result, threshold=0.04):
    votes_per_party = data_input.groupby('Parti')['Stemmer'].sum().reset_index().sort_values(by='Parti')
    votes = votes_per_party['Stemmer'].values
    parties_above_threshold = [votes_per_party['Parti'].iloc[i] for i in range(len(votes)) if votes[i] / sum(votes) >= threshold]
    
    district_mandates = data_input.groupby('Parti')['Distriktmandater'].sum().reindex(votes_per_party['Parti'], fill_value=0)
    
    national_result_df = pd.DataFrame({
        'Parti': votes_per_party['Parti'],
        'Mandater': national_result
    }).set_index('Parti')
    
    mandates_needed = national_result_df['Mandater'] - district_mandates
    eligible_parties = mandates_needed[(mandates_needed > 0) & (mandates_needed.index.isin(parties_above_threshold))].index.tolist()
    
    levelling_mandates = []
    used_districts = set()
    total_levelling_mandates_needed = 19
    
    while len(levelling_mandates) < total_levelling_mandates_needed and eligible_parties:
        best_value = 0
        best_party = None
        best_district = None
        parties_to_remove = []
        
        for district_index, district_row in fixed_districts.iterrows():
            if len(levelling_mandates) >= total_levelling_mandates_needed:
                break
            
            district = district_row['Fylke']
            if district in used_districts:
                continue
            
            district_votes = data_input[data_input['Distrikt'] == district].set_index('Parti')['Stemmer']
            district_factor = district_votes.sum() / district_row['Distriktmandater']
            
            for party_name in eligible_parties:
                if party_name not in district_votes:
                    continue

                current_district_mandates = data_input[(data_input['Parti'] == party_name) & (data_input['Distrikt'] == district)]['Distriktmandater'].sum()
                if current_district_mandates == 0:
                    current_value = district_votes[party_name] / district_factor
                else:
                    current_value = district_votes[party_name] / ((2 * current_district_mandates + 1) * district_factor)

                if current_value > best_value:
                    best_value = current_value
                    best_party = party_name
                    best_district = district

        if best_party and best_district:
            levelling_mandates.append({'Distrikt': best_district, 'Parti': best_party, 'Utjevningsmandater': 1})
            district_mandates[best_party] += 1
            mandates_needed[best_party] -= 1
            used_districts.add(best_district)
            
            if mandates_needed[best_party] <= 0:
                parties_to_remove.append(best_party)
                
            eligible_parties = [party for party in eligible_parties if party not in parties_to_remove]
    
    while len(levelling_mandates) < total_levelling_mandates_needed:
        best_value = 0
        best_party = None
        best_district = None
        
        for district_index, district_row in fixed_districts.iterrows():
            district = district_row['Fylke']
            if district in used_districts:
                continue
            
            district_votes = data_input[data_input['Distrikt'] == district].set_index('Parti')['Stemmer']
            district_factor = district_votes.sum() / district_row['Distriktmandater']
            
            for party_name in parties_above_threshold:
                if party_name not in district_votes:
                    continue
                
                current_district_mandates = data_input[(data_input['Parti'] == party_name) & (data_input['Distrikt'] == district)]['Distriktmandater'].sum()
                if current_district_mandates == 0:
                    current_value = district_votes[party_name] / district_factor
                else:
                    current_value = district_votes[party_name] / ((2 * current_district_mandates + 1) * district_factor)
                
                if current_value > best_value:
                    best_value = current_value
                    best_party = party_name
                    best_district = district

        if best_party and best_district:
            levelling_mandates.append({'Distrikt': best_district, 'Parti': best_party, 'Utjevningsmandater': 1})
            district_mandates[best_party] += 1
            mandates_needed[best_party] -= 1
            used_districts.add(best_district)
    
    return pd.DataFrame(levelling_mandates)


def calculate_district_mandates(data_input, fixed_districts):
    districts = fixed_districts['Fylke'].unique()
    district_mandates = pd.DataFrame(index=districts, columns=data_input['Parti'].unique())
    for district in districts:
        district_data = data_input[data_input['Distrikt'] == district]
        votes = district_data['Stemmer'].values
        seats = int(fixed_districts[fixed_districts['Fylke'] == district]['Distriktmandater'].values[0])
        if len(votes) == 0:
            continue  
        mandates = adjusted_sainte_lague(votes, seats)
        for i, party in enumerate(district_data['Parti'].unique()):
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
st.write("Hele landet som valgdistrikt:")
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

plot_half_circle_chart(aggregated_data, color_mapping)
