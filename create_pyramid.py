import maya.cmds as cd

def create_cube( x, y ):
	cube = cd.polyCube( w = 1, h = 1, d = 1, sx = 1, sy = 1, sz = 1, ax = (0, 1, 0), ch = False )
	cd.move( x, y, 0, cube )
	return cube

def create_cylinder( x, y, rotZ ):
	cylinder = cd.polyCylinder( r = 0.25, h = 2, sx = 20, sy = 1, sz = 1, ax = ( 0, 1, 0 ), ch = False )
	cd.rotate( 0, 0, rotZ, cylinder )
	cd.move( x, y, 0, cylinder )
	return cylinder

def pyramid( column ):

	for i in range( column ):
		
		columnGrp = cd.createNode( "transform", name = "column_" + str(i+1) )
		
		TXmin = -1 - ( i * 2 )
		TXmax = 1 + ( i * 2 )
		TY = ( ( column * 2 ) - 2 ) - ( i * 2 )
		
		# create negative cube
		cy1 = create_cylinder( TXmin, TY, -45 )
		cd.parent( cy1, columnGrp )
		# create positive cube
		cy2 = create_cylinder( TXmax, TY, 45 )
		cd.parent( cy2, columnGrp )
		if i > 0:
			for n in range( i ):
				TXmin = -1 - ( n * 2 )
				TXmax = 1 + ( n * 2 )
				cube1 = create_cube( TXmin, TY )
				cube2 = create_cube( TXmax, TY )
				cd.parent( cube1, columnGrp )
				cd.parent( cube2, columnGrp )

def pyramid_reverse( column ):

	for i in range( column ):
		num = (column-1) - i
		
		columnGrp = cd.createNode( "transform", name = "column_" + str(i+1) )
		
		TXmin = -1 - ( num * 2 )
		TXmax = 1 + ( num * 2 )
		TY = ( ( column * 2 ) - 2 ) - ( i * 2 )
		
		# create negative cube
		cy1 = create_cylinder( TXmin, TY, 45 )
		cd.parent( cy1, columnGrp )
		# create positive cube
		cy2 = create_cylinder( TXmax, TY, -45 )
		cd.parent( cy2, columnGrp )
		
		if num > 0:
			for n in range( num ):
				TXmin = -1 - ( n * 2 )
				TXmax = 1 + ( n * 2 )
				cube1 = create_cube( TXmin, TY )
				cube2 = create_cube( TXmax, TY )
				cd.parent( cube1, columnGrp )
				cd.parent( cube2, columnGrp )