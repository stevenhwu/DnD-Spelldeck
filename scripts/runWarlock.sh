class="warlock"
ll=1
nameOne=(-n"Armor of Agathys" -n"Arms of Hadar" -n"Charm Person" -n"Comprehend Languages" -n"Expeditious Retreat" -n"Hellish Rebuke" -n"Hex" -n"Illusory Script" -n"Protection from Evil and Good" -n"Unseen Servant" -n"Witch Bolt")

python3 generate.py -c $class "${nameOne[@]}" > tex/spells.tex
latexmk -xelatex -cd tex/cards.tex tex/printable.tex > /dev/null
cp ./tex/printable.pdf "./class/${class}_${ll}.pdf"

# ll=2
# nameTwo=()
# python3 generate.py -c $class "${nameTwo[@]}" > tex/spells.tex
# latexmk -xelatex -cd tex/cards.tex tex/printable.tex &> /dev/null
# cp ./tex/printable.pdf "./class/${class}_${ll}.pdf"
