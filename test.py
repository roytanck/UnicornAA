#!/usr/bin/env python3

from unicornaa import UnicornAA
import random

inst = UnicornAA()

for x in range(0,16):
	for y in range(0,16):
		inst.setPixel( x, y, random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255) )

#inst.drawRect(0,0,16,16,50,0,0)
inst.drawRect( 0, 0, 16, 16, 20, 20, 20 )
#inst.drawRect( 4, 0, 4, 8, 255, 255, 255 )
#inst.clear()
inst.drawCircle( 7.5, 7.5, 5, 0, 0, 0 )
inst.drawLine( 3, 3, 11, 14, 255, 255, 255 )

print('\nSub-pixel grid:')
inst.renderGridAscii()
print('\nDownsampled:')
inst.renderAscii()
