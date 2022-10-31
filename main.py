import os.path
import glob
import pikepdf

#Get all pdfs
path = 'input\*.pdf'
files = glob.glob(path)

merge_pdf = pikepdf.Pdf.new()

for file in files:
	with pikepdf.open(file) as pdf:
		pdf.save('output/' + os.path.basename(file))
		merge_pdf.pages.extend(pdf.pages)

#Save a single PDF that is a combination of all input
merge_pdf.remove_unreferenced_resources()
merge_pdf.save('output/_combined_file.pdf')