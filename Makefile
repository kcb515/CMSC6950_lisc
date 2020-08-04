report.pdf: report.tex counts.png document.png organism.png
	pdflatex $<

counts.png: plot.py
	python3 plot.py

document.png: plot2.py
	python3 plot2.py

organism.png: plot3.py
	python3 plot3.py

data1.py: python3 data1.py

data2.py: python3 data2.py

.PHONY: clean almost_clean

clean: almost_clean
	rm *.pdf
	rm *.png

almost_clean:
	latexmk -c
