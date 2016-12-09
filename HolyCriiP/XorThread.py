import threading, Files, Monitor

class XorThread(threading.Thread):

    def __init__(self, num, fileToOverwrite, dataRead, xorKey, event, monitor):
        threading.Thread.__init__(self)
        self.num = num
        self.fileToOverwrite = fileToOverwrite
        self.dataRead = dataRead
        self.xorKey = xorKey
        self.event = event
        self.monitor = monitor

    def run(self):

        print ("Starting {}".format(self.num))
        xorProcess(self)
        print ("Exiting {}".format(self.num))

def xorProcess(self):

        data = bytearray(self.dataRead)
        print ("Thread in XOR {}".format(self.num))
        for i in range(len(data)):
            data[i] ^= self.xorKey
        writeFileThread(self, data)

def writeFileThread(self, data):

    print ("Thread Wait {}".format(self.num))
    orderList = self.num - 1
    if (self.num == 1):
        self.monitor.setThreadToSet(orderList)
    self.monitor.setThreadToWait(orderList)
    print ("Thread Write {}".format(self.num))
    self.fileToOverwrite.write(data)
    self.monitor.setThreadToClear(orderList)
    if (self.monitor.isLastThread(self.num) == False):
        self.monitor.setThreadToSet(orderList + 1) #Set thread after him