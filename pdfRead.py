

import pyPdf, optparse
from pyPdf import PdfFileReader

def banner():
    print "##### PDF Reader p94 #####"

def printMeta(filename):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
            docinfo  pdfFile.getDocumentInfo()
            print '[*] PDF Metadata for: '+str(fileName)
            for metaItem in docInfo:
            	print '[+] '+metaItem+':'+docInfo[metaItem]

def main():
	banner()
	parser = optparse.OptionParser('usage%prog '+'-F <PDF File Name>')
	parser.add_option('-F', dest='filename', type ='string', help='Specify PDF File Name')
	(options, args) = parser.parse_args()
	fileName = options.fileName
	if filename == None:
		print parser.usage
		exit(0)
	else:
		printMeta(fileName)

if __name__ == '__main__':
	main()
