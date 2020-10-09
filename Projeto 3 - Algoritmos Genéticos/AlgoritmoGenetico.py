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
        self.taxaMutacao = 0.1
        self.geracoes = 2
        self.numPopulacao = 6
        self.qtdElite = 2
        
        self.populacao = Populacao(self.numPopulacao)
    
    def executarAG(self):
        print('GERAÇÃO 1')
        self.populacao.calcularRangeRoleta()
        self.populacao.printPopulacao()
        print('\n')
        for i in range(self.geracoes-1):
            print('GERAÇÃO {}'.format(i+2))
            self.populacao.setListaDeIndividuos(self.elitista())
        
            self.mutacao_PermutacaoDeElementos()
            self.populacao.fitnessTotal = 0
            self.populacao.calcularFitness()
            self.populacao.mediaPopulacao = 0
            self.populacao.calcularRangeRoleta()
            self.populacao.printPopulacao()
            print('\n\n')
        
        '''print('OS 10 MELHORES RESULTADOS: \n')
        for i in range(10):
            self.populacao.getListaDeIndividuos()[i].printCromossomo()
        
        print('Média de Aptidão da População: \n')
        print(self.populacao.getMediaPopulacao())
        
        self.plotGraficos()'''
        

    ''' Sorteia número que irá escolher os pais na roleta para o crossover. '''
    def roleta(self):
        selecaoRoleta = random()*100
        
        for individuo in self.populacao.getListaDeIndividuos():
            faixaRoleta = individuo.getFaixaRoleta()
            if(selecaoRoleta >= faixaRoleta[0] and selecaoRoleta <= faixaRoleta[1]):
                return individuo
        return self.populacao.getListaDeIndividuos()[0]
    
    
    def elitista(self):
        self.populacao.setListaDeIndividuos(sorted(self.populacao.getListaDeIndividuos(), key = Individuo.getFitnessPercent))
        novaGeracao = []
         
        for i in range(self.qtdElite):
            novaGeracao.append(self.populacao.getListaDeIndividuos().pop())
        return self.crossover_BaseadoEmOrdem(novaGeracao)
 
          
    '''  '''
    def crossover_BaseadoEmOrdem(self, novaGeracao):
        for i in range(int(self.numPopulacao/2)):
            individuo_1 = self.roleta()
            individuo_2 = self.roleta()
            
            if(random() < self.taxaCrossover):
                filho_1 = self.crossover(individuo_1.getCromossomo(), individuo_2.getCromossomo())
                filho_2 = self.crossover(individuo_2.getCromossomo(), individuo_1.getCromossomo())
                
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
    
    def crossover(self, individuo, individuo2):
        mascara = []
        for i in range(8):
            if(random() < 0.5):
                mascara.append('0')
            else:
                mascara.append('1')
        
        filho = []
        listaAux = []
        #cromossomoAux = individuo.getCromossomo()
        cromossomoAux = [2,3,1,4,8,7,6,5]
        for i in range(8):
            if(mascara[i] == '1'):
                filho.append(cromossomoAux[i])
            else:
                filho.append(0)
                listaAux.append(cromossomoAux[i])
        
        #listaAux é colocada em ordem
        aux = 0
        for i in range(8):
            if(filho[i] == 0):
                filho[i] = listaAux[aux]
                aux = aux + 1
        return filho
    
    
    def mutacao_PermutacaoDeElementos(self):
        for individuo in self.populacao.getListaDeIndividuos():
            individuo.mutacao(self.taxaMutacao)
    
    ''' FUNÇÕES DO GRÁFICO. '''
    '''def distPontos(a, b):
        return math.sqrt((b[0] - a[0])*2 + (b[1] - a[1])*2)

    def printGrafico(x, y, ordem, geracao):
        plt.title(geracao, fontdict=None, loc='center', pad=None)
        printPontos(x, y)
        printPontoStart(x[0],y[0])
        printCaminhos(x, y, ordem)
        #plt.plot(media, color='b', linewidth=1.0)
        plt.show()
        
    def printPontos(x, y):
        plt.scatter(x, y, marker='o')    
    
    def printPontoStart(x, y):
        plt.scatter(x, y, color='r',marker='o')    
    
    def printCaminhos(x,y,ordem):
        x_c = []
        y_c = []
        for i in range(QUANTIDADE_PONTOS):
            x_c.append(x[ordem[i]])
            y_c.append(y[ordem[i]])
        plt.plot(x_c,y_c, color='r')
            
    def plotMedia(media):
        plt.title("Média Fitness", fontdict=None, loc='center', pad=None)
        plt.plot(media, color='b', linewidth=1.0)
        plt.show()
        self.cromossomo = [0] + random.sample(range(1,QUANTIDADE_PONTOS), QUANTIDADE_PONTOS-1)'''
    
''' INICIALIZANDO AG. '''
AG = AlgoritmoGenetico()
AG.executarAG()