'''
Created on Nov 18, 2012

@author: jsuit
'''

  
import Importance
import Tree
import gini


""" 
Recursive Function that tries to learn whether to assign a true or false

"""
def TreeLearner(examples, attrs, labels, values, parentlabels = None, fn = "infoGain" ):
    #attrs is a hash
    #examples is a hash
   
   
    if len(examples) == 0:
        return Importance.Plurality(parentlabels)
    elif Importance.sameClassification(examples, labels):
        
        for l in labels:
            return labels[l] 
    if (len(attrs) == 0):
        #majority rules
        return Importance.Plurality(labels)
    else:
       
    
    #chooseAttr according to fn 
        testValue = -1
        max = -1
        min = 10000
        maxIndex = -1;
        for attr in attrs:
            if fn == "infoGain":
                testValue = Importance.Importance(attr, examples, values,labels)
                if max < testValue:
                    maxIndex = attr
                    max = testValue
            else: 
                testValue = gini.giniD(examples, attr, labels)
               
                if min > testValue:
                    maxIndex = attr
                    min = testValue
                 
        tree = Tree.Tree(maxIndex, values)
        valdict = tree.getValues()
        newAttrs = Importance.remove(maxIndex, attrs)
        for v in valdict:
            exs = examples.copy()
            newLabels = labels.copy()
            for e in exs.keys():
                    if exs[e][maxIndex] != valdict[v]:
                        del exs[e]
                        del newLabels[e]
            if(fn == "infoGain"):
                subtree = TreeLearner(exs, newAttrs, newLabels, values, labels)   
            else:   
                subtree = TreeLearner(exs, newAttrs, newLabels, values, labels, "giniIndex")
            tree.add(v, subtree)
        return tree
    
    
            
      