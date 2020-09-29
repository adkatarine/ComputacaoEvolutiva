# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:46 2020

@author: adlla
"""
#import Individuo as ind
#Individuo = ind.Individuo()
import Populacao as pop

from random import random

class AlgoritmoGenetico():
    
    def __init__(self):
        self.taxaCrossover = 0
        self.taxaMutacao = 0
        self.geracoes = 100
        self.numPopulacao = 5
        print('1')
        self.populacao = pop.Populacao(self.numPopulacao)
        print('AG')
    
    def executarAG(self):
        self.populacao.calcularRangeRoleta()
        self.populacao.printPopulacao()
        
        

    ''' Sorteia número que irá escolher os pais na roleta para o crossover. '''
    def roleta(self):
        return random()*100
            
    
    '''def crossover(self, individuo_1, individuo_2):
        pontoCorte = round(random() + len(individuo_1.getCromossomo))
        
        filho_1 = individuo_2.getCromossomo[0:pontoCorte] + individuo_1.getCromossomo[pontoCorte::]
        filho_2 = individuo_1.getCromossomo[0:pontoCorte] + individuo_2.getCromossomo[pontoCorte::]
        
        filhos = [Individuo(), Individuo()]
        
        filhos[0].setCromossomo(filho_1)
        filhos[0].setGeracao(individuo_1.getGeracao())
        
        filhos[1].setCromossomo(filho_2)
        filhos[1].setGeracao(individuo_1.getGeracao())
        
        return filhos
        
    '''
    
    def mutacao(self, individuo):
        pass


AG = AlgoritmoGenetico()
AG.executarAG()