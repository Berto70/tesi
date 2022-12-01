#importo i pacchetti
import numpy as np
import pandas as pd
#import csv
#from sklearn import preprocessing
import matplotlib.pyplot as plt

def confronto_spettri(file_name): 
    
    #leggo i file grezzo, saltando la prima riga e le ultime.
    raw_data = pd.read_csv(file_name, skiprows=1, skipfooter=10, index_col=False, names = ['lungh_onda', 'riflettanza'], sep='   ', engine='python')
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
    
    print (data_select)
    
    # d = preprocessing.normalize(data_select)
    # scaled_df = pd.DataFrame(d, columns = ['lungh_onda_norm', 'riflettanza_norm'])
    # print (scaled_df.head())
    
    #normalizzo a 550nm
    lungh_onda_norm = lungh_onda_select
    riflettanza_norm = riflettanza_select/riflettanza_select[50]
    
    #creo un dataframe con i dati normalizzati
    data_norm = {'lungh_onda_norm': lungh_onda_norm, 'riflettanza_norm': riflettanza_norm}
    data_select_norm = pd.DataFrame(data=data_norm)
    
    print (data_select_norm)
    
    #creo il grafico dello spettro di riflettanza normalizzato
    plt.plot(lungh_onda_norm, riflettanza_norm)
    plt.xlabel('Lunghezza d\'onda [$nm$]')
    plt.ylabel('Riflettanza')
    plt.title('filename')
    plt.show()
    
    # print(raw_data)
    # print (dat.head())
    
file_name = input('Inserisci il nome del file: ')

