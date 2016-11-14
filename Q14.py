import Array_queue

def buyshare(x,xrate,q,d):
	d[x]=xrate
	q.enqueue(x)

def sellshare(y,yrate,q,d):
	s=0
	l1=[]
	l2=[]
	j=0
	k=0
	y1=y
	for i in range(q.len()):
	#running the loop as long as we dont get the required shares to sell
		if s!=y:
			if q.first()<=y1:
				j=q.dequeue()
				y1 -=j
				s +=j
				l1.append(j)
				l2.append(d[j])
				del d[j]
			else:
				k=q.dequeue()
				j=y1
				d[k-j]=d[k]
				y1=0
				q.enqueue(k-j)
				l1.append(j)
				l2.append(d[k])
				del d[k]
	if i==q.len()-1 and s!=y:
		print("Insufficient shares to sell")
		return -1
	sellprice=0
	for i in range(len(l1)):
		sellprice += l1[i]*(yrate-l2[i])
		print(sellprice)

	if sellprice>0:
		print("Capital Profit=",sellprice)
	elif sellprice>0:
		print("Capital Loss=",sellprice)
	else:
		print("No gain")

q=Array_queue.ArrayQueue()
d={}
buyshare(100,20,q,d)
buyshare(20,24,q,d)
buyshare(200,36,q,d)
sellshare(150,30,q,d)