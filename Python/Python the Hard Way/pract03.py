#finding Amps

print "How many watts (W): "
Watts = int(raw_input())
print "How many Volts (V): "
Volts = int(raw_input())
print "How much time (s)"
Time = int(raw_input())

Amps = Volts * Time / Watts
print "Amps are %r " % Amps
