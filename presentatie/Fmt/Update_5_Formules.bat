cd ..
pdftex -ini -jobname="formules" "&pdflatex" mylatexformat.ltx 5_Formules.tex
move formules.fmt auxdir/formules.fmt
move formules.log auxdir/formulesFmt.log
del formules.pdf
PAUSE
