class="paladin"
ll=1
nameOne=(-n"Bless" -n"Command" -n"Compelled Duel" -n"Cure Wounds" -n"Detect Evil and Good" -n"Detect Magic" -n"Detect Poison and Disease" -n"Divine Favor" -n"Heroism" -n"Protection from Evil and Good" -n"Purify Food and Drink" -n"Searing Smite" -n"Shield of Faith" -n"Thunderous Smite" -n"Wrathful Smite")

python3 generate.py -c $class "${nameOne[@]}" > tex/spells.tex
latexmk -xelatex -cd tex/cards.tex tex/printable.tex > /dev/null
cp ./tex/printable.pdf "./class/${class}_${ll}.pdf"

ll=2
nameTwo=(-n"Aid" -n"Branding Smite" -n"Find Steed" -n"Lesser Restoration" -n"Locate Object" -n"Magic Weapon" -n"Protection from Poison" -n"Zone of Truth")
python3 generate.py -c $class "${nameTwo[@]}"   > tex/spells.tex
latexmk -xelatex -cd tex/cards.tex tex/printable.tex &> /dev/null
cp ./tex/printable.pdf "./class/${class}_${ll}.pdf"
