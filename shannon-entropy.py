# title           :shannon_entropy.py
# description     :This uses the Shannon entropy equation to estimate the
#                  average minimum number of bits needed to encode a
#                  string of symbols, based on the frequency of the symbols.
# author          :Gianni Perez
# date            :20170901
# version         :0.3
# revised         :20211017
# usage           :python shannon_entropy.py
# notes           :
# python_version  :3.7+
# ============================================================================

import math


def shannon_entropy(data):
    stack = {}
    symbol_list = {}

    for character in data:
        stack[character] = round(data.count(character) / len(data), 5)
        symbol_list[character] = data.count(character)
    print("\nSymbol-occurrence frequencies:\n")
    for symbol in stack:
        print("{0} --> {1} -- {2}".format(symbol, stack[symbol], symbol_list[symbol]))
    return symbol_frequency(stack)


def symbol_frequency(symbol_set):
    bit_set = [round(symbol_set[symbol] * math.log2(symbol_set[symbol]), 5) for symbol in symbol_set]
    entropy = -1 * (round(sum(bit_set), 5))
    return entropy


if __name__ == "__main__":
    m = input("\nEnter the message: ")
    bits = shannon_entropy(m)
    print("\nH(X) = {0} bits. Rounded to {1} bits/symbol, ".format(bits, round(bits)))
    print("it will take {0} bits to optimally encode '{1}''".format(len(m) * round(bits), m))
    print("\nMetric entropy: %.5f" % (bits / len(m)))
