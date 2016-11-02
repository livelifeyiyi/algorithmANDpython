
class solution1(object):
	
	def getsum(map):
	    sum = 0
	    for i in range(1, citinum+1):
	        for j in range(i+1, citinum+1):
	            if map[i-1][j-1] != 0:
	                sum +=  map[i-1][j-1]
	            else:
	                sum = DFS(i-1,j-1,sum)
	    return sum
	def DFS(i,j,sum):
	    for t in range(0,citinum): 
	        if t > i and map[i][t] != 0 and visited[i][t] == 0:
	            visited[i][t] = 1
	            p = t
	            break
	    if map[p][j] != 0:
	        sum = sum + map[i][p] + map[p][j]
	        return sum
	    else: 
	        #visited = [0 for i in range(citinum)]
	        sum += DFS(p,j,sum)


	(n,m) = (int(x) for x in raw_input().split(" "))
	citinum = n
	map = [[0 for i in range(n)] for i in range(n)]
	visited = [[0 for i in range(n)] for i in range(n)]
	query = []
	while(n-1 > 0):
	    n -= 1
	    (u,v,k) = (int(x) for x in raw_input().split(" "))
	    map[u-1][v-1] = map[v-1][u-1] = k 

	while (m > 0):
	    m -= 1
	    string = raw_input()
	    if string == "QUERY":
	        query.append(getsum(map))
	        continue
	    else:
	        (edit,u,v,k) = string.split(" ")
	        (u,v,k) = (int(u),int(v),int(k))
	        map[u-1][v-1] = map[v-1][u-1] = k
	        visited = [[0 for i in range(citinum)] for i in range(citinum)]
	        continue
	    
	for i in query:
	    print i    