# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:46:32 2020

@author: adlla
"""
from random import random

class Individuo:
    
    def __init__(self):
        self.cromossomo = []
        self.fenotipo = 0
        self.geracao = 0
        self.fitness = 0
        self.fitnessPercent = 0
        self.faixaRoleta = []
        
        self.setCromossomo()
    
    ''' Inicia o cromossomo com 8 genes e valores aleatórios. '''
    def setCromossomo(self):
        for i in range(3):
            if(random() < 0.5):
                self.cromossomo.append(0)
            else:
                self.cromossomo.append(1)
        self.setFenotipo(self.cromossomo)
        #print('INDIVIDUO CRIADO')
    
    def getCromossomo(self):
        return self.cromossomo
    
    ''' Calcula o fenotipo a partir do cromossomo. '''
    def setFenotipo(self, cromossomo):
        decimal = 0
        for i in range(len(cromossomo)):
            if cromossomo[i] == 1:
                decimal = decimal + 2**i
        self.fenotipo = decimal
    
    def getFenotipo(self):
        return self.fenotipo
    
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
        #print('Roleta 1: ' + str(faixaRoleta_1) + '  Roleta 2: ' + str(faixaRoleta_2))
        self.faixaRoleta.append(faixaRoleta_1)
        self.faixaRoleta.append(faixaRoleta_2)
        #print('Tamanho da lista: ' + str(self.faixaRoleta))
    
    def getFaixaRoleta(self):
        return self.faixaRoleta
    
    ''' Faz a mutação (ou não) do cromossomo a partir da taxa de mutação. '''
    def mutarBit(self, taxaMutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxaMutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
    
    def printCromossomo(self):
        #print('Cromossomo: ' + str(self.cromossomo) + ' Fenotipo: ' + str(self.fenotipo) + ' Fitness: ' + str(self.fitness) + 
        #      ' Porcentagem: ' + str(self.fitnessPercent) + '%' + ' Roleta: ' + str(self.getFaixaRoleta[0]))
        
        print('Cromossomo: {} Fenotipo: {} Fitness: {} Porcentagem: {}% Roleta: {}'. format(self.cromossomo, self.fenotipo,
                                                                  self.fitness, self.fitnessPercent, self.faixaRoleta))