## DREAM
```
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
	

```