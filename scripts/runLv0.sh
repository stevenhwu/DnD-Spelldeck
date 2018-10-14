# for class in wizard warlock bard cleric druid; do
for class in wizard warlock; do
    for ll in 0; do
        echo $class $ll
        python3 generate.py -c $class -l $ll > tex/spells.tex
        latexmk -xelatex -cd tex/cards.tex tex/printable.tex &> /dev/null
        cp ./tex/printable.pdf "./class/${class}_${ll}.pdf"
    done
done

#okular  tex/printable.pdf tex/cards.pdf
