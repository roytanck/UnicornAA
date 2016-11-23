#!/usr/bin/env python3

from unicornaa import UnicornAA
import random
import time
import math

inst = UnicornAA(4)

# for x in range(0,16):
# 	for y in range(0,16):
# 		inst.setPixel( x, y, random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255) )

#inst.drawRect(0,0,16,16,50,0,0)
# inst.drawRect( 0, 0, 16, 16, 255, 255, 0 )
#inst.drawRect( 4, 0, 4, 8, 255, 255, 255 )
#inst.clear()
# inst.drawCircle( 7.5, 7.5, 5, 0, 0, 0 )
# inst.drawLine( 3, 3, 11, 14, 255, 255, 255 )

# print('\nSub-pixel grid:')
# inst.renderGridAscii()
# print('\nDownsampled:')
# inst.renderAscii()

# inst.render()

# time.sleep(3)

steps = 360
for i in range( steps ):
	inst.clear()
	# x = 15.5 + math.sin( (i/steps) * math.pi * 2 ) * 6
	# y = 15.5 + -math.cos( (i/steps) * math.pi * 2 ) * 6
	# rad = 8
	x = 17.5
	y = 28 - math.fabs( math.sin( (i/steps) * math.pi * 2 ) * 24 )
	rad = 8
	inst.drawCircle( x, y, rad, 255, 255, 0 )
	inst.render()
	#time.sleep(0.01)