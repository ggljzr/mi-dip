
all:
	vlna DP_Cervenka_Ondrej_2018.tex
	pdflatex -shell-escape DP_Cervenka_Ondrej_2018
	bibtex DP_Cervenka_Ondrej_2018
	pdflatex -shell-escape DP_Cervenka_Ondrej_2018
	pdflatex -shell-escape DP_Cervenka_Ondrej_2018