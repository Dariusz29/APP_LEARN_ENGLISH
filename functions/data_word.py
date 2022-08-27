word_sourse = open("source_data\\words_tutlo.txt", "r")
word_sourse_ = open("source_data\\new_words.txt", "r")
phases_sourse = open("source_data\\new_phases.txt", "r")
word_in_eng = open('data_to_learn\\word_in_eng.txt',"w")
word_answer = open('data_to_learn\\word_answer.txt','w')
phases_in_eng = open('data_to_learn\\phases_in_eng.txt','w')
phases_answer = open('data_to_learn\\phases_answer.txt', 'w')
#C:\Users\dariu\Desktop\my_projects\App_learn_words\source_data\words_tutlo.txt
word_eng = []
word_ans = []
phases_eng = []
phases_ans = []

def store_word(resp):

    def wordss():
    
        for w in word_sourse:

            if "=" in w:
                data = w.split('=')
                word_eng.append(data[0].lower())
                word_ans.append(data[1].lower())
            elif "-" in w:
                data = w.split('-')
                word_eng.append(data[0].lower())
                word_ans.append(data[1].lower())

        for w in word_sourse_:

            if "=" in w:
                data = w.split('=')
                word_eng.append(data[0].lower())
                word_ans.append(data[1].lower())
            elif "-" in w:
                data = w.split('-')
                word_eng.append(data[0].lower())
                word_ans.append(data[1].lower())
    
        for i in word_eng:
            word_in_eng.write(i)
            word_in_eng.write('\n')

        for i in word_ans:
            word_answer.write(i)
        
        word_in_eng.close()
        word_answer.close()


    def phass():  
      
        for w in phases_sourse:
            
            if "=" in w :
                data = w.split('=')
                phases_eng.append(data[0].lower())
                phases_ans.append(data[1].lower())
            elif "-" in w :
                data = w.split('-')
                phases_eng.append(data[0].lower())
                phases_ans.append(data[1].lower())
    
        for i in phases_eng: 
            phases_in_eng.write(i)
            phases_in_eng.write('\n')

        for i in phases_ans:
            phases_answer.write(i)
        
        phases_in_eng.close()
        phases_answer.close()   

    if resp == 'w':
        wordss()
    elif resp == 'p':
        phass()