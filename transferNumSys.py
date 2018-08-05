#!/usr/bin/env python3
# -*- coding: utf-8 -*-
digits = '0123456789'
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = abc.upper()
ALPHABET = digits+abc+ABC

def startStep(num, base):
    step = 1
    while num // base**step > 0:
        step+=1
    return step - 1

def transfer(num, base, *, _ALPHABET = ALPHABET):
    d = dict(enumerate(_ALPHABET))
    sign = "-" if num < 0 else ''
    num = abs(num)

    answer = ''
    while num:
        step = startStep(num, base)
        rem = num // base**step
        rem = d.get(rem, str(rem))
        answer = answer[:-(step+1)] + rem + _ALPHABET[0]*step
        num %= base**step
    return sign + answer

def main():
    N, B = (int(x) for x in input().split())
    print(transfer(N, B).upper())


if __name__ == '__main__':
    main()