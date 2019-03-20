class NormalSample:
    """A class for generating and analyzing samples from a Normal distribution"""
    
    def __init__(self,mu,sig,size):
        "mu = population mean, sig = population standard deviation"
        "size =  sizze of sample to generate"
        from random import gauss,random
        self.mu = mu
        self.sig = sig
        self.sample = []
        for j in range(size):
            self.sample.append(gauss(mu,sig))
    
    def getSize(self):
        "returns size of sample"
        return len(self.sample)
    
    def getSample(self):
        "returns the sample"
        return self.sample
    
    def getMean(self):
        "returns the mean of the sample"
        size = self.getSize()
        return sum(self.sample)/size
        
    def getStdDev(self):
        "returns the sample standard deviation"
        temp = 0
        size = self.getSize()
        mean = self.getMean()
        for i in range(size):
            temp = temp + (self.sample[i] - mean)**2
        return temp/size
    
    def getMax(self):
        "returns the maximum value in the sample"
        return max(self.sample)

    def getMin(self):
        "returns the minimum of the sample"
        return min(self.sample)
        
    def getMed(self):
        "returns the median of the sample"
        sortSample = self.sort("a")
        size = self.getSize()
        if size%2 == 0:
            med = 0.5*(sortSample[size//2] + sortSample[(size//2) + 1]) 
        if size%2 !=0:
            med = sortSample[(size + 1)//2]
        return med
        
    def sort(self,order):
        "returns the sample in order"
        "order can be either 'a' for ascending and 'd' for descending"
        "'a' and 'd' are strings"
        size = self.getSize()
        sortSample = self.sample[0:size]
        if order == "d":
            for i in range(size):
                for j in range(i+1,size):
                    if sortSample[i] < sortSample[j]:
                        sortSample[i],sortSample[j] = sortSample[j],sortSample[i] 
        if order == "a":
            for i in range(size):
                for j in range(i+1,size):
                    if sortSample[i] > sortSample[j]:
                        sortSample[i],sortSample[j] = sortSample[j],sortSample[i]                   
        return sortSample
    
    def subSample(self,replacement,n):
        "returns a sub sample"
        "replacement takes on the string value 'w' for with replacement"
        "and 'wo' for without replacement"
        "n is an interger less than or equal to the sample size"
        from random import randint
        subSample = []
        lenSample = self.getSize()
        if replacement == "w":
            for i in range(n):
                index = randint(0,lenSample-1)
                subSample.append(self.sample[index])
        if replacement == "wo":
            temp = self.sample
            for i in range(n):
                lentemp = len(temp)
                index = randint(0,lentemp-1)
                subSample.append(temp[index])
                temp = temp[0:index] + temp[(index+1):lentemp]
        return subSample

    def quantile(self,p):
        "returns the pth quantile of the sample"
        "p is between 0 and 1 open interval"
        from math import ceil
        sample = self.sample
        size = self.getSize()
        q = p*size
        sortSample = self.sort("a")
        if q.is_integer():
            q = int(q)
            quant = .5*(sortSample[q]+sortSample[q+1])
        else:
            q = int(ceil(q))
            quant = sortSample[q]
        return(quant)







        
