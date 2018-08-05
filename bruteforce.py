#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Файл brutforce.py: реализация генерирования варианта пароля
"""

# Строки алфавита, то есть те строки, из букв которых будет состоять пароль
# парль может состоять:
digits = '0123456789'              # только из цыфр
abc = 'abcdefghijklmnopqrstuvwxyz' # только из строчных букв
ABC = abc.upper()				   # только из заглавных букв
ALPHABET = digits + abc + ABC      # или всё вместе

# Импортируем функцию
# from transferNumSys import transfer
from recursivTransferNumSys import transfer

def fromNumIntoWord(num, lenCap, *,startLenCap = 1, _ALPHABET = ALPHABET):
	lenAlpha = len(_ALPHABET)
	word = transfer(num, lenAlpha, _ALPHABET = _ALPHABET)
	if len(word) < lenCap:
		word = (lenCap -len(word))*_ALPHABET[0] + word

	return word

def genPassword(lenCap, *, _ALPHABET = ALPHABET):
	lenAlpha = len(_ALPHABET)
	N = lenAlpha**lenCap
	for num in range(N):
		variant = fromNumIntoWord(num, lenCap, _ALPHABET = _ALPHABET)
		yield variant

def main():
	password = input('Enter your password: ')
	lenCap  = len(password)
	f = open('keys.txt', 'w')
	for pas in genPassword(lenCap, _ALPHABET = ALPHABET):
		print(pas, file = f)
		if pas == password:
			break
	print("WIN HAKER", pas)

if __name__ == "__main__":
	main()

# genPassword(lenCap, _ALPHABET = digits)
# genPassword(lenCap, _ALPHABET = abc)
# genPassword(lenCap, _ALPHABET = ABC)