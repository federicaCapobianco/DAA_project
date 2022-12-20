#make a class named DeviceSelection
class DeviceSelection:
    slots = ('N', 'X', 'data', 'count', 'subsets', 'index', 'current', 'done')
    def __init__(self, N, X, data):
        self.N=N
        self.X=X
        self.data=data
        self.N.sort(key=lambda x: sum(self.data[x]), reverse=True)
        self.data={k: sorted(v, reverse=True) for k, v in self.data.items()}
        self.count=0
        self.subsets=[[] for i in range(self.countDevices())]
        self.index=[0 for i in range(self.countDevices())]
        self.current=0
        self.done=False
    def countDevices(self):
        self.count=0
        for i in range(len(self.N)):
            if sum(self.data[self.N[i]])>=self.X:
                self.count+=1
        return self.count
    def nextDevice(self, i):
        if self.done:
            return None
        if i==self.current:
            if self.index[i]==len(self.N):
                self.current+=1
                if self.current==self.count:
                    self.done=True
                return self.nextDevice(self.current)
            else:
                if sum(self.data[self.N[self.index[i]]])>=self.X:
                    self.subsets[i].append(self.N[self.index[i]])
                    self.index[i]+=1
                    return self.subsets[i][-1]
                else:
                    self.index[i]+=1
                    return self.nextDevice(i)
        else:
            return self.nextDevice(self.current)
    def getSubsets(self):
        return self.subsets
        