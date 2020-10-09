# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:46:32 2020

@author: adlla
"""

from random import sample
import random

class Individuo:
    
    def __init__(self):
        self.cromossomo = []
        self.geracao = 0
        self.fitness = 0
        self.fitnessPercent = 0
        self.faixaRoleta = []
        
        self.cromossomo = sample(range(1, 9), 8)   

    def setCromossomo(self, cromossomo):
        self.cromossomo = cromossomo
    
    def getCromossomo(self):
        return self.cromossomo
    
    ''' Atualiza a geração do individuo. '''
    def setGeracao(self, geracao):
        self.geracao = geracao + 1
    
    def getGeracao(self):
        return self.geracao
    
    def setFitness(self, fitness):
        self.fitness = fitness
    
    def getFitness(self):
        return self.fitness
    
    def setFitnessPercent(self, fitnessPercent):
        self.fitnessPercent = fitnessPercent
        
    def getFitnessPercent(self):
        return self.fitnessPercent
    
    def setFaixaRoleta(self, faixaRoleta_1, faixaRoleta_2):
        if(len(self.faixaRoleta) != 0):
            self.faixaRoleta = []
        self.faixaRoleta.append(faixaRoleta_1)
        self.faixaRoleta.append(faixaRoleta_2)
    
    def getFaixaRoleta(self):
        return self.faixaRoleta
    
    ''' Faz a mutação(ou não) do cromossomo a partir da taxa de mutação. '''
    def mutacao(self, taxaMutacao):
        if(random.random() < taxaMutacao):
            index1 = random.randint(1, 7)
            index2 = index1
            while(index2 == index1):
                index2 = random.randint(1, 7)
            valorIndex1 = self.cromossomo[index1]
            self.cromossomo[index1] = self.cromossomo[index2]
            self.cromossomo[index2] = valorIndex1

    def printCromossomo(self):
        print('Cromossomo: {}  Fitness: {}  Porcentagem: {}%  Roleta: {}'. format(self.cromossomo,
                                                                  self.fitness, self.fitnessPercent, self.faixaRoleta))