cd ..
pdftex -ini -jobname="afbeeldingen" "&pdflatex" mylatexformat.ltx 4_Afbeeldingen.tex
move afbeeldingen.fmt auxdir/afbeeldingen.fmt
move afbeeldingen.log auxdir/afbeeldingenFmt.log
del afbeeldingen.pdf
PAUSE
