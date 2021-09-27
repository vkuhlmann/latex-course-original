cd ..
pdftex -ini -jobname="extras" "&pdflatex" mylatexformat.ltx 8_Extras.tex
move extras.fmt auxdir/extras.fmt
move extras.log auxdir/extrasFmt.log
del extras.pdf
PAUSE
