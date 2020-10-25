# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:42:00 2020

@author: adlla
"""

from Individuo import Individuo
from Populacao import Populacao
from random import random
from random import randint

class AlgoritmoGenetico():
    
    def __init__(self, taxaCrossover, taxaMutacao, geracoes, numPopulacao, limiteEspacos, gastoMaximo, qtdElite):
        self.taxaCrossover = taxaCrossover
        self.taxaMutacao = taxaMutacao
        self.geracoes = geracoes
        self.numPopulacao = numPopulacao
        self.qtdElite  = qtdElite
        self.melhorSolucao = None
        
        self.populacao = Populacao(numPopulacao, limiteEspacos, gastoMaximo)
        self.melhorSolucao = self.populacao.listaDeIndividuos[0]
    
    def executarAG(self):
        print('GERAÇÃO 1')
        self.populacao.printPopulacao()
        print('\n')
        for i in range(self.geracoes-1):
            print('GERAÇÃO {}'.format(i+2))
            self.populacao.setListaDeIndividuos(self.elitista())
        
            self.mutacao()
            self.populacao.avaliar()
            self.populacao.ordernarPopulacao()
            self.populacao.printPopulacao()
            self.melhorSolucao = self.populacao.melhorIndividuo(self.melhorSolucao)
            print('\n\n')
            
        print('MELHOR SOLUÇÃO ENCONTRADA:')
        self.printMelhorSolucao(self.melhorSolucao)
        print('\n\n')
        print('MELHOR SOLUÇÃO ENCONTRADA NA GERAÇÃO ATUAL:')
        self.printMelhorSolucao(self.populacao.listaDeIndividuos[0])
        
        
    ''' Realiza a seleção do individuo mais apto por torneio, considerando N = 2 '''
    def selecionarTorneio(self):

        individuo_1 = self.populacao.listaDeIndividuos[randint(0, self.numPopulacao - 1)]
        individuo_2 = self.populacao.listaDeIndividuos[randint(0, self.numPopulacao - 1)]
        
        # retorna individuo com a maior avaliação, ou seja, o vencedor do torneio
        if individuo_1.fitness > individuo_2.fitness:
            return individuo_1
        else:
            return individuo_2
    
    ''' Clona uma quantidade pré-definida dos melhores indivíduos para a próxima geração. '''
    def elitista(self):
        self.populacao.setListaDeIndividuos(sorted(self.populacao.listaDeIndividuos, key = Individuo.getFitness, reverse=True))
        novaGeracao = []
         
        for i in range(self.qtdElite):
            novaGeracao.append(self.populacao.listaDeIndividuos.pop())
            self.numPopulacao = len(self.populacao.listaDeIndividuos)
        return self.crossover(novaGeracao)
    
    
    ''' Cruzamento entre dois pais para criação de dois filhos. É definido um ponto de corte aleatório em 
    cada cromossomo e os segmentos de cromossomo criados a partir dos pontos de corte são trocados, criando
    dois novos indivíduos. '''
    def crossover(self, novaGeracao):
        for i in range(int(self.numPopulacao/2)):
            individuo_1 = self.selecionarTorneio()
            individuo_2 = self.selecionarTorneio()
            
            if(random() < self.taxaCrossover):
                pontoCorte = round(random() + len(individuo_1.cromossomo))
                
                filho_1 = individuo_2.cromossomo[0:pontoCorte] + individuo_1.cromossomo[pontoCorte::]
                filho_2 = individuo_1.cromossomo[0:pontoCorte] + individuo_2.cromossomo[pontoCorte::]
                
                descricaoJogo = []
                descricaoJogo = self.populacao.copiarAtributosJogos()
                filhos = [Individuo(descricaoJogo[0], descricaoJogo[1], descricaoJogo[2], len(self.populacao.listaJogos)), Individuo(descricaoJogo[0], descricaoJogo[1], descricaoJogo[2], len(self.populacao.listaJogos))]
                filhos[0].setCromossomo(filho_1)
                filhos[0].setGeracao(individuo_1.geracao)
                filhos[1].setCromossomo(filho_2)
                filhos[1].setGeracao(individuo_1.geracao)
                    
                novaGeracao.append(filhos[0])
                novaGeracao.append(filhos[1])
            else:
                novaGeracao.append(individuo_1)
                novaGeracao.append(individuo_2)
        return novaGeracao

    def mutacao(self):
        for individuo in self.populacao.listaDeIndividuos:
            individuo.mutarBit(self.taxaMutacao, len(self.populacao.listaJogos))

    ''' Print da melhor solução (indivíduo) recebido. '''
    def printMelhorSolucao(self, melhorSolucao):
        print("GERAÇÃO: " + str(melhorSolucao.geracao))
        melhorSolucao.printCromossomo()
        print()
        qtdGenes = len(melhorSolucao.cromossomo)
        cromossomo = melhorSolucao.cromossomo
        for i in range(qtdGenes):
            if cromossomo[i] == 1:
                print('Jogo: {}  Espaço: {}  Preço: {}  Valor: {}'. format(self.populacao.listaJogos[i].nome, self.populacao.listaJogos[i].espaco, self.populacao.listaJogos[i].preco, self.populacao.listaJogos[i].valor))
    
                               
if __name__ == '__main__':
    
    TAXA_CROSSOVER = 0.8
    TAXA_MUTACAO = 0.1
    GERACOES = 100
    NUM_POPULACAO = 100
    LIMITE_ESPACO = [2.4, 3]
    GASTO_MAXIMO = 10000.00
    QTD_ELITE = 20
    
    ''' INICIALIZANDO AG. '''
    AG = AlgoritmoGenetico(TAXA_CROSSOVER, TAXA_MUTACAO, GERACOES, NUM_POPULACAO, LIMITE_ESPACO, GASTO_MAXIMO, QTD_ELITE)
    AG.executarAG()