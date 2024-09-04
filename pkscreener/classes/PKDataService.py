#!/usr/bin/python3
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

import json
from pkscreener.classes.PKTask import PKTask
from PKDevTools.classes.SuppressOutput import SuppressOutput
from pkscreener.classes.PKScheduler import PKScheduler
from PKDevTools.classes.log import default_logger

class PKDataService():
    def getSymbolsAndSectorInfo(self,configManager,stockCodes=[]):
        from PKNSETools.PKCompanyGeneral import download, initialize
        stockDictList = []
        tasksList = []
        for symbol in stockCodes:
            fn_args = (symbol)
            task = PKTask(f"DataDownload-{symbol}",long_running_fn=download,long_running_fn_args=fn_args)
            task.userData = symbol
            tasksList.append(task)
        
        processedStocks = []
        if len(tasksList) > 0:
            # Suppress any multiprocessing errors/warnings
            with SuppressOutput(suppress_stderr=True, suppress_stdout=True):
                initialize() # Let's get the cookies set-up right
                PKScheduler.scheduleTasks(tasksList=tasksList,
                                        label=f"Downloading latest symbol/sector info. (Total={len(stockCodes)} records in {len(tasksList)} batches){'Be Patient!' if len(stockCodes)> 2000 else ''}",
                                        timeout=(5+2.5*configManager.longTimeout*4), # 5 seconds additional time for getting multiprocessing ready
                                        minAcceptableCompletionPercentage=100,
                                        submitTaskAsArgs=True,
                                        showProgressBars=True)
            for task in tasksList:
                if task.result is not None:
                    taskResult = json.loads(task.result)
                    if taskResult is not None and isinstance(taskResult,dict) and "info" in taskResult.keys():
                        stockDictList.append(taskResult.get("info"))
                        processedStocks.append(task.userData)
        leftOutStocks = list(set(stockCodes)-set(processedStocks))
        default_logger().debug(f"Attempted fresh download of {len(stockCodes)} stocks and downloaded {len(processedStocks)} stocks. {len(leftOutStocks)} stocks remaining.")
        return stockDictList, leftOutStocks
