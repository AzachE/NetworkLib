import multiprocessing

class MyProcess(multiprocessing.Process):

    def __init__(self, ):
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()

    def run(self):
        while not self.exit.is_set():
            pass
        print "You exited!"

    def terminate(self):
        print "terminate initiated"
        self.exit.set()

