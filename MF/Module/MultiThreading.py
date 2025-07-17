import concurrent.futures

class MysteryThreading:    

    #スレッドの起動
    def Create(self, bootingThreadValu):

        thread = concurrent.futures.ThreadPoolExecutor(bootingThreadValu)
        
        print("Thread is Booting COMPLATE! : [", bootingThreadValu, "] Threads")

        return thread
