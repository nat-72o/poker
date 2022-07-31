import os
import re 

hands = ""

from pathlib import Path
for file in Path("/home/gambit-72o/Documents/Hand-History/Hands").iterdir():
    proxy = file.read_text()
    hands = proxy + hands


isolated = re.findall('\*{3} HOLE CARDS \*{3}(.*?)\*{3} FLOP \*{3}', hands, flags=re.M|re.S)
total_hands = len(isolated) 
me_raises_len = '\n'.join(isolated).count('[ME] : Raises')
print(isolated)
#print("total hands is:", total_hands)
#print("total raises is: ", me_raises_len)
print(me_raises_len)
print(f'{total_hands=}')
VPIP = me_raises_len / total_hands
print(VPIP)