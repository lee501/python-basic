// 二叉树结构
typeof struct BinaryTreeNode
{
  int data;
  int frequency; //当插入数据与当前结点相同时+1，当删除当前结点时-1
  struct BinaryTreeNode *left;
  struct BinaryTreeNode *right;
}BinaryTreeNode;

typedef BinaryTreeNode *BinaryTree;

//二分查找应用于二叉查找树
bool searchByTree(BinaryTree t, int data)
{
  if(t == NULL)
    return false;
  if(t->data == data&&t->frequency > 0)
    return true;
  if(t->data<data)
    return searchByTree(t->right, data);
  if(t->data > data)
    return searchByTree(t->left, data);

  return false;
}

// 二叉树插入节点
BinaryTree insert(BinaryTree tree, int data)
{
  if(tree == NULL)
  {
    BinaryTree temp = (BinaryTree)malloc(sizeof(BinaryTreeNode));
    temp->data = data;
    temp->frequency = 1;
    temp->left = temp->right = NULL;
    return temp;
  }
  if(tree->data > data)
    tree->left = insert(tree->left, data);
  if(tree->data <  data)
    tree->right = insert(tree-right, data);
  else
    tree->frequency += 1;
  return tree;
}
