#ask user about kind of which you choice 

from unittest import result
from functions.data_word import store_word as sw
import random
from functions.save_results import save_results as sr


# Main of exam
def kind_test():
    while True:
        input("""
        Learn english words = TEST_1
        Learn english phases = TEST_2
        \n
        Number learn words or phases:

        1. 5
        2. 10
        3. 15
        4. 20
        5. 25
        """)
        test = input('Which are you choice test? ')
        n = input('How much words or phases are you learn in the TEST? ')

        if test == 'TEST_1':
            TEST.start_test_word(n)
            break
        elif test == 'TEST_2':
            TEST.start_test_phase(n)
            break
        else:
            print('You type not expected thing, try again')
            break


# feature to take exam with phases
class TEST():

    def __init__(self,i):
        self.i = i
        

    
    def start_test_phase(i):

        sw('p')
        with open('data_to_learn\\phases_in_eng.txt', 'r') as pp:
            pp = list(pp)
        with open('data_to_learn\\phases_answer.txt', 'r') as pa:
            pa = list(pa)
        
        phas = {}
        ans = {}
        check = []
        senp = [] 
        

        for i in range(0,int(i)):
            phases = random.choice(pp)
            num_pp = pp.index(phases)
            num_an = num_pp
            answer = input(f'Type translation {phases} = ')    
                
            
            for i, v in enumerate(pa[num_an]):
                phas[i] = v

            for i, v in enumerate(answer):
                ans[i] = v

            for i in range(len(ans.keys())):

                if phas[i] == ans[i]:
                    check.append(1)
                     
                else:

                    check.append(0)                   

            if sum(check) == len(phas.keys()):
                print("""
                Great answer!!!
                Next word....""", pa[num_an])

            elif sum(check) >= len(phas.keys())//2:
                print("""
                Your answer is in half right.
                Next word....""",pa[num_an])
                print(f'Create sentance with {phases}')
                sentence = input("\n...")
                senp.append(sentence)
    
            else:
                print("""
                Bad answer
                Next word....""",pa[num_an])
                print(f'Create sentance with {phases}')
                sentence = input("\n...")
                senp.append(sentence)
                
        print("Test is finish!")
        print(senp)


# feature to exam with words
# wrong examine translations
# in data are lot of wrong connecting word with answer
    def start_test_word(i):

        sw('w')
        with open('data_to_learn\\word_in_eng.txt', 'r') as ww:
            ww = list(ww)
        with open('data_to_learn\\word_answer.txt', 'r') as an:
            an = list(an)
        
        
        
        word = {}
        ans = {}
        check = []
        sen = []


        for i in range(0,int(i)):
            result = ''
            words = random.choice(ww)
            num_ww = ww.index(words)
            num_an = num_ww
            answer = input(f'Type translation {words} = ')    
            print(num_ww)
            print(num_an)   

            

            

        
            for i, v in enumerate(an[num_an]):
                word[i] = v

            for i, v in enumerate(answer):
                ans[i] = v

            
            for i in range(len(ans.keys())):

                if word[i] == ans[i]:
                    check.append(1)
                    print(check)
                    
                else:

                    check.append(0)
                    print(check)

            if sum(check) == len(word.keys()):
                print("""
                Great answer!!!
                Next word....""", an[num_an])
                result = "good"
                

            elif sum(check) >= len(word.keys())//2:
                print("""
                Your answer is in half right.
                Next word....""",an[num_an])
                print(f'Create sentance with {words}')
                sentence = input("\n...")
                sen.append(sentence)
                result = 'half good'
    
            else:
                print("""
                Bad answer
                Next word....""",an[num_an])
                print(f'Create sentance with {words}')
                sentence = input("\n...")
                sen.append(sentence)
            sr(result) 

        

            
        
            
                
        print("Test is finish!")
        print(sen)


while True:

    kind_test()
    break


