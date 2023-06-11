import sys

n=int(sys.stdin.readline())
ix=[];iy=[];iw=[]
for i in range(n):
	x,y,w=map(int,sys.stdin.readline().split())
	ix.append(x)
	iy.append(y)
	iw.append(w)

nx=len(set(ix));ny=len(set(iy))								# 좌표 압축
tx=dict(zip(sorted(list(set(ix))),[i for i in range(nx)]))
ty=dict(zip(sorted(list(set(iy))),[i for i in range(ny)]))

gold={}
for x,y,w in zip(ix,iy,iw):
	if tx[x] in gold.keys():
		gold[tx[x]].append((ty[y],w))
	else:
		gold[tx[x]]=[(ty[y],w)]

def update(t,v,node,l,r):									# 세그먼트 트리 업데이트
	if t<l or r<t:
		return stree[node]
	elif l==r:
		for i in range(4):
			stree[node][i]+=v
		return stree[node]
	mid=l+r>>1
	lv=update(t,v,node<<1,l,mid)
	rv=update(t,v,node<<1|1,mid+1,r)
	stree[node][0]=lv[0]+rv[0]
	stree[node][1]=max(lv[1],rv[1],lv[3]+rv[2])
	stree[node][2]=max(lv[2],lv[0]+rv[2])
	stree[node][3]=max(rv[3],rv[0]+lv[3])
	return stree[node]

m=0
for x1 in range(nx):
	stree=[[0,0,0,0] for i in range(ny<<2)]				 	# 0:all, 1:mid sum, 2:left sum, 3:right sum
	for x2 in range(x1,nx):
		for y,w in gold[x2]:
			update(y,w,1,0,ny-1)
		m=max(m,stree[1][1])

print(m)
