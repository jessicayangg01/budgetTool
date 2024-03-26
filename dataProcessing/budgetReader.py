import pandas as pd

class budgetReader(object):
    def __init__(self, fileName, data_logger):
        self.data = pd.read_csv(fileName)
        self.filename = fileName
        
        self.data_logger = data_logger
        self.data_logger.addtext("Data loaded successfully.")
    
    def getCol(self):
        return self.data.columns

    def numRows(self):
        return len(self.data)
    
    def dataClean(self):
        self.data_logger.addtext("________________________________________________________ ")
        self.data_logger.addtext("Data cleaning for " + self.filename + "... ")
        
        self.data_logger.addtext(" ")
        self.data_logger.addtext("Taking out None Data")
        old = self.numRows()
        self.data.dropna(subset=self.getCol(), inplace=True)
        self.data_logger.addtext("Removed " + str(old - self.numRows()) + " rows of None Data.")
        
        # self.dataDict = self.data.to_dict("list")

        self.data_logger.addtext(" ")
        self.data_logger.addtext("Assigning numeric values to string variables")


        for col in self.data:
            if not isinstance(self.data[col][0], float):
                self.data_logger.addtext(str(col)  +  " is a " +  str(type(self.data[col][0])) +  ". Data cleaning will assign integer values to each variable.")
                variables = set(self.data[col])
                changeVar = {}

                for index, var in enumerate(variables, 1):
                    changeVar[var] = index
                    self.data_logger.addtext(str(var) + " will be assigned to the numeric value of : " +  str(index))

                self.data = self.data.reset_index()
                for val in range(len(self.data[col])):
                    self.data.loc[val, col] = changeVar[self.data[col][val]]
        
        self.data_logger.addtext(" ")
        self.data_logger.addtext("Data preview:")
        self.data_logger.addtext(str(self.data))

        self.data_logger.addtext(" ")
        self.data_logger.addtext("Data finished cleaning.")
        self.data_logger.addtext("________________________________________________________ ")


    def delCol(self, colName):
        del self.dataDict[colName]
