import sys
def whatever():
    try:
        f = open ( "foo.txt", 'r' )
    except IOError:
        print ('')
        print (sys.exc_type)
        whatever()