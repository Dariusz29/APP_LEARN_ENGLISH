#saving history scores about my learn of vocabulary


with open('results_history.txt', 'r') as rh:
    rh = rh


def save_results(result, results=rh):

    if result == 'good':
        results[len(results)+1] = 1
    
    elif result == 'half good':
        results[len(results)+1] = 0.5

    else:
        results[len(results)+1] = 0

    for w in results:
        rh.write(w)
        rh.write('\n')

    rh.close