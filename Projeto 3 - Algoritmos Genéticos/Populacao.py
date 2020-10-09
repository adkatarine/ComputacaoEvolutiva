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
        self.fitnessTotal = 0
        self.coordenadas = []
        
        # Cria uma população de individuos. a quantidade de individuos é recebida por parâmetro.
        for i in range(numPopulacao):
            self.listaDeIndividuos.append(Individuo())
        self.coordenadaCidades()
         
    def setListaDeIndividuos(self, listaDeIndividuos):
        self.listaDeIndividuos = listaDeIndividuos
    
    def getListaDeIndividuos(self):
        return self.listaDeIndividuos
    
    def coordenadaCidades(self):
        cidade1 = {"1": 1, "x": 100, "y": 150}
        cidade2 = {"2": 2, "x": 120, "y": 170}
        cidade3 = {"3": 3, "x": 90, "y": 100}
        cidade4 = {"4": 4, "x": 200, "y": 80}
        cidade5 = {"5": 5, "x": 110, "y": 110}
        cidade6 = {"6": 6, "x": 60, "y": 20}
        cidade7 = {"7": 7, "x": 160, "y": 40}
        cidade8 = {"8": 8, "x": 70, "y": 80}
        
        self.coordenadas.append(cidade1)
        self.coordenadas.append(cidade2)
        self.coordenadas.append(cidade3)
        self.coordenadas.append(cidade4)
        self.coordenadas.append(cidade5)
        self.coordenadas.append(cidade6)
        self.coordenadas.append(cidade7)
        self.coordenadas.append(cidade8)
        
    
    ''' Calcula o fitness de cada individuo, obtendo o fitness total de todos os individuos
    para calcular o fitness percent. '''
    def calcularFitness(self):
        for individuo in self.getListaDeIndividuos():
            cromossomo = individuo.getCromossomo()
            
            somaFitness = 0
            for i in range(len(cromossomo)-1):
                x1 = self.coordenadas[cromossomo[i]-1]['x']
                x2 = self.coordenadas[cromossomo[i+1]-1]['x']
                y1 = self.coordenadas[cromossomo[i]-1]['y']
                y2 = self.coordenadas[cromossomo[i+1]-1]['y']
                
                distancia = math.sqrt(abs(((x2 - x1)**2) + ((y2 - y1)**2)))
                somaFitness = somaFitness + distancia
            #individuo.setFitness(somaFitness**(-1))
            individuo.setFitness(somaFitness)
            self.fitnessTotal = self.fitnessTotal + somaFitness
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