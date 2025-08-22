# title           :shannon_entropy.py
# description     :This uses the Shannon entropy equation to estimate the
#                  average minimum number of bits needed to encode a
#                  string of symbols, based on the frequency of the symbols.
# author          :Gianni Perez
# date            :20170901
# version         :0.4
# revised         :20250821
# usage           :python shannon_entropy.py
# notes           :
# python_version  :3.7+
# ============================================================================

import math
from collections import Counter

def shannon_entropy(data):
    if not data:
        print("Input string is empty.")
        return 0.0

    symbol_counts = Counter(data)
    length = len(data)
    print("\nSymbol-occurrence frequencies:\n")
    for symbol, count in symbol_counts.items():
        freq = count / length
        print(f"{symbol} --> {freq:.5f} -- {count}")
    return calculate_entropy(symbol_counts, length)

def calculate_entropy(symbol_counts, length):
    entropy = 0.0
    for count in symbol_counts.values():
        p = count / length
        entropy -= p * math.log2(p)
    return round(entropy, 5)

if __name__ == "__main__":
    m = input("\nEnter the message: ")
    bits = shannon_entropy(m)
    if m:
        print(f"\nH(X) = {bits} bits. Rounded to {round(bits)} bits/symbol, ")
        print(f"it will take {len(m) * round(bits)} bits to optimally encode '{m}'")
        print(f"\nMetric entropy: {bits / len(m):.5f}")
