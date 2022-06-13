trajectories = []
#p1 =790 300 p2=360 470
N=4
print("\tself.nPoints =",N)
print("\tself.seq =",N)
print("\tself.trajectories=[ #p1 =790 300 p2=360 470")
for i in range(0,15):
    trajectory = []
    #for j in range(0,4):
    #    trajectory.append([360+410*(j%2), 300+150*((j-1)%2)])
    trajectory.append([400, 400])
    trajectory.append([600, 400])
    #trajectory.append([740, 410])
    #trajectory.append([740, 340])
    print("\t",trajectory,",#",i)
    trajectories.append(trajectory)
print("\t]")
