cd ..
pdftex -ini -jobname="tekstopmaak" "&pdflatex" mylatexformat.ltx 2_Tekstopmaak.tex
move tekstopmaak.fmt auxdir/tekstopmaak.fmt
move tekstopmaak.log auxdir/tekstopmaakFmt.log
del tekstopmaak.pdf
PAUSE
