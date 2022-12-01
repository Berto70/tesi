#import required module
#import os
import numpy as np
import glob 
import pandas as pd
import matplotlib.pyplot as plt

chi_quadro_tot = []
filename_list = []
filenames = glob.glob('analoghi\spettri/*.tab')
filenames = filenames[34:37]
for filename in filenames:
    print(filename)
    #leggo i file grezzo, saltando la prima riga e le ultime.
    raw_data = pd.read_csv(filename, skiprows=1, skipfooter=10, index_col=False, names = ['lungh_onda', 'riflettanza'], sep='   ', engine='python')
    #dat.to_csv(sep=',', encoding='utf-8', index=False, header=False, quoting=csv.QUOTE_ALL)
    #dat.columns=['lungh_onda']

    #creo due liste separate per la lunghezza d'onda e il valore relativo di riflettanza
    lungh_onda = raw_data['lungh_onda']
    riflettanza = raw_data['riflettanza']

    #selezioni i dati da 330 a 1100 nm
    lungh_onda_select = lungh_onda.iloc[6:161]
    riflettanza_select = riflettanza.iloc[6:161]

    #creo un dataframe con i dati selezionati
    data = {'lungh_onda_select': lungh_onda_select, 'riflettanza_select': riflettanza_select}
    data_select = pd.DataFrame(data=data)

    #print (data_select)

    #normalizzo a 550nm
    lungh_onda_norm = lungh_onda_select
    riflettanza_norm = riflettanza_select/riflettanza_select[50]

    #creo un dataframe con i dati normalizzati
    data_norm = {'lungh_onda_norm': lungh_onda_norm, 'riflettanza_norm': riflettanza_norm}
    data_select_norm = pd.DataFrame(data=data_norm)

    print (data_select_norm)

    #plotto il grafico dello spettro di riflettanza normalizzato
    # plt.plot(lungh_onda_norm, riflettanza_norm)
    # plt.xlabel('Lunghezza d\'onda [$nm$]')
    # plt.ylabel('Riflettanza')
    # plt.title('filename')
    # plt.show()

    # print(raw_data)
    # print (dat.head())
    
    #dati dello spettro di Didymos con cui confrontare
    
    spettro = pd.read_csv('analoghi\spettri/bkrbmt312.tab', skiprows=1, skipfooter=10, index_col=False, names = ['lungh_onda', 'riflettanza'], sep='   ', engine='python')
    spettro_onda = spettro['lungh_onda']
    spettro_riflettanza = spettro['riflettanza']

    #seleziono i dati da 330 a 1100 nm
    spettro_onda_select = spettro_onda.iloc[6:161]
    spettro_riflettanza_select = spettro_riflettanza.iloc[6:161]

    #creo un dataframe con i dati selezionati
    spettro_data = {'spettro_onda_select': spettro_onda_select, 'spettro_riflettanza_select': spettro_riflettanza_select}
    spettro_data_select = pd.DataFrame(data=spettro_data)

    #print (data_select)

    #normalizzo a 550nm
    spettro_onda_norm = spettro_onda_select
    spettro_riflettanza_norm = spettro_riflettanza_select/spettro_riflettanza_select[50]

    #creo un dataframe con i dati normalizzati
    spettro_data_norm = {'spettro_onda_norm': spettro_onda_norm, 'spettro_riflettanza_norm': spettro_riflettanza_norm}
    spettro_data_select_norm = pd.DataFrame(data=spettro_data_norm)
    
    #chi quadro
    
    chi_quadro = np.sum((spettro_riflettanza_norm-riflettanza_norm)**2/(riflettanza_norm))
    print('\u03C7^2= ', chi_quadro)
    
    #plotto gli spettri normalizzati di Didymos (verde) e quello dell'analogo (rosso)
    plt.plot(lungh_onda_norm, riflettanza_norm, color='red')
    plt.plot(spettro_onda_norm, spettro_riflettanza_norm, color='green')
    plt.xlabel('Lunghezza d\'onda [$nm$]')
    plt.ylabel('Riflettanza')
    plt.title(filename)
    plt.show()

    
    chi_quadro_tot.append(chi_quadro)
    filename_list.append(filename)

confronto_finale = {'filename':filename_list, 'chi_quadro': chi_quadro_tot}

confronto_list = pd.DataFrame(data=confronto_finale)
confronto_list_sorted = pd.DataFrame.sort_values(confronto_list, by=['chi_quadro'], ascending=True)

print (confronto_list_sorted)