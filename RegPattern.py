# -*- coding: utf-8 -*- 
import re



class RegPattern(object):
	"""docstring for RegPattern"""
	def __init__(self):
		super(RegPattern, self).__init__()
		# self.arg = arg

	'''
	patterns
	'''
	re_ex = r'!{1}' #exclamation
	re_mutiex = r'!{2,20}'
	re_dot = r'\.{2,20}' # dot, appear more than twice
	re_que = r'\?{2,20}' # question mark, appear more than twice
	re_ch = r'([a-zA-Z])(\1+)' # repeated letters appear more than once
	# re_ch = r'([a-zA-Z])\1+'

	'''
	emoticon
	the emoticons come from https://en.wikipedia.org/wiki/List_of_emoticons
	metacharacters: . ^ $ * + ? { } [ ] \ | ( )
	'''
	re_happy = r"(:-\)|:\)|:D|:o\)|:\]|:3|:c\)|:>|=\]|8\)|=\)|:\}|:\^\)|:-\)\))" # :‑) :) :D :o) :] :3 :c) :> =] 8) =) :} :^) :-))
	re_laugh = r"(:‑D|8‑D|8D|x‑D|xD|X‑D|XD|=‑D|=D|=‑3|=3|B\^D)" # :‑D 8‑D 8D x‑D xD X‑D XD =‑D =D =‑3 =3 B^D	
	re_sad = r"(>:\[|:‑\(|:\(|:‑c|:c|:‑<|:<|:‑\[|:\[|:\{|;\()" # >:[ :‑( :( :‑c :c :‑< :っC :< :‑[ :[ :{
	re_angry = r"(:-\|\||:@|>:\()" # :-|| :@ >:(
	re_cry = r"(:'‑\(|:'\()" # :'‑( :'(
	re_horror = r"(D:<|D:|D8|D;|D=|DX|v\.v|D‑':)" # D:< D: D8 D; D= DX v.v D‑':
	re_surprise = r"(>:O|:‑O|:O|:‑o|:o|8‑0|O_O|o‑o|O_o|o_O|o_o|O-O)" # >:O :‑O :O :‑o :o 8‑0 O_O o‑o O_o o_O o_o O-O
	re_love = r"(:\*|:-\*|:\^\*|\( '\}\{'\))" # :* :-* :^* ( '}{' )
	re_wink = r"(;‑\)|;\)|\*-\)|\*\)|;‑\]|;\]|;D|;\^\)|:‑,)" # ;‑) ;) *-) *) ;‑] ;] ;D ;^) :‑,
	re_uneasy = r"(>:\\\\|>:/|:‑/|:‑\.|:/|:\\\\|=/|=\\\\|:L|=L|:S|>\.<)" # >:\ >:/ :‑/ :‑. :/ :\ =/ =\ :L =L :S >.<
	re_trouble = r"(\(>_<\)|\(>_<\)>)" # (>_<) (>_<)>


	'''
	words, punctuations and emoticons
	'''
	re_all = r"[\w']+|[.,!?;]{2,20}|[.,!?;]|<PERSON>|<URL>|:-\)|:\)|:D|:o\)|:\]|:3|:c\)|:>|=\]|8\)|=\)|:\}|:\^\)|:-\)\)|:‑D|8‑D|8D|x‑D|xD|X‑D|XD|=‑D|=D|=‑3|=3|B\^D|>:\[|:‑\(|:\(|:‑c|:c|:‑<|:<|:‑\[|:\[|:\{|;\(|D:<|D:|D8|D;|D=|DX|v\.v|D‑':|>:O|:‑O|:O|:‑o|:o|8‑0|O_O|o‑o|O_o|o_O|o_o|O-O|:\*|:-\*|:\^\*|\( '\}\{'\)"



	'''
	re_ex: 單個感嘆號
	re_multiex: 兩個及兩個以上感嘆號
	re_dot: 三個及三個以上句號
	re_que: 兩個及兩個以上問號
	re_ch: 重複出現三次以上的字母
	re_all: 匹配全部
	'''
	def get_pattern(self, text, re_text):
		if re_text == 're_ex':
			return self.__get_ex(text)
		elif re_text == 're_multiex':
			return self.__get_multiex(text)
		elif re_text == 're_dot':
			return self.__get_dot(text)
		elif re_text == 're_que':
			return self.__get_que(text)
		elif re_text == 're_ch':
			return self.__get_ch(text)
		elif re_text == 're_all':
			return self.__get_all(text)

	def __get_ex(self, text):
		p = re.compile(self.re_ex)
		match = p.findall(text)
		return len(match)

	def __get_multiex(self, text):
		p = re.compile(self.re_mutiex)
		match = p.findall(text)
		return len(match)

	def __get_dot(self, text):
		p = re.compile(self.re_dot)
		match = p.findall(text)
		return len(match)

	def __get_que(self, text):
		p = re.compile(self.re_que)
		match = p.findall(text)
		return len(match)

	def __get_ch(self, text):
		count = 0
		p = re.compile(self.re_ch)
		match = p.findall(text)
		for m in match:
			if len(m[1]) > 1:
				count += 1
		return count

	# return the match list rather than the count of matched items
	def __get_all(self, text):
		match = []
		p = re.compile(self.re_all)
		match = p.findall(text)
		return match
