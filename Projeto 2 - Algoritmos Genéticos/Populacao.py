# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:37 2020

@author: adlla
"""
from Individuo import Individuo
import math

class Populacao():
    
    def __init__(self):
        self.listaDeIndividuos = []
            
    ''' Cria uma população de individuos. a quantidade de individuos é recebida por parâmetro. '''
    def setListaDeIndividuos(self, numPopulacao):
        for i in range(numPopulacao):
            self.listaDeIndividuos.append(Individuo())
    
    def getListaDeIndividuos(self):
        return self.listaDeIndividuos
    
    ''' Calcula o fitness de cada individuo, obtendo o fitness total de todos os individuos
    para calcular o fitness percent. '''
    def calcularFitness(self):
        fitnessTotal = 0
        x = 0

        for individuo in self.listaDeIndividuos:
             y = round(100 + (x - math.sin(math.sqrt(abs(x)))))
             individuo.setFitness(y)
             fitnessTotal = fitnessTotal + y
        
        for individuo in self.listaDeIndividuos:
            individuo.setFitnessPercent(self.calcularFitnessPercent(individuo.getFitness, fitnessTotal))
    
    def calcularFitnessPercent(self, fitness, fitnessTotal):
        return (fitness*100)/fitnessTotal
    
    def calcularRangeRoleta(self):
        pass
    
    def getMediaPopulacao(self):
        pass
    
    def printPopulacao(self):
        pass