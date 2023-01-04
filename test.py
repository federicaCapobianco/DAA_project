from time import time
from pos_tagging import pos_tag
from DeviceSelection import DeviceSelection


#Testing pos_tagging
R=('Noun', 'Modal', 'Verb')
S=('Will', 'Mary', 'Spot', 'Jane')
T=dict()
T['Start']={'Noun': 3/4, 'Modal': 1/4, 'Verb': 0, 'End': 0}
T['Noun']={'Noun': 1/9, 'Modal': 3/9, 'Verb': 1/9, 'End': 4/9}
T['Modal']={'Noun': 1/4, 'Modal': 0, 'Verb': 3/4, 'End': 0}
T['Verb']={'Noun': 1, 'Modal': 0, 'Verb': 0, 'End': 0}
E=dict()
E['Will']={'Noun': 1/4, 'Modal': 3/4, 'Verb': 0}
E['Mary']={'Noun': 1, 'Modal': 0, 'Verb': 0}
E['Spot']={'Noun': 1/2, 'Modal': 0, 'Verb': 1/2}
E['Jane']={'Noun': 1, 'Modal': 0, 'Verb': 0}
out={'Will': 'Modal', 'Mary': 'Noun', 'Spot': 'Verb', 'Jane': 'Noun'}

start = time()
sol = pos_tag(R, S, T, E)
end = time()-start

if sol != out:
    print('FAIL')
else:
    print('True')
    print(end)

#Testing DeviceSelection
N = ('Device 1', 'Device 2', 'Device 3', 'Device 4', 'Device 5')
X = 7
data = {'Device 1': (100, 99, 85, 77, 63), 'Device 2': (101, 88, 82, 75, 60), 'Device 3': (98, 89, 84, 76, 61), 'Device 4': (110, 65, 65, 67, 80), 'Device 5': (95, 80, 80, 63, 60)}
partition = [['Device 1', 'Device 3', 'Device 5'], ['Device 2'], ['Device 4']]

start = time()
ds=DeviceSelection(N, X, data)
C=ds.countDevices()
subsets = [[] for i in range(C)]
for i in range(C):
    dev = ds.nextDevice(i)
    while dev is not None:
        subsets[i].append(dev)
        dev = ds.nextDevice(i)
end=time()-start

if sorted(subsets) != sorted(partition):
    print('FAIL')
else:
    print('True')
    print(end)
