# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:37 2020

@author: adlla
"""

from Individuo import Individuo
import math
import numpy as np

class Populacao:
    
    def __init__(self, numPopulacao):
        self.listaDeIndividuos = []
        self.mediaPopulacao = 0
        self.fitnessTotal = 0
        
        # Cria uma população de individuos. a quantidade de individuos é recebida por parâmetro.
        for i in range(numPopulacao):
            self.listaDeIndividuos.append(Individuo())
        self.coordenadaCidades()
        self.calcularFitness()
         
    def setListaDeIndividuos(self, listaDeIndividuos):
        self.listaDeIndividuos = listaDeIndividuos
    
    def getListaDeIndividuos(self):
        return self.listaDeIndividuos
    
    def coordenadaCidades(self):
        self.x = np.array([300, 150, 200, 115, 100, 250, 285, 150, 200, 115])
        self.y = np.array([200, 115, 300, 150, 200, 285, 250, 290, 100, 250])
    
    ''' Calcula o fitness de cada individuo, obtendo o fitness total de todos os individuos
    para calcular o fitness percent. '''
    def calcularFitness(self):
        for individuo in self.getListaDeIndividuos():
            cromossomo = individuo.getCromossomo()
            
            somaFitness = 0
            for i in range(len(cromossomo)-1):

                distancia = math.sqrt(abs(((self.x[i+1] - self.x[i])**2) + ((self.y[i+1] - self.y[i])**2)))
                somaFitness = somaFitness + distancia
            individuo.setFitness(1/somaFitness)
            self.fitnessTotal = self.fitnessTotal + (1/somaFitness)
        for individuo in self.listaDeIndividuos:
            individuo.setFitnessPercent(self.calcularFitnessPercent(individuo.getFitness()))
    
    ''' Calcula e retorna a porcentagem do fitness. '''
    def calcularFitnessPercent(self, fitness):
        return (fitness*100)/self.fitnessTotal
    
    
    ''' Organiza a população em ordem decrescente da porcentagem de fitness para determinar
    a faixa da roleta. '''
    def calcularRangeRoleta(self):
        self.setListaDeIndividuos(sorted(self.getListaDeIndividuos(), key = Individuo.getFitnessPercent, reverse=True))
        valorSomaFitnessMinimo = 0
        valorSomaFitnessMaximo = 0
        
        for individuo in self.getListaDeIndividuos():
            
            fitnessPercentAtual = individuo.getFitnessPercent()
            valorSomaFitnessMaximo = valorSomaFitnessMaximo + fitnessPercentAtual
            individuo.setFaixaRoleta(valorSomaFitnessMinimo, valorSomaFitnessMaximo)
            
            valorSomaFitnessMinimo = valorSomaFitnessMinimo + fitnessPercentAtual
    
    
    ''' Retorna a média de aptidão da população. '''
    def getMediaPopulacao(self):
        return self.fitnessTotal / len(self.listaDeIndividuos)

    def printPopulacao(self):
        for individuo in self.getListaDeIndividuos():
            individuo.printCromossomo()