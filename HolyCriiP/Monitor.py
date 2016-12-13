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

    def requestAccess(self, numThread):
        if (numThread == 1):
            self.__setThreadToSet(numThread)
        self.__setThreadToWait(numThread)

    def reportFinally(self, numThread):
        if (self.__isLastThread(numThread) == False):
            self.__setThreadToSet((numThread + 1)) #Set next thread (numThread is the parameter because List started in 0)
        else:
            pass
    
    def setNewThreadInList(self, thread):
        self.thWatch.append(thread)

    def getThreadList(self):
        return self.thWatch

    def __setThreadToSet(self, numThread):
        
        self.thWatch[(numThread - 1)].event.set()
        #for i in self.thWatch:
        #    if (self.thWatch[i].num == numThread):
        #        self.thWatch[i].event.set()
        #    else:
        #        print("Thread no encontrado")

    def __setThreadToClear(self, numThread):
        self.thWatch[(numThread-1)].event.clear()

    def __setThreadToWait(self, numThread):
        self.thWatch[(numThread-1)].event.wait()

    def __isLastThread(self, numThread):
        if (len(self.thWatch) == numThread):
            return True
        else:
            return False