import zipfile
import glob

def makeRelative(target, home):
	# Archive names should be relative to the archive root, that is, they should not start with a path separator

def archive(dirList, fileList, deleteOnSuccess=False, outputFileName=None, outputPath=None):
	if outputFileName is None:
		outputFileName = os.path.basename(os.path.abspath("."))
	if outputPath is None:
		outputPath = r"%temp%"
	fullOutputPath = os.path.join(outputPath, outputFileName)
	makeRelative(dirList, outputPath)
	makeRelative(fileList, outputPath)

	for _ in dirList:	# dirList is list of absolute paths
		if os.path.isdir(_):
			if os.stat(_)[6] is 0:
				# special case, empty dir
			for aFile in glob.glob(_+os.sep+"*"):

		else:
			# special case, dir doesn't exist
	for _ in fileList:
		if os.path.isfile(_):
			#
		else:
			# special case, file doesn't exist

	with zipfile.ZipFile(fullOutputPath.encode("UTF-8"), mode='a', compression=ZIP_STORED) as zfh:
		do(zfh, )
	print("Zip file successfully created")
	os.start(fullOutputPath)

	if deleteOnSuccess:
		if os.path.isfile(fullOutputPath):
			with zipfile.ZipFile(fullOutputPath, mode='w') as x:
				if x.testzip() not None:
					print("File is corrupted, not deleteing")
					return
			subprocess.call("del %(BLANK)s" % locals(), shell=True)
	return











def archive(outputFileName, dirList, fileList, deleteOnSuccess, outputPath=".", frmt="ZIP", level="STORE", method=None):
	if frmt is "zip":
		from zipfile import ZipFile as Frmt

	elif frmt is "bz2":
		from zipfile import BZ2File as Frmt

	elif frmt is "7z":
		from svnZipAPI import BLANK as Frmt
		if method is "lzma":
			compress = lambda *args: Frmt(level=Ultra, args)
			compress = lambda *args: Frmt(level=Store, args)
		elif method is "ppmd"
		else

	elif...
	else:
		# simply zip it
	
