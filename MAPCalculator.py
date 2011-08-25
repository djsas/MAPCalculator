# -*- coding:utf-8 -*-
# $Id$

"""
MAPを計算するPythonクラス
"""

class MAPCalculator:
	def __init__(self):
		self.clearResults()
		self.corrects = [] #正解とするラベルを格納する
	def clearResults(self):
		self.results = {}  #回答結果を格納する。インデックスが0から順に1位、2位、...、と代入していく
	def calculateAP(self, key):
		print self.getCalculateAP(key)
	def getCalculateAP(self, key):
		num = 0.0
		ansnum = 0.0
		sum_p = 0.0
		for x in self.results[key]:
			num += 1
			if x in self.corrects:
				ansnum += 1
				p = ansnum / num
				sum_p += p
		return sum_p / ansnum
	def calculateMAP(self):
		print self.getCalculateMAP()
	def getCalculateMAP(self):
		for k in self.results.keys():
			pass
	def loadCorrects(self, f):
		self.corrects = self.__fopen(f)
	def loadResults(self, key, f):
		self.results[key] = self.__fopen(f)
	def setCorrects(self, a):
		self.corrects = a
	def setResults(self, key, a):
		self.results[key] = a
	
	def __fopen(self, f):
		return [x.rstrip() for x in open(f)]


# D.S.G.