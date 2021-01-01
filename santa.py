#!/usr/bin/python3

# Made for a friend who likes to host Secret Santas.
#
# We'll make a list of all the participants of a given Secret Santa gift
# exchange, then randomly shuffle its order.
#
# With the list randomly shuffled, we can assign each participant to be the
# Secret Santa of the next participant on the list. The last participant in
# the list will play Secret Santa to the first participant.
#
# This simple solution will ensure that no participant is their own Secret
# Santa, and that no two participants play Secret Santa to one another,
# provided the number of participants is greater than two.

import random

santa_names = [ "John", "Jade", "Dave", "Rose", "Jake", "Jane", "Dirk", "Roxy" ]
santa_count = len(santa_names)

random.shuffle(santa_names)

for i in range(1, santa_count + 1):
    print("%i: %s -> %s" % (i, santa_names[i - 1], santa_names[i % santa_count]))
