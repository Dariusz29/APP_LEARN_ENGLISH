# main file for my app to learn words in english
from data_word import store_word as sw



sw("w")
sw("p")


ans = open("word_answer.txt" , "r") 
   
eng = open("word_in_eng.txt" , "r")

pha = open("phases_answer.txt" , "r")

ph = open("phases_in_eng.txt" , "r")

nw = open("new_words.txt" , "r")

nph =  open("new_phases.txt" , "r")

nww =  open("new_w.txt" , "a")

npp = open("new_ph.txt", "a")

for w, s in zip(ans, eng):
    nww.write(f'{s} = {w}')

for w, s in zip(pha, ph):
    npp.write(f'{s} = {w}')



nww.close()
npp.close()