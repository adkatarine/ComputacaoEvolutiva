# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:46 2020

@author: adlla
"""

from Populacao import Populacao
from Individuo import Individuo
from random import random

class AlgoritmoGenetico():
    
    def __init__(self):
        self.taxaCrossover = 0.6
        #self.crossover = 1
        self.taxaMutacao = 0.1
        self.mutar = 1
        self.geracoes = 3
        self.numPopulacao = 6
        
        self.populacao = Populacao(self.numPopulacao)
    
    ''' '''
    def executarAG(self):
        self.populacao.calcularRangeRoleta()
        self.populacao.printPopulacao()
        print()
        print()
        #for i in geracoes
        self.populacao.setListaDeIndividuos(self.crossover())
        self.populacao.fitnessTotal = 0
        self.populacao.calcularFitness()
        self.populacao.mediaPopulacao = 0
        self.populacao.calcularRangeRoleta()
        
        
        if(self.mutar != 0):
            self.mutacao()
        self.populacao.printPopulacao()
    
        

    ''' Sorteia número que irá escolher os pais na roleta para o crossover. '''
    def roleta(self):
        selecaoRoleta = random()*100
        
        for individuo in self.populacao.getListaDeIndividuos():
            faixaRoleta = individuo.getFaixaRoleta()
            if(selecaoRoleta >= faixaRoleta[0] and selecaoRoleta <= faixaRoleta[1]):
                return individuo
                
            
    ''' Cruzamento entre dois pais para criação de dois filhos. '''
    def crossover(self):
        novaGeracao = []
        #n= int(self.numPopulacao/2)
        for i in range(int(self.numPopulacao/2)):
            individuo_1 = self.roleta()
            individuo_2 = self.roleta()
            
            if(random() < self.taxaCrossover):
                pontoCorte = round(random() + len(individuo_1.getCromossomo()))
                
                filho_1 = individuo_2.getCromossomo()[0:pontoCorte] + individuo_1.getCromossomo()[pontoCorte::]
                filho_2 = individuo_1.getCromossomo()[0:pontoCorte] + individuo_2.getCromossomo()[pontoCorte::]
                
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
        
        
        
        
        
        return filhos
    
    
    def mutacao(self):
        for individuo in self.populacao.getListaDeIndividuos():
            individuo.mutarBit(self.taxaMutacao)


AG = AlgoritmoGenetico()
AG.executarAG()