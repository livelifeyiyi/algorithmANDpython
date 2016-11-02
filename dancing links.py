//处理行
Build:
	// 初始化head节点
	head = {left: head, right: head, up: head, down: head, x: 0, y: 0}
	// 初始化列头节点
	columnHead = []
	pre = head // 表示前一个节点
	For i = 1 .. m
		p = columnHead[i]
		// 上下指针指向自己
		p.up = p, p.down = p
		// 记录坐标
		p.x = 0, p.y = i
		// 向横向的双向列表中添加一个元素
		p.right = pre.right
		p.left = pre
		pre.right.left = p
		pre.right = p
		// 更新pre为当前节点
		pre = p
	End For
	// 给节点编号，并初始化每个节点
	cnt = 0
	node = []
	For i = 1 .. n
		For j = 1 .. m
			If (board[i][j] == 1) Then
				cnt = cnt + 1
				id[i][j] = cnt
				node[cnt] = {
					left: node[cnt], right: node[cnt], 
					up: node[cnt], down: node[cnt],
					x: i, y: j
				}
			End If  
		End For
	End For
	// 纵向添加节点
	For j = 1 .. m
		pre = columnHead[j]
		For i = 1 .. n
			If (board[i][j] == 1) Then
				p = node[ id[i][j] ];
				p.down = pre.down
				p.up = pre
				pre.down.up = p
				pre.down = p
				pre = p
			End If
		End For
	End For
	// 横向添加节点
	For i = 1 .. n
		pre = NULL	// 横向没有头结点
		For j = 1 .. m
			If (board[i][j] == 1) Then
				If (pre == NULL) Then
					// 将扫描到的第一个节点作为头结点
					pre = node[ id[i][j] ]
				Else
					p = node[ id[i][j] ]
					p.right = pre.right
					p.left = pre
					pre.right.left = p
					pre.right = p
					pre = p
				End If
			End If
		End For
	End For

remove(col):	// 删除第col列
	p = columnHead[col]
	p.right.left = p.left
	p.left.right = p.right
	p2 = p.down
	While (p2 != p) 
		// 获取该列下的每一个节点p2
		p3 = p2.right 
		While (p3 != p2)
			// 获取节点p2所在行的其他节点p3
			p3.down.up = p3.up
			p3.up.down = p3.down
			p3 = p3.right
		End While
		p2 = p2.down
	End While


resume(col):	// 恢复第col列
	p = columnHead[col]
	p.right.left = p
	p.left.right = p
	p2 = p.down
	While (p2 != p) 
		// 获取该列下的每一个节点p2
		p3 = p2.right 
		While (p3 != p2)
			// 获取节点p2所在行的其他节点p3
			p3.down.up = p3
			p3.up.down = p3
			p3 = p3.right
		End While
		p2 = p2.down
	End While



dance(depth):
	p = head.right
	If (p == head) Then
		// 若head的右边就是head自己，则已经找到解
		Return True;
	End If
	p2 = p.down
	If (p2 == p) Then
		// 当前列没有节点，则当前列一定不会被覆盖
		Return false
	End If 
	
	remove(p.y) // 删除当前列
	While (p2 != p) 
		// 枚举选取每一个节点
		ans[ depth ] = p2.x	// 将行压入答案栈中
		
		// 删除p2所在行的其他列
		p3 = p2.right
		While (p3 != p2)
			remove(p3.y)
			p3 = p3.right
		End While
		
		// 递归下一步
		If (dance(depth + 1)) Then
			Return True
		End If
		
		// 恢复p2所在行的其他列
		p3 = p2.left // 这个地方需要反向来做
		While (p3 != p2)
			resume(p3.y)
			p3 = p3.left
		End While
		
		// 	枚举下一个节点
		p2 = p2.down
	End While
	resume(p.y) // 恢复当前列
	Return False