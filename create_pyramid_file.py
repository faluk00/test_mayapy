import sys, os
import optparse
import subprocess

import maya.standalone 
maya.standalone.initialize( name='python' )

import maya.cmds as cd
from pyramid_script.create_pyramid import pyramid, pyramid_reverse

def main():
	
	parser = optparse.OptionParser()

	# add options
	parser.add_option('-c', "--column", dest = "column",
					  type = "int",
					  help = 'column')
	
	parser.add_option('-f', "--fileName", dest = "fileName",
					  type = "string",
					  help = 'file name')
	parser.add_option("-o", "--output", dest="output",
					  type = 'string', 
					  help = 'output export file directory')
	parser.add_option("-r", action="store_true", dest="reverse", default=False)
	
	(options, args) = parser.parse_args()

	if (options.column != None):
		column = options.column
	else:
		print (parser.usage)
		print( "FUCK THIS SHIT I'M OUT." )
		exit(0)

	if (options.fileName != None):
		fileName = options.fileName
		fileName = fileName + ".ma"
	else:
		fileName = "untitle.ma"

	if (options.reverse != None):
		reverse = options.reverse
	else:
		reverse = False

	if (options.output == None):
		print (parser.usage)
		print( "FUCK THIS SHIT I'M OUT." )
		exit(0)
	else:
		output = options.output
	
	if not reverse:
		pyramid(column)
	else:
		pyramid_reverse(column)
	
	output_file = os.path.join( output, fileName )
	cd.file( rename = output_file )
	cd.file( save = True,  f=True, type='mayaAscii' )

	open_maya = input( "Do you want to open maya? 1/0 : " )
	if open_maya:
		cmd = r'C:\Program Files\Autodesk\Maya2023\bin\maya.exe'
		theproc = subprocess.Popen( [ cmd, output_file ] )
		theproc.communicate()
	
	sys.exit()

if __name__ == '__main__':
	main()