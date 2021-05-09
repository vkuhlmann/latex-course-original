cd ..
pdftex -ini -jobname="formules" "&pdflatex" mylatexformat.ltx formules.tex
move formules.fmt auxdir/formules.fmt
move formules.log auxdir/formulesFmt.log
PAUSE
