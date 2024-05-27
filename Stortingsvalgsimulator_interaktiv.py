import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

default_values = {'Parti': ['Ap', 'H', 'FrP', 'SV', 'Sp', 'KrF', 'V', 'MDG', 'R', 'A', 'AfN', 'D', 'FNTB', 'Hp', 'IN', 'Lb', 'PdK', 'PS', 'Pp', 'PiP', 'Gp', 'RN', 'Kp', 'NKP', 'PF', 'FI', 'Prognostisert valgoppslutning per fylke - godkjente stemmer', 'Personer med stemmerett 2021'], 'Kategori': [4, 8, 10, 3, 5, 7, 6, 5.5, 1, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 0, 0], 'Oslo': ['23.00%', '23.50%', '6.00%', '13.30%', '3.11%', '1.81%', '10.00%', '8.50%', '8.30%', '0.00%', '0.10%', '0.68%', '0.29%', '0.10%', '0.06%', '0.18%', '0.12%', '0.40%', '0.33%', '0.10%', '0.00%', '0.00%', '0.02%', '0.03%', '0.00%', '0.07%', '78.50%', '519846.1824'], 'Akershus': ['25.80%', '27.40%', '10.50%', '6.80%', '8.81%', '2.00%', '6.90%', '4.70%', '3.90%', '0.00%', '0.10%', '1.10%', '0.20%', '0.30%', '0.10%', '0.20%', '0.19%', '0.30%', '0.60%', '0.10%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '79.10%', '382290.526'], 'Hordaland': ['22.70%', '24.50%', '12.60%', '8.90%', '9.90%', '4.90%', '4.30%', '3.90%', '4.70%', '0.00%', '0.07%', '0.96%', '0.10%', '0.16%', '0.58%', '0.17%', '0.46%', '0.19%', '0.77%', '0.09%', '0.00%', '0.00%', '0.04%', '0.03%', '0.00%', '0.00%', '79.90%', '405549.144'], 'Rogaland': ['22.40%', '23.90%', '16.80%', '5.10%', '10.40%', '8.10%', '3.50%', '2.36%', '3.69%', '0.00%', '0.08%', '1.03%', '0.10%', '0.19%', '0.64%', '0.16%', '0.54%', '0.35%', '0.52%', '0.08%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '78.10%', '354417.23'], 'Sør-Trøndelag': ['29.97%', '16.51%', '8.65%', '9.01%', '15.13%', '2.24%', '4.27%', '4.69%', '5.57%', '0.00%', '0.11%', '0.89%', '0.00%', '0.17%', '0.35%', '0.13%', '0.16%', '0.23%', '1.78%', '0.11%', '0.00%', '0.00%', '0.00%', '0.03%', '0.00%', '0.00%', '78.50%', '261366.4574'], 'Østfold': ['30.63%', '18.75%', '12.79%', '5.88%', '14.21%', '3.35%', '2.81%', '2.86%', '4.53%', '0.00%', '0.11%', '1.47%', '0.18%', '0.25%', '0.14%', '0.16%', '0.43%', '0.21%', '1.18%', '0.09%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '73.00%', '236306.764'], 'Nordland': ['28.98%', '15.40%', '12.29%', '6.93%', '21.33%', '1.96%', '2.36%', '2.20%', '5.37%', '0.00%', '0.08%', '1.36%', '0.00%', '0.26%', '0.43%', '0.13%', '0.24%', '0.16%', '0.41%', '0.09%', '0.00%', '0.00%', '0.00%', '0.03%', '0.00%', '0.00%', '74.20%', '190577.9025'], 'Buskerud': ['28.52%', '22.12%', '12.32%', '5.49%', '16.23%', '2.32%', '3.48%', '2.87%', '3.40%', '0.00%', '0.10%', '1.39%', '0.09%', '0.29%', '0.19%', '0.17%', '0.23%', '0.31%', '0.37%', '0.09%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '75.20%', '202694.4549'], 'Møre og Romsdal': ['20.14%', '16.36%', '22.36%', '6.07%', '17.53%', '5.38%', '2.83%', '2.35%', '3.29%', '0.00%', '0.08%', '1.19%', '0.05%', '0.19%', '0.74%', '0.11%', '0.56%', '0.21%', '0.54%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '77.60%', '202879.473'], 'Hedmark': ['33.33%', '10.60%', '8.50%', '6.66%', '28.27%', '1.62%', '2.18%', '1.95%', '3.31%', '0.00%', '0.09%', '1.19%', '0.07%', '0.26%', '0.15%', '0.12%', '0.19%', '0.19%', '1.32%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '76.10%', '159458.83'], 'Vestfold': ['26.99%', '25.21%', '12.55%', '6.04%', '10.02%', '3.50%', '3.99%', '3.85%', '4.41%', '0.00%', '0.11%', '1.33%', '0.05%', '0.28%', '0.29%', '0.14%', '0.48%', '0.27%', '0.42%', '0.09%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '76.50%', '192054.1617'], 'Oppland': ['35.21%', '12.48%', '8.62%', '5.31%', '26.15%', '1.57%', '2.28%', '2.16%', '3.70%', '0.00%', '0.08%', '0.94%', '0.07%', '0.20%', '0.13%', '0.09%', '0.21%', '0.18%', '0.55%', '0.06%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '75.00%', '139028.6266'], 'Telemark': ['31.02%', '15.74%', '12.80%', '5.91%', '16.61%', '4.48%', '2.15%', '2.68%', '4.60%', '0.00%', '0.11%', '1.40%', '0.09%', '0.20%', '0.62%', '0.11%', '0.66%', '0.29%', '0.44%', '0.08%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '74.50%', '137369.697'], 'Vest-Agder': ['20.83%', '21.36%', '13.29%', '5.17%', '10.42%', '13.88%', '3.53%', '3.05%', '3.15%', '0.00%', '0.05%', '2.61%', '0.06%', '0.16%', '0.35%', '0.15%', '0.93%', '0.44%', '0.49%', '0.07%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '77.00%', '144490.5126'], 'Troms': ['27.21%', '13.71%', '14.11%', '10.63%', '19.14%', '2.22%', '2.39%', '2.88%', '4.75%', '0.00%', '0.08%', '1.49%', '0.14%', '0.24%', '0.34%', '0.20%', '0.20%', '0.19%', '0.00%', '0.09%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '75.00%', '128763.672'], 'Nord-Trøndelag': ['33.72%', '10.63%', '8.07%', '5.46%', '29.07%', '2.26%', '1.96%', '1.74%', '3.90%', '0.00%', '0.10%', '0.99%', '0.03%', '0.19%', '0.47%', '0.08%', '0.23%', '0.17%', '0.86%', '0.07%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '76.60%', '105287.4756'], 'Finnmark': ['31.61%', '6.76%', '10.93%', '5.88%', '18.32%', '1.65%', '1.36%', '2.19%', '4.87%', '0.00%', '0.13%', '1.73%', '0.00%', '0.29%', '0.47%', '0.17%', '0.36%', '0.17%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '13.12%', '0.00%', '72.00%', '57862.6368'], 'Aust-Agder': ['24.62%', '20.26%', '13.38%', '5.39%', '13.60%', '8.78%', '3.14%', '2.88%', '3.69%', '0.00%', '0.07%', '1.42%', '0.00%', '0.29%', '0.43%', '0.16%', '0.88%', '0.35%', '0.59%', '0.10%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '75.80%', '925.2927'], 'Sogn og Fjordane': ['26.50%', '13.88%', '9.42%', '5.59%', '28.74%', '3.89%', '3.27%', '2.32%', '3.97%', '0.00%', '0.07%', '0.74%', '0.00%', '0.15%', '0.46%', '0.08%', '0.41%', '0.23%', '0.29%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '0.00%', '79.70%', '81742.0644']}
df = pd.DataFrame(default_values)

districts = [col for col in df.columns if col not in ['Parti', 'Kategori']]
email_address = "alberto@vthoresen.no"
st.title("Interaktiv valgsimulator")
st.markdown(f"Kontakt: [Alberto Valiente Thoresen](mailto:{email_address})")
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
        19, 18, 15, 13, 9, 8, 8, 7, 7, 6, 6, 5, 5, 5, 5, 4, 4, 3, 3
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
    parties_above_threshold = [i for i in range(len(votes)) if votes[i] / sum(votes) >= threshold]
    
    district_mandates = data_input.groupby('Parti')['Distriktmandater'].sum().reindex(votes_per_party['Parti'], fill_value=0)
    
    national_result_df = pd.DataFrame({
        'Parti': votes_per_party['Parti'],
        'Mandater': national_result
    }).set_index('Parti')
    
    mandates_needed = national_result_df['Mandater'] - district_mandates
    
    eligible_parties = mandates_needed[mandates_needed > 0 & & (mandates_needed.index.isin(parties_above_threshold))].index.tolist().index.tolist()
    
    levelling_mandates = []
    used_districts = set()
    for district_index, district_row in fixed_districts.iterrows():
        district = district_row['Fylke']
        if district in used_districts:
            continue
        district_votes = data_input[data_input['Distrikt'] == district].set_index('Parti')['Stemmer']
        district_factor = district_votes.sum() / district_row['Distriktmandater']
       
        best_value = 0
        best_party = None
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
            if best_party:
                levelling_mandates.append({'Distrikt': district, 'Parti': best_party, 'Utjevningsmandater': 1})
                district_mandates[best_party] += 1
                mandates_needed[best_party] -= 1
                used_districts.add(district)
            
                if mandates_needed[best_party] <= 0:
                    eligible_parties.remove(best_party)
            
                if len(levelling_mandates) >= fixed_districts['Utjevningsmandater'].sum():
                    break
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
       
        
        label = ax.text(x * 0.7, y * 0.7, f"{aggregated_data['Parti'].iloc[i]}: {aggregated_data['TotalMandater'].iloc[i]}",
                        horizontalalignment='center', verticalalignment='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none"))
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
plot_half_circle_chart(aggregated_data, color_mapping)
