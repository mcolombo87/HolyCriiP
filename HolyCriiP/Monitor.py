import threading

class Monitor(threading.Thread):

    def __init__(self, num, thWatch):
        threading.Thread.__init__(self)
        self.num = num
        self.thWatch = thWatch

    def run(self):

        print ("Monitor Starting: Now my watch begins")

    def threadReport(self, numThread):

        print("Is Alive? {}".format(self.thWatch[numThread].is_alive()))
        print("Is ready? {}".format(self.thWatch[numThread].event.is_set()))

    def setThreadToSet(self, numThread):
        self.thWatch[numThread].event.set()

    def setThreadToClear(self, numThread):
        self.thWatch[numThread].event.clear()

    def setThreadToWait(self, numThread):
        self.thWatch[numThread].event.wait()
   
    def setNewThreadInList(self, thread):
        self.thWatch.append(thread)

    def getThreadList(self):
        return self.thWatch

    def isLastThread(self, numThread):
        if (len(self.thWatch) == numThread):
            return True
        else:
            return False