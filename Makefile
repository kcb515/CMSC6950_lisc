report.pdf: report.tex counts.png document.png
	latexmk -pdf

counts.png: plot.py
	python3 plot.py

document.png: plot2.py
	python3 plot.py

test.py: python3 test.py
