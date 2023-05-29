'''
Prompt:
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
'''

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        #i is the customer, j is the bank they have money in.
        #we need to jump through each of the columns at every row i

        best = 0
        sums = 0

        for i in range(len(accounts)): #the number of rows
            for j in range(len(accounts[0])): #the number of cols in each row
                sums += accounts[i][j]
            if sums >= best:
                best = sums
            sums = 0 #reset sum for each account holder

        return best
