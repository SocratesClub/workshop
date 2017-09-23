import numpy as np
import pylab as pl
import random

#f=open('data.txt','w')
N=1000
nmax=1000
averdegree=999
nx=[0]*N
link=[[0 for i in range(nmax)] for i in range(N)]
conn=[[0 for i in range(N)] for i in range(N)]

addlink=0
numlink=N*averdegree/2.0
while(addlink<numlink):
      rd1=random.random()
      i=int(rd1*N)
      rd2=random.random()
      j=int(rd2*N)
      if(i != j and conn[i][j]==0):
            conn[i][j]=1
            conn[j][i]=1
            addlink += 1

for i in range(N):
      link[i][0]=i
      for j in range(N):
            if(conn[i][j]==1):
                  nx[i] += 1
                  link[i][nx[i]]=j

visit=[0]*N
group=[0]*N
neighbor=[0]*N
neinew=[0]*N
group_label=0
for i in range(N):
      if(group[i]==0):
            group_label += 1
            group[i]=group_label
            visit[i]=1
            l1=0
            for j in range(nx[i]):
                  k1=link[i][j+1]
                  if(visit[k1]==0):
                        l1 += 1
                        neighbor[l1]=k1
                        group[k1]=group_label
                        visit[k1]=1
            nlay=l1
            while(nlay>0):
                  l2=0
                  for j in range(nlay):
                        icu1=neighbor[j]
                        for j1 in range(nx[icu1]):
                              k2=link[icu1][j+1]
                              if(visit[k2]==0):
                                    l2=l2+1
                                    neinew[l2]=k2
                                    group[k2]=group_label
                                    visit[k2]=1
                  nlay=l2
                  for k3 in range(nlay):
                        neighbor[k3]=neinew[k3]

numcluster=group_label
print(numcluster)

