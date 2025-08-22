# Shannon's Entropy Calculator

Shannon's entropy is a way to measure how much **information** is contained in a message. In this context, it tells us the average minimum number of bits needed to encode a string of symbols, based on how often each symbol appears. If a message uses many different symbols with similar frequencies, its entropy is higher, meaning it takes more bits to store or transmit. If the message repeats the same symbol often, its entropy is lower, and it can be compressed more efficiently. This calculation helps us understand how "random" or "predictable" a message is, and how much space is needed to represent it in digital form.

Named after Boltzmann's Η-theorem, Shannon defined the entropy Η (Greek capital letter eta) of a discrete random variable X with possible values {x1, ..., xn} and probability mass function P(X) as:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;\mathrm&space;{H}&space;(X)=\mathbb&space;{E}&space;[\mathrm&space;{I}&space;(X)]=\mathbb&space;{E}&space;[-\ln(\mathrm&space;{P}&space;(X))].}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;\mathrm&space;{H}&space;(X)=\mathbb&space;{E}&space;[\mathrm&space;{I}&space;(X)]=\mathbb&space;{E}&space;[-\ln(\mathrm&space;{P}&space;(X))].}" title="{\displaystyle \mathrm {H} (X)=\mathbb {E} [\mathrm {I} (X)]=\mathbb {E} [-\ln(\mathrm {P} (X))].}" /></a>

Here E is the expected value operator, and I is the information content of X. I(X) is itself a random variable. The entropy can explicitly be written as:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;\mathrm&space;{H}&space;(X)=\sum&space;_{i=1}^{n}{\mathrm&space;{P}&space;(x_{i})\,\mathrm&space;{I}&space;(x_{i})}=-\sum&space;_{i=1}^{n}{\mathrm&space;{P}&space;(x_{i})\log&space;_{b}\mathrm&space;{P}&space;(x_{i})},}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;\mathrm&space;{H}&space;(X)=\sum&space;_{i=1}^{n}{\mathrm&space;{P}&space;(x_{i})\,\mathrm&space;{I}&space;(x_{i})}=-\sum&space;_{i=1}^{n}{\mathrm&space;{P}&space;(x_{i})\log&space;_{b}\mathrm&space;{P}&space;(x_{i})},}" title="{\displaystyle \mathrm {H} (X)=\sum _{i=1}^{n}{\mathrm {P} (x_{i})\,\mathrm {I} (x_{i})}=-\sum _{i=1}^{n}{\mathrm {P} (x_{i})\log _{b}\mathrm {P} (x_{i})},}" /></a>

where b is the base of the logarithm used. Common values of b are 2, Euler's number e, and 10, and the corresponding units of entropy are the bits for b = 2, nats for b = e, and bans for b = 10.

One may also define the conditional entropy of two events X and Y taking values xi and yj respectively, as:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;\mathrm&space;{H}&space;(X|Y)=-\sum&space;_{i,j}p(x_{i},y_{j})\log&space;{\frac&space;{p(x_{i},y_{j})}{p(y_{j})}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;\mathrm&space;{H}&space;(X|Y)=-\sum&space;_{i,j}p(x_{i},y_{j})\log&space;{\frac&space;{p(x_{i},y_{j})}{p(y_{j})}}}" title="{\displaystyle \mathrm {H} (X|Y)=-\sum _{i,j}p(x_{i},y_{j})\log {\frac {p(x_{i},y_{j})}{p(y_{j})}}}" /></a>

where p(xi, yj) is the probability that X = xi and Y = yj. This quantity should be understood as the amount of randomness in the random variable X given the event Y [[SOURCE]](https://en.wikipedia.org/wiki/Entropy_(information_theory)#Definition).

This project calculates the Shannon entropy of a given text message based on symbol frequencies.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Support](#support)
- [License](#license)

## Installation

All the code required to get started is in the file (*shannon-entropy.py*). Only a working installation of Python 3 is necessary [[LINK]](https://www.python.org/).

## Features

After user input, the program iterates over the given string (m) separating each character (symbol) and calculating its frequency (probability) over the length of m.  Besides Shannon's entropy, values for optimally encoding the message and the metric entropy are also determined. Such optimal encoding would allocate fewer bits for the frequency occuring symbols and long bit sequences for the more infrequent symbols [[SOURCE]](http://www.bearcave.com/misl/misl_tech/wavelets/compression/shannon.html). 

## Usage

This is a sample output of entering the string **"abracadabra"**:

```
Enter the message: abracadabra

Symbol-occurrence frequencies:

b --> 0.18182 -- 2
d --> 0.09091 -- 1
a --> 0.45455 -- 5
r --> 0.18182 -- 2
c --> 0.09091 -- 1

H(X) = 2.04039 bits. Rounded to 2 bits/symbol (bits per byte),
it will take 22 bits to optimally encode "abracadabra"

Metric entropy: 0.18549
```

## Support

For questions or comments:

- Author: **Gianni Perez** @ [skylabus.tech](https://www.skylabus.tech) or at gianni.perez@gmail.com
- [![](http://www.linkedin.com/img/webpromo/btn_liprofile_blue_80x15.png)](https://www.linkedin.com/in/gianni-perez/)


## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ambron60/l-system-drawing/blob/master/LICENSE.md)