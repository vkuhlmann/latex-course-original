cd ..
pdftex -ini -jobname="bibliografie" "&pdflatex" mylatexformat.ltx 6_Bibliografie.tex
move bibliografie.fmt auxdir/bibliografie.fmt
move bibliografie.log auxdir/bibliografieFmt.log
del bibliografie.pdf
PAUSE
