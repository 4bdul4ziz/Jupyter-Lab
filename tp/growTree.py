'''
Algorithm - GrowTree(D, F) - grows a feature tree from training data
Input - data D, set of features F
Output - feature tree T with labelled leaves
if Homogeneous(D) then return Label(D);
S <- BestSplit(D, F);
split D into subsets Di according to the literals in S;
for each i, do 
    if Di != phi then Ti <- GrowTree(Di, F);
    else Ti is a leaf labelled with Label(D);
end
return a tree whose root is labelled with S and whose childeren are Ti

Algorithm - BestSplit-Class(D, F) - find the best split for a decision tree
Input - data D, set of features F
Output - feature f to split on
Imin <- 1;
for each f < F do
    split D into subsets D1, ...., Dl according to the values vj of f;
    i IMp({D1,....,Dl}) < Imin then
        Imin <- Imp({D1,....,Dl});
        fbest <- f;
    end
end
return fbest;
'''

import math
import random
import sys
import time
import numpy as np
import pandas as pd


class GrowTree:
    def __init__(self, data, features, target, depth=0):
        self.data = data
        self.features = features
        self.target = target
        self.depth = depth
        self.children = []
        self.split = None
        self.label = None
        self.leaf = False
        self.grow()

    def grow(self):
        if self.homogeneous():
            self.leaf = True
            self.label = self.data[self.target].iloc[0]
        else:
            self.split = self.best_split()
            for value in self.split.values:
                subset = self.data[self.data[self.split.feature] == value]
                if len(subset) > 0:
                    self.children.append(GrowTree(subset, self.features, self.target, self.depth + 1))
                else:
                    self.children.append(GrowTree(self.data, self.features, self.target, self.depth + 1))

    def homogeneous(self):
        return len(self.data[self.target].unique()) == 1

    def best_split(self):
        best = None
        for feature in self.features:
            split = Split(self.data, feature, self.target)
            if best is None or split.impurity < best.impurity:
                best = split
        return best

    def __str__(self):
        if self.leaf:
            return str(self.label)
        else:
            return str(self.split)

    def __repr__(self):
        if self.leaf:
            return str(self.label)
        else:
            return str(self.split)

    def predict(self, row):
        if self.leaf:
            return self.label
        else:
            value = row[self.split.feature]
            for child in self.children:
                if child.split.value == value:
                    return child.predict(row)

    def print_tree(self):
        print('  ' * self.depth + str(self))
        for child in self.children:
            child.print_tree()


    
class Split:
    def __init__(self, data, feature, target):
        self.feature = feature
        self.values = data[feature].unique()
        self.impurity = self.impurity(data, feature, target)

    def impurity(self, data, feature, target):
        total = len(data)
        impurity = 0
        for value in self.values:
            subset = data[data[feature] == value]
            p = len(subset) / total
            impurity += p * self.entropy(subset[target])
        return impurity

    def entropy(self, target):
        total = len(target)
        entropy = 0
        for value in target.unique():
            p = len(target[target == value]) / total
            entropy -= p * math.log(p, 2)
        return entropy

    def __str__(self):
        return self.feature + ' = ' + str(self.value)

    def __repr__(self):
        return self.feature + ' = ' + str(self.value)

def main():
    data = pd.read_table('tp/data.txt', sep=',', header=None)
    features = data.columns[:-1]
    target = data.columns[-1]
    tree = GrowTree(data, features, target)
    tree.print_tree()
    print(tree.predict(data.iloc[0]))

if __name__ == '__main__':
    main()
    
