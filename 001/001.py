#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# 001: Heads or Tails

from random import randint

cara, count, sello = 0, 0, 0
while count < 100: count, (cara, sello) = count + 1, (cara + 1, sello) if randint(0, 1) == 1 else (cara, sello + 1)
print('contador {}, número de caras {}, número de sellos {}'.format(count, cara, sello))
