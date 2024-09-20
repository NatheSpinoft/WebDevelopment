elements = [0, 1, 2, 3, 4, 5, 6, 7]
strange = ['reed', 'steve', 'ben', 'stone']

for i in elements:
    print "the number: %d" % i 

for i in elements:
    print "the number: %s" % elements

for i in strange:
    print "the strange: %r" % i

markup = [['steve', 'ben', 'Van'], ['001', '002', '003']]


for i in markup:
    print "This is %s" %i