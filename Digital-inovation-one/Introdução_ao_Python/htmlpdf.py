import weasyprint
 
weasyprint.HTML('https://www.delftstack.com/').write_pdf('sample.pdf')