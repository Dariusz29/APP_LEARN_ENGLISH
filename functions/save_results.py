#saving history scores about my learn of vocabulary





def save_results(result_):

    with open('results_history.txt', 'r') as rh:
        results = list(rh)

    if result_ == 'good':
        print(len(results))
        score  = 1
        results.append(score)
    
    elif result_ == 'half good':
        print(len(results))
        score = 0.5
        results.append(score)

    else:
        print(len(results))
        score = 0
        results.append(score)

    for w in results:
        rh.write(w)
        rh.write('\n')

    