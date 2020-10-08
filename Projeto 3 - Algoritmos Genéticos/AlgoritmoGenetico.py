# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:46 2020

@author: adlla
"""

from Populacao import Populacao
from Individuo import Individuo
from random import random
import math
import matplotlib.pyplot as plt

class AlgoritmoGenetico():
    
    def __init__(self):
        self.taxaCrossover = 0.8
        self.taxaMutacao = 0
        self.geracoes = 100
        self.numPopulacao = 100
        
        self.populacao = Populacao(self.numPopulacao)
    
    def executarAG(self):
        print('GERAÇÃO 1')
        self.populacao.calcularRangeRoleta()
        self.populacao.printPopulacao()
        print('\n')
        for i in range(self.geracoes-1):
            print('GERAÇÃO {}'.format(i+2))
            self.populacao.setListaDeIndividuos(self.crossover())
        
            self.mutacao()
            self.populacao.fitnessTotal = 0
            self.populacao.calcularFitness()
            self.populacao.mediaPopulacao = 0
            self.populacao.calcularRangeRoleta()
            self.populacao.printPopulacao()
            print('\n\n')
        
        print('OS 10 MELHORES RESULTADOS: \n')
        for i in range(10):
            self.populacao.getListaDeIndividuos()[i].printCromossomo()
        
        print('Média de Aptidão da População: \n')
        print(self.populacao.getMediaPopulacao())
        
        self.plotGraficos()
        

    ''' Sorteia número que irá escolher os pais na roleta para o crossover. '''
    def roleta(self):
        selecaoRoleta = random()*100
        
        for individuo in self.populacao.getListaDeIndividuos():
            faixaRoleta = individuo.getFaixaRoleta()
            if(selecaoRoleta >= faixaRoleta[0] and selecaoRoleta <= faixaRoleta[1]):
                return individuo
        return self.populacao.getListaDeIndividuos()[0]
    
    def elitista(self):
         self.populacao.setListaDeIndividuos(sorted(self.getListaDeIndividuos(), key = Individuo.getFitnessPercent, reverse=True))
         
         for i in range(30):
             pass

    '''def torneio(self):
        for i in range(2):
            selecaoPai1 = round(random()*100)
            selecaoPai2 = selecaoPai1
            while(selecaoPai2 == selecaoPai1):
                selecaoPai2 = round(random()*100)'''   
          
    ''' Cruzamento entre dois pais para criação de dois filhos. '''
    def crossover_BaseadoEmOrdem(self, novaGeracao):
        for i in range(int(self.numPopulacao/2)):
            individuo_1 = self.roleta()
            individuo_2 = self.roleta()
            
            if(random() < self.taxaCrossover):
                filho_1 = self.mascara(individuo_1.getCromossomo(), individuo_2.getCromossomo())
                filho_2 = self.mascara(individuo_2.getCromossomo(), individuo_1.getCromossomo())
                
                filhos = [Individuo(), Individuo()]
                filhos[0].setCromossomo(filho_1)
                filhos[0].setGeracao(individuo_1.getGeracao())
                filhos[1].setCromossomo(filho_2)
                filhos[1].setGeracao(individuo_1.getGeracao())
                
                novaGeracao.append(filhos[0])
                novaGeracao.append(filhos[1])
            else:
                novaGeracao.append(individuo_1)
                novaGeracao.append(individuo_2)
        return novaGeracao
    
    def mascara(self, individuo, individuo2):
        mascara = []
        for i in range(8):
            if(random() < 0.5):
                self.mascara.append('0')
            else:
                self.mascara.append('1')
        
        filho = []
        listaAux = []
        for i in range(8):
            if(mascara[i] == '1'):
                filho[i] = individuo[i]
            else:
                filho[i] = 0
                listaAux.append(individuo[i])
        
        #listaAux é colocada em ordem
        
        for i in range(8):
            if(filho[i] == 0):
                filho[i] = listaAux[i]
        return filho
    
    
    def mutacao(self):
        for individuo in self.populacao.getListaDeIndividuos():
            individuo.mutarBit(self.taxaMutacao)
    
    ''' FUNÇÕES DO GRÁFICO. '''
    def funcao1(self, x):
        return 100 + math.fabs(x * math.sin(math.sqrt(math.fabs(x))))
   
    def plotFuncao1(self):
        y = []
        x = []
        for individuo in self.populacao.getListaDeIndividuos():
            i = individuo.getFenotipo()
            x.append(i)
            y.append(self.funcao1(i))
        plt.plot(x,y, color='r', linewidth=2.0)
    
    def plotPop(self):
        x_populacao = []
        y_populacao = []   
        for individuo in self.populacao.getListaDeIndividuos():
            x_populacao.append(individuo.getFenotipo())
            y_populacao.append(self.funcao1(individuo.getFenotipo()))
        plt.stem(x_populacao, y_populacao, use_line_collection=True)
    
    def plotGraficos(self):
        plt.title('Gerações', fontdict=None, loc='center', pad=None)
        self.plotFuncao1()
        self.plotPop()
        plt.show()
        
    
''' INICIALIZANDO AG. '''
AG = AlgoritmoGenetico()
AG.executarAG()