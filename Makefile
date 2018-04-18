
SRC += chapters/uvod.tex chapters/analyza.tex chapters/implementace.tex chapters/navrh.tex chapters/testovani.tex chapters/teorie.tex chapters/zaver.tex chapters/prirucka.tex chapters/nasazeni.tex

all:
	vlna -l -m -n $(SRC) DP_Cervenka_Ondrej_2018.tex
	pdflatex -shell-escape DP_Cervenka_Ondrej_2018
	bibtex DP_Cervenka_Ondrej_2018
	pdflatex -shell-escape DP_Cervenka_Ondrej_2018
	pdflatex -shell-escape DP_Cervenka_Ondrej_2018