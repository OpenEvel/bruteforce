#!/usr/bin/env python3
# -*- coding: utf-8 -*-
digits = '0123456789'
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = abc.upper()
ALPHABET = digits + abc + ABC

def transfer_d(num, base, d):
	if num < base:
		return d.get(num, str(num))
	answer = d.get(num % base)
	return transfer_d(num // base, base, d) + answer

def transfer(num, base, *, _ALPHABET = ALPHABET):
    d = dict(enumerate(_ALPHABET[:base]))
    sign = '-' if num < 0 else ''
    num = abs(num)
    return (sign + transfer_d(num, base, d))

def main():
    num, base = (int(x) for x in input().split())
    print(transfer(num, base))

if __name__ == "__main__":
    main()