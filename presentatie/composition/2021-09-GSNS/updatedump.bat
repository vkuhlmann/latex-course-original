pdftex -ini -jobname="tekstopmaak" "&pdflatex" mylatexformat.ltx 2_Tekstopmaak.tex
move tekstopmaak.fmt auxdir/tekstopmaak.fmt
move tekstopmaak.log auxdir/tekstopmaakFmt.log

pdftex -ini -jobname="formules" "&pdflatex" mylatexformat.ltx 5_Formules.tex
move formules.fmt auxdir/formules.fmt
move formules.log auxdir/formulesFmt.log
PAUSE
