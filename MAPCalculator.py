# -*- coding:utf-8 -*-
# $Id$

"""
MAPを計算するPythonクラス
"""

class MAPCalculator:
	results = []  #回答結果を格納する。インデックスが0から順に1位、2位、...、と代入していく
	corrects = [] #正解とするラベルを格納する
	def loadCorrects(self, f):
		self.corrects = self.__fopen(f)
	def loadResults(self, f):
		self.results = self.__fopen(f)
	def setCorrects(self, a):
		self.corrects = a
	def setResults(self, a):
		self.results = a
	
	def __fopen(self, f):
		return [x.rstrip() for x in open(f)]


# D.S.G.