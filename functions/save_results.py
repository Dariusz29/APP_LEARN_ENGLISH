#saving history scores about my learn of vocabulary
import time



def save_results(result_,status):

    file = open('results_history.txt', 'a')
    t = time.asctime()
         
    if result_ == 'good':
        
        score  = '1'
        file.write(score)
        file.write('\n')
    
    elif result_ == 'half good':
        
        score = '0.5'
        file.write(score)
        file.write('\n')

    else:
        
        score = '0'
        file.write(score)
        file.write('\n')
    
    if status == True:

        file.write(f'End a test!!!, {t}')
        file.close()
        

    


    