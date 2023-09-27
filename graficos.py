import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def plot2D(df,dfFLC,dfFLEV1,dfFLEV2,dfFLEV3,dfFLEV4,filename):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  X1 = dfFLC['n']
  X2 = dfFLEV1['n']
  X3 = dfFLEV2['n']
  X4 = dfFLEV3['n']
  X5 = dfFLEV4['n']
  Y1 = dfFLC['C(n)']
  Y2 = dfFLEV1['C(n)']
  Y3 = dfFLEV2['C(n)']
  Y4 = dfFLEV3['C(n)']
  Y5 = dfFLEV4['C(n)']

  # Plote as três funções em 3D usando plot_surface
  ax.plot(X1, Y1, label="C(n) - FLC")
  ax.plot(X2, Y2, label="C(n) - FLEV1")
  ax.plot(X3, Y3, label="C(n) - FLEV2")
  ax.plot(X4, Y4, label="C(n) - FLEV3")
  ax.plot(X5, Y5, label="C(n) - FLEV4")

  # Configuração dos rótulos dos eixos
  ax.set_xlabel('Quantidade de itens (n)')
  ax.set_ylabel(f'Execuções da operação básica (C(n))')
  plt.legend()
  plt.savefig(filename)

  plt.show()
for arq,file in [
   ('dados_pior_caso.csv','imagens/pior_caso'),
                 ('dados_melhor_caso.csv','imagens/melhor_caso')]:
    df = pd.read_csv('csvs\\'+arq)
    dfFLC =df[df['Fila'] == 'FLC']
    dfFLEV1 = df[df['Fila'] == 'FLEV1']
    dfFLEV2 = df[df['Fila'] == 'FLEV2']
    dfFLEV3 = df[df['Fila'] == 'FLEV3']
    dfFLEV4 = df[df['Fila'] == 'FLEV4']
    print(df)
    plot2D(df,dfFLC,dfFLEV1,dfFLEV2,dfFLEV3,dfFLEV4,file)
    plot2D(df,dfFLC,dfFLEV1,dfFLEV2,dfFLEV3,dfFLEV4,file)