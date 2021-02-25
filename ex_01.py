#!/usr/bin/env python3.8

import sys

nb = input().split()
nb = [int(i) for i in nb]
streets = []
paths = []

for i in range(0, nb[2]):
    streets = input()
for i in range(0, nb[3]):
    paths = input()

print(streets)