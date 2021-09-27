cd ..
pdftex -ini -jobname="inleiding" "&pdflatex" mylatexformat.ltx 1_Inleiding.tex
move inleiding.fmt auxdir/inleiding.fmt
move inleiding.log auxdir/inleidingFmt.log
del inleiding.pdf
PAUSE
