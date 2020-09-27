# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:46:32 2020

@author: adlla
"""
from random import random
import math

class Individuo():
    
    def __init__(self):
        self.cromossomo = []
        self.fitness = 0
        self.fitnessPercent = 0
        self.faixaRoleta = 0
    
    ''' Inicia o cromossomo com 8 genes e valores aleatórios. '''
    def setCromossomo(self):
        for i in range(8):
            if(random() < 0.5):
                self.cromossomo.append('0')
            else:
                self.cromossomo.append('1')
    
    def getCromossomo(self):
        return self.cromossomo
    
    def setFitness(self, fitness):
        self.fitness = fitness
    
    def getFitness(self):
        return self.fitness
    
    def setFitnessPercent(self, fitnessPercent):
        self.fitnessPercent = fitnessPercent
        
    def getFitnessPercent(self):
        return self.fitnessPercent
    
    def setFaixaRoleta(self, faixaRoleta_1, faixaRoleta_2):
        self.faixaRoleta = '[' + faixaRoleta_1 + '   ' + faixaRoleta_1 + ']'
    
    def getFaixaRoleta(self):
        return self.faixaRoleta
    
    def mutarBit(self):
        pass
    
    def printCromossomo(self):
        print('Cromossomo: ' + self.cromossomo + ' Fitness: ' + self.fitness + 
              ' Porcentagem: ' + self.fitnessPercent + '%' + ' Roleta: ' + self.faixaRoleta)