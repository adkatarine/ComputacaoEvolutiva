# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:46 2020

@author: adlla
"""
from Individuo import Individuo
from random import random

class AlgoritmoGenetico():
    
    def __init__(self):
        self.taxaCrossover = 0
        self.taxaMutacao = 0
        self.geracoes = 100
        self.numPopulacao = 100
        self.populacao = None
    
    def executarAG(self):
        pass
    
    ''' Sorteia número que irá escolher os pais na roleta para o crossover. '''
    def roleta(self):
        return random()*100
            
    
    def crossover(self, individuo_1, individuo_2):
        pontoCorte = round(random() + len(individuo_1.getCromossomo))
        
        filho_1 = individuo_2.getCromossomo[0:pontoCorte] + individuo_1.getCromossomo[pontoCorte::]
        filho_2 = individuo_1.getCromossomo[0:pontoCorte] + individuo_2.getCromossomo[pontoCorte::]
        
        

    def mutacao(self, individuo):
        for i in range(len(individuo.cromossomo)):
            if random() < self.taxaMutacao:
                if individuo.cromossomo[i] == '1':
                    individuo.cromossomo[i] = '0'
                else:
                    individuo.cromossomo[i] = '1'

if '__name__' == '__main__':
    pass