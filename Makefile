report.pdf: report.tex counts.png document.png
	pdflatex $<

counts.png: plot.py
	python3 plot.py

document.png: plot2.py
	python3 plot2.py

test.py: python3 test.py

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm counts.png
	rm document.png

almost_clean:
	latexmk -c
