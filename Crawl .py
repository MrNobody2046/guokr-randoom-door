import threading
from Queue import Queue
from bs4 import BeautifulSoup
import urllib2
import cPickle
import time

class Item(threading.Thread):
    def __init__(self,id):'
        threading.Thread.__init__(self)
        self.id = id
        self.url = "http://movie.douban.com/subject/%d/"%id
        self.data = time.ctime()
        self.dl_link = []
    
    def run:




res = []
class Crawl(threading.Thread):
    def __init__(self,begin,que,life=10):
        threading.Thread.__init__(self)
        self.url_format = "http://www.guokr.com/site/?page="
        self.begin = begin + 1
        self.life = life
        self.queue = que
    def run(self):
        for i in range(self.life):
            url = self.url_format+str(self.begin)
            self.queue.put(urllib2.urlopen(url))
            self.begin += 1
        print "Finished:",self.name
#        while self.life > 0:
#            if htmls.qsize() > 100:
#                pass
#            else:
#                print "Downloading Page[%d]..."%self.begin
#                url = self.url_format+str(self.begin)
#                htmls.put(urllib2.urlopen(url))
#                self.life -= 1
#                self.begin += 1
#            if self.life == 0:
#                break
        
class Process(threading.Thread):
    def __init__(self,que,life=10):
        threading.Thread.__init__(self)
        self.queue = que
        self.life = life
        
    def run(self):
        global res
        for i in range(self.life):
            soup = BeautifulSoup(self.queue.get())
#            print soup.prettify(encoding="gb2312")
            for a in soup('h2'):
                res.append(str(a.a['href']))
        print "Finished Process:",self.name
#        print res
#        while True:
#            if htmls.qsize() >= 1:
#                soup = BeautifulSoup(htmls.get())
#                for a in soup('h2'):
#                    res.append(str(a.a['href']))
#            else
            
def run(start=0):
    cs = []
    ps = []
    q = Queue()
    for i in range(10):
        c = Crawl(i*10+start,q)
        p = Process(q)
        cs.append(c)
        ps.append(p)
        c.start()
        p.start()
    for c in cs:
        c.join()
    for p in ps:
        p.join()
#    print len(res)
#    file1 = "Res_cPickle_%d.bin"%start
#    file2 = "Res_String_%d.txt"%start
#    file1 = open(file1, 'w')
#    file2 = open(file2,'w')
#    cPickle.dump(res,file1)
#    file2.write(str(res))

def main():
    for i in range(8):
        print "Run stage 1"
        run(i*100)

t1 = time.time()
main()
print time.time() - t1
        

