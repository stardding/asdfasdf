import sys,math
from collections import deque

for _ in range(int(sys.stdin.readline())):
	n,m=map(int,sys.stdin.readline().split())
	inp=[]
	ch=False
	for i in range(n):
		inp.append(list(map(int,sys.stdin.readline().split())))		#입력
	total=sum([sum(i) for i in inp])
	gragh=[dict() for i in range(n*m+2)]
	for i in range(n):							#그래프 초기화
		for j in range(m):
			if ch:
				gragh[n*m][i*m+j]=inp[i][j]			#격자 연결
			else:
				gragh[i*m+j][n*m+1]=inp[i][j]
			ch=not ch

			if j%m!=0:						#인접 노드 연결
				gragh[i*m+j][i*m+j-1]=math.inf
			if j%m!=m-1:
				gragh[i*m+j][i*m+j+1]=math.inf
			if i>0:
				gragh[i*m+j][(i-1)*m+j]=math.inf
			if i<n-1:
				gragh[i*m+j][(i+1)*m+j]=math.inf

		if m%2==0:
			ch=not ch
	
	flow=[[0 for i in range(n*m+2)] for j in range(n*m+2)]			#에드몬드-카프
	res=0
	while True:
		q=deque([n*m])
		parent=[-1 for i in range(n*m+2)]
		parent[n*m]=n*m
		while q:
			now=q.popleft()
			for nex,capacity in gragh[now].items():
				if parent[nex]==-1 and capacity-flow[now][nex]>0:
					q.append(nex)
					parent[nex]=now

		if parent[n*m+1]==-1:
			break

		t=n*m+1
		wave=math.inf
		while t!=n*m:
			wave=min(wave,gragh[parent[t]][t]-flow[parent[t]][t])
			t=parent[t]
		res+=wave
		t=n*m+1
		while t!=n*m:
			flow[parent[t]][t]+=wave
			flow[t][parent[t]]-=wave
			t=parent[t]
	print(total-res)							#결과 출력
