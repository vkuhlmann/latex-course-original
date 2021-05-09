cd ..
pdftex -ini -jobname="documentstructuur" "&pdflatex" mylatexformat.ltx 3_Documentstructuur.tex
move documentstructuur.fmt auxdir/documentstructuur.fmt
move documentstructuur.log auxdir/documentstructuurFmt.log
del documentstructuur.pdf
PAUSE
