from __future__ import division
from Fraction import Fraction
from MixedFraction import MixedFraction
__author__ = 'Dennis Qiu'

def main():
    Fractions = []
    fractions = []
    with open('fractions.dat', 'r', encoding='UTF-8') as read_frac:
        for line in read_frac.readlines():
            strip = line.strip('\n')
            split = strip.split('/')
            if len(split) == 2 and split[0].isdigit() and split[1].isdigit():
                frac = Fraction(int(split[0]), int(split[1]))
                fractions.append(frac)
                Fractions.append(strip)
    sumf = Fraction(0, 1)
    for frac in fractions:
        sumf += frac
    print(' + '.join(Fractions) + ' = {}'.format(sumf))

    MixedFractions = []
    mf = []
    with open('MixedFractions.dat', 'r', encoding='UTF-8') as read_frac:
        for line in read_frac.readlines():
            strip = line.strip('\n')
            s = strip.split(' ')
            if len(s) > 1:
                whole_num = int(s[0])
            else:
                whole_num = 0
            split = s[-1].split('/')
            if len(split) == 2:
                n = split[0]
                d = split[1]
                if n.isdigit() and d.isdigit():
                    M = whole_num * int(d) + int(n)
                    mfrac = MixedFraction(M, int(d))
                    mf.append(mfrac)
                    MixedFractions.append(strip)
    summf = MixedFraction(0, 1)
    for mfn in mf:
        summf += mfn
    print(' + '.join(MixedFractions) + ' = {}'.format(summf))

    sum_total = MixedFraction(0, 1)
    sum_total += summf
    sum_total += sumf
    print('{} + {} = {}\n'.format(sumf, summf, sum_total))


    sub_total = sum_total
    equation = sub_total.__str__()
    for frac in fractions:
        last_total = sub_total
        sub_total -= frac
        equation += ' - '
        equation += frac.__str__()
        print('{} - {} = {}'.format(last_total, frac, sub_total))


    subtract = summf - fractions[5]
    print('\n{} - {} = {}'.format(summf, fractions[5], subtract))

    divide = summf / sumf
    print('{} / {} = {}'.format(summf, sumf, divide))

    multiply = fractions[1] * mf[2]
    print('{} * {} = {}\n'.format(fractions[1], mf[2], multiply))


    if sumf == sumf:
        print('{} is equal to {}'.format(sumf, sumf))

    if sumf != summf:
        print('{} is not equal to {}'.format(sumf, summf))

    if sumf > summf:
        print('{} is greater than {}'.format(sumf, summf))
    else:
        print('{} is less than {}'.format(sumf, summf))

    if sum_total > summf:
        print('{} is greater than {}'.format(sum_total, summf))
    else:
        print('{} is less than {}'.format(sum_total, summf))

    if (summf - summf) <= summf:
        print('{} is less than or equal to {}'.format((summf - summf), summf))
    else:
        print('{} is greater than or equal to {}'.format((summf - summf), summf))

    if (sumf + sumf) >= sumf:
        print('{} is greater than or equal to {}'.format((sumf + sumf), sumf))
    else:
        print('{} is less than or equal to {}'.format((sumf + sumf), sumf))

if __name__ == '__main__':
    main()
