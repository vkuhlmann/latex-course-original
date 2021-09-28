cd ..
pdftex -ini -jobname="presentatie" "&pdflatex" mylatexformat.ltx presentatie.tex
move presentatie.fmt auxdir/presentatie.fmt
move presentatie.log auxdir/presentatieFmt.log
del presentatie.pdf
PAUSE
