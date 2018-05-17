#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct tree
{
	int data;
	struct tree * lchild;
	struct tree * rchild;
}*PTreeNode;

PTreeNode find(int x, PTreeNode tree)
{
	if (NULL == tree)
		return NULL;
	if (x == tree->data)
		return tree;
	else if (x > tree->data)
		return find(x, tree->rchild);
	else if (x < tree->data)
		return find(x, tree->lchild);
}

PTreeNode findMin(PTreeNode tree)
{
	if (tree == NULL)
		return NULL;
	while(tree->lchild)
		tree = tree->lchild;
	return tree;
}

int findMax(PTreeNode tree)
{
	if (tree == NULL)
		return -1;
	else if (tree->rchild == NULL)
		return tree->data;
	else 
		return findMax(tree->rchild);
}

PTreeNode insert(int x, PTreeNode tree)
{
	if (NULL == tree)
	{
		PTreeNode tmp = (PTreeNode)malloc(sizeof(struct tree));
		if (NULL == tmp)
		{
			printf("alloc memory failed\n");
			return NULL;
		}
		tmp->data = x;
		tmp->lchild = tmp->rchild = NULL;
		tree = tmp;
		return tree;
	}
	else if (x < tree->data)
		tree->lchild = insert(x, tree->lchild);
	else if (x > tree->data)
		tree->rchild = insert(x, tree->rchild);
	else if (x == tree->data)
		printf("the tree has the %d, cannot be inserted\n", x);
	return tree;
}


void printpre(PTreeNode tree)
{
	if (NULL != tree)
	{
		printf("%d ", tree->data);
		printpre(tree->lchild);
		printpre(tree->rchild);
	}
}

int getDepthTree(PTreeNode tree)
{
	int ldepth = 0;
	int rdepth = 0;
	if (NULL == tree)
		return -1;
	else if (NULL != tree->lchild)
	{
		ldepth += 1;
		getDepthTree(tree->lchild);
	}
	else if (NULL != tree->rchild)
	{
		rdepth += 1;
		getDepthTree(tree->rchild);
	}

	return (ldepth > rdepth)?ldepth:rdepth;
}

int maxDepth(PTreeNode root) 
{  
	if(root == NULL)  
		return 0;  
	else if(root->lchild == NULL && root->rchild == NULL)  
		return 1;  
	else  
		{  
			int leftDepth= maxDepth(root->lchild);  
			int rightDepth = maxDepth(root->rchild);  
			if(leftDepth > rightDepth)  
				return leftDepth +1;  
			else  
				return rightDepth +1;  
		}  
         
}  

PTreeNode deleteTreeNode(PTreeNode tree, int data)
{
	PTreeNode tmpCell;
	if (NULL == tree)
		return NULL;
	else if (data < tree->data)
		tree->lchild = deleteTreeNode(tree->lchild, data);
	else if (data > tree->data)
		tree->rchild = deleteTreeNode(tree->rchild, data);
	else if (tree->lchild && tree->rchild)
	{
		tmpCell = findMin(tree->rchild);
		tree->data = tmpCell->data;
		tree->rchild = deleteTreeNode(tree->rchild, tree->data);
	}
	else
	{
		tmpCell = tree;
		if (tree->lchild == NULL)
			tree = tree->rchild;
		else if (tree->rchild == NULL)
			tree = tree->lchild;
		free(tmpCell);
	}
	return tree;
}

int main()
{
	int a = 12;
	static int data[] = {12,3, 24};
	int count = sizeof(data)/sizeof(data[0]);
	PTreeNode mnode = NULL;
	int i = 0;
	for (i = 0; i < count; i++)
	{
		mnode = insert(data[i], mnode);
	}

	int num = findMax(mnode);
	printf("num = %d\n", num);

	PTreeNode MYTEST = findMin(mnode);
	printf("PTreeNode->data = %d\n", MYTEST->data);
	printpre(mnode);
	int det = maxDepth(mnode);
	printf("det = %d\n", det);
	PTreeNode TEST = deleteTreeNode(mnode, 3);
	return 0;
}