class="wizard"
ll=1
nameOne=(-n"Alarm" -n"Burning Hands" -n"Charm Person" -n"Chromatic Orb" -n"Color Spray" -n"Comprehend Languages" -n"Detect Magic" -n"Disguise Self" -n"Expeditious Retreat" -n"False Life" -n"Feather Fall" -n"Find Familiar" -n"Fog Cloud" -n"Grease" -n"Identify" -n"Illusory Script" -n"Jump" -n"Longstrider" -n"Mage Armor" -n"Magic Missile" -n"Protection from Evil and Good" -n"Ray of Sickness" -n"Shield" -n"Silent Image" -n"Sleep" -n"Tasha's Hideous Laughter" -n"Tenser's Floating Disk" -n"Thunderwave" -n"Unseen Servant" -n"Witch Bolt")

python3 generate.py -c $class "${nameOne[@]}" > tex/spells.tex
latexmk -xelatex -cd tex/cards.tex tex/printable.tex > /dev/null
cp ./tex/printable.pdf "./class/${class}_${ll}.pdf"

ll=2
nameTwo=()
python3 generate.py -c $class "${nameTwo[@]}" -l $ll > tex/spells.tex
latexmk -xelatex -cd tex/cards.tex tex/printable.tex &> /dev/null
cp ./tex/printable.pdf "./class/${class}_${ll}.pdf"
#34 spells PHB
