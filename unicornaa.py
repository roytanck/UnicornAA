#!/usr/bin/env python3

import math

class UnicornAA:

	oversample = 2
	size = 16
	grid = []

	def __init__(self):
		self.size = 8 * self.oversample
		self.initGrid()

	# create a multidimensional array to hold our subpixels
	def initGrid(self):
		val = (0,0,0)
		self.grid = [ [ val for i in range(self.size) ] for j in range(self.size) ]

	# render the subpixel grid to stdout as "ascii art" (for testing)
	def renderGridAscii(self):
		chars = ' .,:;~=+*?$#@&'
		for y in range( 0, self.size ):
			for x in range( 0, self.size ):
				brightness = round( ( self.grid[x][y][0] + self.grid[x][y][1] + self.grid[x][y][2] ) /3 )
				charnr = round( (brightness/255) * (len(chars)-1) );
				print( chars[charnr] + ' ', end="" )
			print('')

	# downsample and render the pixel grid to stdout as "ascii art" (for testing)
	def renderAscii(self):
		chars = ' .,:;~=+*?$#@&'
		for y in range( 0, 8 ):
			for x in range( 0, 8 ):
				# loop through the subpixel grid for this pixel
				brightness = 0;
				for sx in range( x*self.oversample, (x+1)*self.oversample ):
					for sy in range( y*self.oversample, (y+1)*self.oversample ):
						brightness += ( self.grid[sx][sy][0] + self.grid[sx][sy][1] + self.grid[sx][sy][2] )
				avg_brightness = brightness / ( self.oversample**2 * 3 )
				charnr = round( (avg_brightness/255) * (len(chars)-1) );
				print( chars[charnr] + ' ', end="" )
			print('')

	# clear the subpixel array (setting all values to zero)
	def clear(self):
		self.initGrid()		

	# set a single pixel's rgb value
	def setPixel( self, x, y, r, g, b ):
		if( ( x >= 0 and x < self.size ) and ( y >= 0 and y < self.size ) ):
			self.grid[x][y] = ( r, g, b )

	# draw a rectangle
	def drawRect( self, x, y, w, h, r, g, b ):
		for i in range( 0, w ):
			for j in range( 0, h ):
				self.setPixel( int(x)+int(i), int(y)+int(j), r, g, b )

	# draw a circle
	def drawCircle( self, x, y, radius, r, g, b ):
		for sx in range( math.floor(x) - radius, math.ceil(x) + radius ):
			for sy in range( math.floor(y) - radius, math.ceil(y) + radius ):
				dist = math.sqrt( math.fabs( sx - x)**2 + math.fabs( sy - y )**2 )
				if( dist < radius ):
					self.setPixel( sx, sy, r, g, b );

	#draw s single pixel line
	def drawLine( self, x0, y0, x1, y1, r, g, b ):
		# Bresenham's line algorithm from http://rosettacode.org/wiki/Bitmap/Bresenham%27s_line_algorithm#Python
		dx = round( abs(x1 - x0) )
		dy = round( abs(y1 - y0) )
		x, y = round(x0), round(y0)
		sx = -1 if x0 > x1 else 1
		sy = -1 if y0 > y1 else 1
		if dx > dy:
			err = dx / 2.0
			while x != x1:
				self.setPixel( x, y, r, g, b )
				err -= dy
				if err < 0:
					y += sy
					err += dx
				x += sx
		else:
			err = dy / 2.0
			while y != y1:
				self.setPixel( x, y, r, g, b )
				err -= dx
				if err < 0:
					x += sx
					err += dy
				y += sy        
		self.setPixel( x, y, r, g, b )
