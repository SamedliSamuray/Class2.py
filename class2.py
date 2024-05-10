import itertools
class Metods:
    def __init__(self):
        pass    
    def list_creater(self, getlist):
        self.setlist = getlist[0:]
        return self.setlist  
    def sumFind(self, target_sum):
        write=False
        for a,b in itertools.combinations(range(len(self.setlist)),2):
            if self.setlist[a]+self.setlist[b]==target_sum and a!=b:
                write=True
                print(f'{self.setlist[a]} ededi indeksi {a}, {self.setlist[b]} ededi indeksi {b}')
        if write==False:
            print(f'{-1} -- list icindeki hec bir 2 deyerin cemi {target_sum} ededine beraber deyil')
                
        
list = Metods()
getlist = [2, 5,16,24,32,11, 0, 5, 6,345]
setlist=list.list_creater(getlist)
print(setlist)
list.sumFind(100)  
