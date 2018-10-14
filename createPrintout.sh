#!/usr/bin/bash

# python3 generate.py -c $class -l $ll > tex/spells.tex
latexmk -xelatex -cd tex/cards.tex tex/printable.tex &> /dev/null
