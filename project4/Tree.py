'''
Created on Nov 18, 2012

@author: jsuit
'''

class Tree:
    '''
    classdocs
    '''


    def __init__(self, attrIndex, values  ):
        '''
        Constructor
        '''
        self.root = attrIndex
        self.branches = {}
        self.values = {}
        self.values[0] = values[0]
        self.values[1] = values[1]
        
        
    def getValues(self):
        return self.values
    
    def add(self, value, subTree):
        self.branches[value] = subTree
       
    def numBranches(self):
        return len(self.branches)
    
    def getRoot(self):
        return self.root
    def getBranches(self):
        return self.branches
    
    def getBranch(self, key):
        if(self.branches.has_key(key)):
            return self.branches[key]