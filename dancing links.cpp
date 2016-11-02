#include <string>
#include <iostream>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
#include <set>

#define dbg(x) cout << #x << ": " << x << endl
#define zero(x) (x >= - EPSINON) && (x <= EPSINON)
using namespace std;

class Node {
public:
  Node* left;Node* right;Node* down;Node* up;
  int x, y;
  Node() {setProperties(0,0,0,0,0,0);}
  Node(Node* l, Node* r, Node* u, Node* d, int xx, int yy) {setProperties(l,r,u,d,xx,yy);}
  void setProperties(Node* l, Node* r, Node* u, Node* d, int xx, int yy) {
      left=l;right=r;down=d;up=u;x=xx;y=yy;
  }
};

#define MAX_M 102
#define MAX_N 102
Node* columnHead[MAX_M];
Node* node[MAX_M*MAX_N];
int board[MAX_N][MAX_M];
int id[MAX_N][MAX_M];
int ans[MAX_M];
int t,n,m;
Node* head;

void build() {
    int logCount = 0;
// 	printf("build %d\n", logCount++);
    if (!head) head = new Node();
	head->setProperties(head,head,head,head,0,0);
	
// 	printf("build %d\n", logCount++);
	
	Node* pre = head;
	Node* p;
	for(int i = 1;i<=m;i++) {
		if (!columnHead[i]) columnHead[i] = new Node();
		p = columnHead[i];
		p->up = p;
		p->down = p;
		
		p->x = 0;
		p->y = i;
		
		p->right = pre->right;
		p->left = pre;
		pre->right->left = p;
		pre->right = p;
		
		pre = p;
	}
// 	printf("build %d\n", logCount++);
	int cnt = 0;
	for(int i = 1;i<=n;i++) {
		for(int j = 1;j<=m;j++) {
			if (board[i][j] == 1){
				cnt = cnt + 1;
				id[i][j] = cnt;
				if (!node[cnt]) node[cnt] = new Node();
				node[cnt]->setProperties(node[cnt],node[cnt],node[cnt],node[cnt],i,j);
			}  
		}
	}
// 	printf("build %d\n", logCount++);
	for(int j = 1;j<=m;j++) {
		pre = columnHead[j];
		for (int i = 1;i<=n;i++) {
			if (board[i][j] == 1) {
				p = node[ id[i][j] ];
				p->down = pre->down;
				p->up = pre;
				pre->down->up = p;
				pre->down = p;
				pre = p;
			}
		}
	}
// 	printf("build %d\n", logCount++);
	for(int i = 1;i<=n;i++) {
	    pre = NULL;
		for(int j = 1;j<=m;j++) {
			if (board[i][j] == 1) {
				if (pre == NULL) {
					pre = node[ id[i][j] ];
				} else {
					p = node[ id[i][j] ];
					p->right = pre->right;
					p->left = pre;
					pre->right->left = p;
					pre->right = p;
					pre = p;
				}
			}
		}
	}
// 	printf("build %d\n", logCount++);
}

void remove(int col) {
    // printf("remove %d\n", col);
	Node* p = columnHead[col];
	p->right->left = p->left;
	p->left->right = p->right;
	Node* p2 = p->down;
	Node* p3 = NULL;
	while (p2 != p) {
		p3 = p2->right;
		while (p3 != p2) {
			p3->down->up = p3->up;
			p3->up->down = p3->down;
			p3 = p3->right;
		}
		p2 = p2->down;
	}
// 	printf("remove %d finish\n", col);
}

void resume(int col) {
	Node* p = columnHead[col];
	p->right->left = p;
	p->left->right = p;
	Node* p2 = p->down;
	Node* p3 = NULL;
	while (p2 != p) {
		p3 = p2->right;
		while (p3 != p2) {
			p3->down->up = p3;
			p3->up->down = p3;
			p3 = p3->right;
		}
		p2 = p2->down;
	}
// 	printf("resume %d finish\n", col);
}

bool dance(int depth) {
	Node* p = head->right;
	if (p == head) {
		return true;
	}
	Node* p2 = p->down;
	if (p2 == p) {
		return false;
	}
	
	remove(p->y);
	Node* p3 = NULL;
	while (p2 != p) {
		ans[ depth ] = p2->x;
		
		p3 = p2->right;
		while (p3 != p2) {
			remove(p3->y);
			p3 = p3->right;
		}
		
		// 递归下一步
		if (dance(depth + 1)) {
			return true;
		}
		
		p3 = p2->left;
		while (p3 != p2) {
			resume(p3->y);
			p3 = p3->left;
		}
		
		p2 = p2->down;
	}
	resume(p->y);
	return false;
}

void solve() {
//     n=4;m=4;
// board[1][1]=1;board[1][2]=0;board[1][3]=1;board[1][4]=0;
// board[2][1]=0;board[2][2]=1;board[2][3]=0;board[2][4]=0;
// board[3][1]=1;board[3][2]=0;board[3][3]=0;board[3][4]=0;
// board[4][1]=0;board[4][2]=0;board[4][3]=1;board[4][4]=1;
//         build();
//         if (dance(1)) printf("Yes\n");
//         else printf("No\n");
    scanf("%d",&t);
    for(int i=1;i<=t;i++) {
        scanf("%d %d", &n,&m);
        for(int j=1;j<=n;j++) {
            for(int k=1;k<=m;k++) {
                scanf("%d", &board[j][k]);
            }
        }
        build();
        if (dance(1)) printf("Yes\n");
        else printf("No\n");
    }
}

int main() {
    solve();
    return 0;
}