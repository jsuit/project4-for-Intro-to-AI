'''
Created on Nov 26, 2012

@author: jsuit
'''


"gini: a math function defined in notes"
def gini(labels):
    p_k = 0.0;
    n_k = 0.0;
    sum = 0.0;
    #labels are a dict
    for v in labels:
        if labels[v]:
            p_k+=1.0
        else: 
            n_k+=1.0
            
    total = p_k + n_k;
    if total == 0: 
        return 0
    sum = (p_k/total)*p_k/total + (n_k/total)*(n_k/total) 
  
    return 1 - sum;
    
def giniD(examples, attr, labels):
                   
             #examples are dict
             #attr is an index into each example
             p_k = 0.0
             n_k = 0.0
             S_1 = {}
             S_0 = {}
             newLabelS1 = {}
             newLabelS0 = {}
             for ex in examples:
                     if examples[ex][attr]:
                         p_k+=1.0
                         S_1[ex] = examples[ex]
                         newLabelS1[ex] = labels[ex]
                     else:
                        n_k+=1.0
                        S_0[ex] = examples[ex]
                        newLabelS0[ex] = labels[ex]
             sum = 0.0
             sum = p_k + n_k
             giniTotal = float((p_k/sum)* gini(newLabelS1)) + float((n_k/sum) * gini(newLabelS0))
             
             return giniTotal
            
            