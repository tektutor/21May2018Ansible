#!/usr/bin/python

def add( value1, value2 ):
	return value1 + value2

if __name__ == "__main__":

   result = add ( 100, 200 )
   print ( 'The result is ' + str( result ) )

   result = add ( 'Hello ' , 'World' )
   print ( 'The result is ' + result )

