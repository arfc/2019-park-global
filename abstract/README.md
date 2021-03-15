### Instructions
1. Building the pdf file for the abstract
- To build on a Linux machine run ``make``.
- To build on a Windows machine run
  - ``pdflatex abstract.tex``
  - ``bibtex abstract.tex``
  - ``pdflatex abstract.tex``
  - ``pdflatex abstract.tex``
2. To get rid of built files, ``make clean.``
