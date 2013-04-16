'''
Created on Nov 18, 2012

@author: jsuit
'''
import math

def entropy(prob):
        if(prob == 0 or prob == 1):
            return 0
        else: return -(prob * math.log(prob,2) + (1-prob)*math.log(1-prob,2))
    
def Importance(attrIndex, examples, values, labels):
            #example nums are list indexes into examples
                p = 0.0
                n = 0.0
                #examples is a dict
                for ex in examples:
                          if labels[ex]:
                                p+=1
                          else: n+=1  
                
                prob = float(p)
                prob = (p/float(p+n))
             
                prob = entropy(prob)
                total = 0.0
                for v in values:
                    # for every value of attribute,   
                    total += Remainder(attrIndex, v, examples, p+n, labels)
                    
                #print "prob - total", prob - total
                return prob - total
              
    
def Remainder(attrIndex, value, examples, totalSize, labels):         
                
                p_k = 0.0
                n_k = 0.0
                #examples is a dict
                #loop through the examples, then look at the attribute, then see if has the value in question,
                #Finally if the it is positive add one to P_k else add one to n_k
                
                for ex in examples:
                        example = examples[ex]
                        if example[attrIndex] == value:
                            if labels[ex]:
                                p_k +=1
                            else: n_k+=1
                
                p_kn_k = float(p_k + n_k)
                totalSize = float(totalSize)
                p_k = float(p_k)
                if p_k==0 :
                    return 0    
                return float(p_kn_k/totalSize)*entropy(float(p_k/(p_kn_k)))
               
def remove(attr, seq):
    """Return a copy of seq (or string) with all occurences of item removed.
    >>> removeall(3, [1, 2, 3, 3, 2, 1, 3])
    [1, 2, 2, 1]
    >>> removeall(4, [1, 2, 3])
    [1, 2, 3]
    """
    newDict = seq.copy()
    del newDict[attr]
    return newDict       
def sameClassification(examples, labels):
    
    for l in labels:
        truthValue = labels[l]
        break
    
    for l in labels:
        if truthValue != labels[l]:
             return False
        
    return True

def Plurality(labels):
        p_count = 0
        n_count = 0
        
        for l in labels:
            if labels[l] == 1:
                p_count +=1
            else: n_count +=1
            
    
        if p_count >= n_count:
            return 1
        else: return 0
        
        