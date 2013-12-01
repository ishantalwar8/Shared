#---------------------------------------------------------------------------
# Core Solution
# Name:        ClassCode
# Purpose:     Read a CSV file to display the maximum value of company shares
# Author:      Ishan Talwar
# Created:     1-Dec-2013
# Last Updated: 1-Dec-2013
#---------------------------------------------------------------------------

import csv

class SharesAnalysis(): 
    '''
    SharesAnalysis class provides function to show the maximum share value for all the compnaies
    as well as for a particular company.
    '''
    def __init__(self):
        '''
        Constructor to read .csv file and set its content as attribute
        '''
        with open('Shares.csv', 'rb') as fileHand:
            fileReader = csv.reader(fileHand)
            self.fileList = list(fileReader)
          
    def _fetch(self, indexValue):
        '''
        Sorts the list for a particular index using custom sorting method
        @Input: Index value to perform sorting
        @Itye: Integer
        @Return: Year month value
        @rtype: String
        '''
        result = sorted(self.fileList[1:], key = lambda value: int(value[indexValue+2]))[-1]
        return "%s %s %s" % (result[0],result[1],result[indexValue+2])
            
    def getResult(self):
        '''
        Print the result for all the companies
        '''
        for ind in range(len(self.fileList[0][2:])):
            maxResult = self._fetch(ind)
            print self.fileList[0][2:][ind], maxResult
    
    def queryCompResult(self, companyName):
        '''
        Get the result for a particular company
        @Input: Name of the Company
        @Itye: String
        @Return: Year month value / message
        @rtype: String
        '''
        if companyName in self.fileList[0][2:]:
            ind = self.fileList[0][2:].index(companyName)
            return self._fetch(ind)
        else:
            return "Invalid company name"
            
if __name__ =="__main__":
    share = SharesAnalysis()
    print "Name\tYear Month Value"
    share.getResult()

    

    
