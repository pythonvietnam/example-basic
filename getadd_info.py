import sys, socket

try:
    result = socket.gethostbyaddr("8.8.8.8")

    print "Primary hostname:"
    print "  " + result[0]

    print "\nAddresses:"
    for item in result[2]:
        print "  " + item

except socket.herror, e:
    print "Couldn't look up name:", e