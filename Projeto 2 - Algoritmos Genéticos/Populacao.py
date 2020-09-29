# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:47:37 2020

@author: adlla
"""
from Individuo import Individuo
import math

class Populacao:
    
    def __init__(self, numPopulacao):
        self.listaDeIndividuos = []
        self.mediaPopulacao = 0
        
        # Cria uma população de individuos. a quantidade de individuos é recebida por parâmetro.
        for i in range(numPopulacao):
            self.listaDeIndividuos.append(Individuo())
            
    def setListaDeIndividuos(self, listaDeIndividuos):
        self.listaDeIndividuos = listaDeIndividuos
    
    def getListaDeIndividuos(self):
        return self.listaDeIndividuos
    
    ''' Calcula o fitness de cada individuo, obtendo o fitness total de todos os individuos
    para calcular o fitness percent. '''
    def calcularFitness(self):
        fitnessTotal = 0

        for individuo in self.listaDeIndividuos:
            x = individuo.getFenotipo()
            #y = round(100 + (x - math.sin(math.sqrt(abs(x)))))
            y = round( (10*(x**2)) + (2*x) + 30)
            individuo.setFitness(y)
            fitnessTotal = fitnessTotal + y
        
        for individuo in self.listaDeIndividuos:
            individuo.setFitnessPercent(self.calcularFitnessPercent(individuo.getFitness, fitnessTotal))
    
    
    ''' Calcula e retorna a porcentagem do fitness. '''
    def calcularFitnessPercent(self, fitness, fitnessTotal):
        return (fitness*100)/fitnessTotal
    
    
    ''' Organiza a população em ordem decrescente da porcentagem de fitness para determinar
    a faixa da roleta. '''
    def calcularRangeRoleta(self):
        self.listaDeIndividuos = sorted(self.getListaDeIndividuos(), key = Individuo.getFitnessPercent(), reverse=True)
        
        valorSomaFitnessMinimo = 0
        valorSomaFitnessMaximo = 0
        for individuo in self.getListaDeIndividuos():
            fitnessPercentAtual = individuo.getFitnessPercent()
            valorSomaFitnessMaximo = valorSomaFitnessMaximo + fitnessPercentAtual
            individuo.setFaixaRoleta(valorSomaFitnessMinimo, valorSomaFitnessMaximo)
            
            valorSomaFitnessMinimo = valorSomaFitnessMinimo + fitnessPercentAtual
    
    def getMediaPopulacao(self):
        return self.mediaPopulacao

    def printPopulacao(self):
        for individuo in self.getListaDeIndividuos():
            individuo.printCromossomo()