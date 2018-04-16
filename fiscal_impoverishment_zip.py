# CODE TO ZIP THE FISCAL IMPOVERISHMENT COMMANDS TO SUBMIT TO SSC
#  Sean Higgins
#  Last updated 15apr2018

# PACKAGES
import zipfile
import zlib
import os # for shell commands like change directory
import shutil # for shell commands like copy

# DIRECTORIES
os.chdir('C:/Dropbox/CEQGates/fiscal_impoverishment')

# LISTS
ados = [
	'fiscal_impoverishment',
	'fi_fgp',
	'fi_fgp_graph'
]
ados_only = []
ados_sthlps = []
for ado in ados:
	ados_sthlps.append(ado + '.ado')
	ados_sthlps.append(ado + '.sthlp')
for ado in ados_only:
	ados_sthlps.append(ado + '.ado')

myzip = 'fiscal_impoverishment.zip'

# ZIPIFY 
compression = zipfile.ZIP_DEFLATED
zf = zipfile.ZipFile(myzip, mode='w')
	# note: mode='w' to write a new file; mode='a' to append to an existing file
for file in ados_sthlps:
	print('adding %s to %s' % (file, myzip))
	zf.write(file,compress_type=compression)
zf.close()
