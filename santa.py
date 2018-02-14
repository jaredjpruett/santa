# Made for a friend who likes to host Secret Santas.

import random

# We'll make a list of all the participants of a given Secret Santa gift
#  exchange, then randomly shuffle its order.
# With the list randomly shuffled, we can assign each participant to be the
#  Secret Santa of the next participant on the list. The last participant in
#  the list will play Secret Santa to the first participant.
# This simple solution will ensure that no participant is their own Secret
#  Santa, and that no two participants play Secret Santa to one another,
#  provided the number of participants is greater than two.

santas = [ "John", "Mike", "Josh", "Fred", "Mick" ]
random.shuffle(santas)

for i in xrange(0, len(santas) - 1):
	print("%s -> %s" % (santas[i], santas[i + 1]))
print("%s -> %s" % (santas[len(santas) - 1], santas[0]))
