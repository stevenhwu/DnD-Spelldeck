## filter out classes

./search.py --no-class wizard --no-class warlock --no-class paladin -l 0 -l 1 > tex/spells.tex



### History
./generate.py -c Bard -c Cleric -c Druid -l 0
./generate.py -c Bard -c Cleric -c Druid -l 0 
./generate.py -c Bard -c Cleric -c Druid -l 0 > tex/spells.tex 

./generate.py -c fighter -c rouge -l 1
./generate.py -c fighter -c rouge -l 0
./generate.py -c fighter -c rouge -c ranger -l 0 | less



./search.py --duration "24 hours" | less
./search.py --duration "3 hours" | less
./search.py --duration "2 hours" | less
./search.py --duration "1 day" | less
./search.py --duration "1 hour" | less

./search.py -c cleric -c bard > tex/spells.tex 
./search.py -c cleric -c bard -l 1 > tex/spells.tex 
./search.py -c cleric -c bard -druid -l 0 > tex/spells.tex 
./search.py -c cleric -c bard -c druid -c fighter -l 0 > tex/spells.tex 
./search.py -c cleric -c bard -c druid -c fighter -c rouge -l 0 > tex/spells.tex 
./search.py -c cleric -c bard -c druid -c fighter -c rouge -l 1 > tex/spells.tex 
./search.py -c cleric -c bard -c druid -c fighter -c rouge -l 2 > tex/spells.tex 
./search.py --no-class wizard --no-class warlock --no-class paladin -l 0 -l 1 > tex/spells.tex 


./search.py -d wizard -d warlock -d paladin  -c cleric -c bard -l 4 | less

