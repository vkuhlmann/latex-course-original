cd ..
pdftex -ini -jobname="goedomteweten" "&pdflatex" mylatexformat.ltx 7_GoedOmTeWeten.tex
move goedomteweten.fmt auxdir/goedomteweten.fmt
move goedomteweten.log auxdir/goedomtewetenFmt.log
del goedomteweten.pdf
PAUSE
