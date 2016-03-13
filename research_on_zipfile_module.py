""" SRC--- http://pastebin.com/9h2y7rEq """

"""
If the file is created with mode 'w', 'x' or 'a' and then closed without adding any files to the archive, the appropriate ZIP structures for an empty archive will be written to the file
"""
===============================================================
>>> zfh = zipfile.ZipFile('desiredZipfileName.zip', 'w')	# can change .zip of first parameter to anything n it will still be a zip file TESTED
>>> zinfo = zipfile.ZipInfo("empty/",(2002,12,31,23,59,59))
>>> zfh.writestr(zinfo, "")
>>> zfh.close()
>>> zfh = zipfile.ZipFile('desiredZipfileName.zip', 'a')	# creates desiredZipfileName despite 'a' flag if it doesn't exist, irrespective of weather we write anything in it
>>> zinfo = zipfile.ZipInfo("empty/nested/",(2002,12,31,23,59,59))
>>> zfh.writestr(zinfo, "")
>>> zfh.close()
===============================================================
zfi.external_attr = 16
zinfo.external_attr = 48
===============================================================
## Nature of zfh.write(p1, p2)
p1-> take bytes from this file
```
>>> p1 = os.path.join(os.path.abspath("."), "learn by doing.txt").encode("UTF-8")
>>> zfh.write(p1, "lBD.text")
```
p2-> arcname=>"put the bytes from 'filename' into archive under the name arcname";
	 usually os.path.basename(filename), EXPLOIT THIS
```
>>> zfh = zipfile.ZipFile('desiredZipfileName.sip', 'a')
>>> os.listdir(".")
['desiredZipfileName.sip', 'learn by doing.txt', 'muse-myTestSuite.txt', 'webpageSanitize']
>>> p1 = os.path.join(os.path.abspath("."), "learn by doing.txt").encode('UTF-8')
>>> zfh.write(p1, "empty/nested/lBD.text")
>>> zfh.close()
>>> zfh = zipfile.ZipFile('desiredZipfileName.sip', 'a')
>>> p1 = os.path.join(os.path.abspath("."), "muse-myTestSuite.txt").encode('UTF-8')
>>> zfh.write(p1, "empty/aMuse.txt")
>>> zfh.close()
>>>
```
===============================================================
A zip file has no directory structure, it just has a bunch of pathnames and their contents. These pathnames should be relative to an imaginary root folder (the ZIP file itself). "../" prefixes have no defined meaning in a zip file.
Consider you have a file, a and you want to store it in a "folder" inside a zip file. All you have to do is prefix the filename with a folder name when storing the file in the zipfile:
===============================================================
def ZipDir(inputDir, outputZip):
	'''Zip up a directory and preserve symlinks and empty directories'''
	zipOut = zipfile.ZipFile(outputZip, 'w', compression=zipfile.ZIP_DEFLATED)
	
	rootLen = len(os.path.dirname(inputDir))
	def _ArchiveDirectory(parentDirectory):
		contents = os.listdir(parentDirectory)
		#store empty directories
		if not contents:
			#http://www.velocityreviews.com/forums/t318840-add-empty-directory-using-zipfile.html
			archiveRoot = parentDirectory[rootLen:].replace('\\', '/').lstrip('/')
			zipInfo = zipfile.ZipInfo(archiveRoot+'/')
			zipOut.writestr(zipInfo, '')
		for item in contents:
			fullPath = os.path.join(parentDirectory, item)
			if os.path.isdir(fullPath) and not os.path.islink(fullPath):
				_ArchiveDirectory(fullPath)
			else:
				archiveRoot = fullPath[rootLen:].replace('\\', '/').lstrip('/')
				if os.path.islink(fullPath):
					# http://www.mail-archive.com/python-list@python.org/msg34223.html
					zipInfo = zipfile.ZipInfo(archiveRoot)
					zipInfo.create_system = 3
					# long type of hex val of '0xA1ED0000L',
					# say, symlink attr magic...
					zipInfo.external_attr = 2716663808L
					zipOut.writestr(zipInfo, os.readlink(fullPath))
				else:
					zipOut.write(fullPath, archiveRoot, zipfile.ZIP_DEFLATED)
	_ArchiveDirectory(inputDir)
	
	zipOut.close()
===============================================================
def addFolderToZip(myZipFile,folder):
	folder = folder.encode('ascii') #convert path to ascii for ZipFile Method
	for file in glob.glob(folder+"/*"):
			if os.path.isfile(file):
				print file
				myZipFile.write(file, os.path.basename(file), zipfile.ZIP_DEFLATED)
			elif os.path.isdir(file):
				addFolderToZip(myZipFile,file)

def createZipFile(filename,files,folders):
	curTime=strftime("__%Y_%m_%d", time.localtime())
	filename=filename+curTime;
	print filename
	zipFilename=utils.getFileName("files", filename+".zip")
	myZipFile = zipfile.ZipFile( zipFilename, "w" ) # Open the zip file for writing 
	for file in files:
		file = file.encode('ascii') #convert path to ascii for ZipFile Method
		if os.path.isfile(file):
			(filepath, filename) = os.path.split(file)
			myZipFile.write( file, filename, zipfile.ZIP_DEFLATED )

	for folder in  folders:   
		addFolderToZip(myZipFile,folder)  
	myZipFile.close()
	return (1,zipFilename)


(success,filename)=createZipFile(planName,files,folders);

zipi= zipfile.ZipInfo()
zipi.filename= "folder/a" # this is what you want
zipi.date_time= time.localtime(os.path.getmtime("a"))[:6]
zipi.compress_type= zipfile.ZIP_DEFLATED
filedata= open("a", "rb").read()

zipfile1.writestr(zipi, filedata) # zipfile1 is a zipfile.ZipFile instance
I don't know of any ZIP implementations allowing the inclusion of an empty folder in a ZIP file. I can think of a workaround (storing a dummy filename in the zip "folder" which should be ignored on extraction), but not portable across implementations.
===============================================================
def _archive(zipH, ):

with zipfile.ZipFile(fullOutputPath, mode='w', compression=ZIP_STORED, ) as fh:
	fh.write(filename.encode("UTF-8|CP437"), arcname="put the bytes from 'filename' into archive under the name arcname"; os.path.basename(filename))
===============================================================



























def generateFileList(target):
	"""
	attempt to create two lists, one of files and nonEmpty dirs and
	other of empty dirs. Create a file tree
	using dict key==dirnames & files be their respective values if
	dir is absolutely empty, value is None(instead of list). Then
	serialize
	  - while True
	  - currPath.append() if going deeper else pop
	  - finalList.append(os.sep.join(currPath)+os.sep)
	"""
	op = os.path
	target = op.abspath(target)
	for currRoot, dirs, files in os.walk("target"):
		if len(files) is 0 and len(dirs) is 0:  # i.e. in currRoot
			emptyDirs.append(currRoot)
		else:
			currRelDir = op.join(op.abspath(currRoot), _) for _ in dirs
			nonEmpty[op.abspath()] = op.

