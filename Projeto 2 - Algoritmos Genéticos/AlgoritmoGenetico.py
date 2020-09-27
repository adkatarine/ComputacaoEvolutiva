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
        self.geracoes = 0
        self.numPopulacao = 100
        self.populacao = None
        self.roletaSelecao = []
    
    def executarAG(self):
        pass
    
    ''' Organiza a população em ordem decrescente da porcentagem de fitness para determinar
    a faixa da roleta. '''
    def roleta(self):
        self.populacao = sorted(self.populacao.getListaDeIndividuos(), key = Individuo.getFitnessPercent(), reverse=True)
        
        valorSomaFitnessMinimo = 0
        valorSomaFitnessMaximo = 0
        for individuo in self.populacao.getListaDeIndividuos():
            fitnessPercentAtual = individuo.getFitnessPercent()
            valorSomaFitnessMaximo = valorSomaFitnessMaximo + fitnessPercentAtual
            individuo.setFaixaRoleta(valorSomaFitnessMinimo, valorSomaFitnessMaximo)
            
            valorSomaFitnessMinimo = valorSomaFitnessMinimo + fitnessPercentAtual
            
    
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