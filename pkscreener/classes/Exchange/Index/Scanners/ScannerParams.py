"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""

class ScannerParams:
    def __init__(self):
        return

    @property
    def runOption(self):
        return None

    @property
    def menuOption(self):
        return None
    
    @property
    def exchangeName(self):
        return None
    
    @property
    def executeOption(self):
        return None

    @property
    def reversalOption(self):
        return None
        
    @property
    def maLength(self):
        return None
    
    @property
    def daysForLowestVolume(self):
        return None
    
    @property
    def minValue(self):
        return None
    
    @property
    def maxValue(self):
        return None

    @property
    def respChartPattern(self):
        return None

    @property
    def insideBarToLookback(self):
        return None

    @property
    def totalStocks(self):
        return None
    
    @property
    def cacheEnabled(self):
        return None

    @property
    def stock(self):
        return None

    @property
    def newlyListedOnly(self):
        return None

    @property
    def downloadOnly(self):
        return None
    
    @property
    def volumeRatio(self):
        return None
    
    @property
    def testBuild(self):
        return None
    
    @property
    def userArgs(self):
        return None
    
    @property
    def daysInPast(self):
        return None
    
    @property
    def backtestPeriod(self):
        return None
    
    @property
    def logLevel(self):
        return None
    
    @property
    def calculatePortfolio(self):
        return None
    
    @property
    def testData(self):
        return None