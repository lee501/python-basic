// 初始化树
void Initialize(Tree *t){
  *t = (Tree).malloc(sizeof(treeNode));
  (*t)->IsFile= false;
  strcpy_s((*t)->name, NameSize, "root");
  (*t)->son= NULL;
  (*t)->brother = NULL;
}

// 先序遍历，每一个节点先处理本身，再处理孩子
void PrintPreOrder(Tree t, int layer){
  // 递归一定要有基形
  if(t==NULL)
    return;
  //处理当前节点
  for(int i=0; i<layer; i++)
    putchar('\t'); //根据当前结点在树中的层决定打印多少个制表符
  printf("%s\n", t->name );

  // 处理孩子节点
  Tree temp = t->son;
  // 条件循环语句while
  while(temp!=NULL){
    ++layer;
    PrintPreOrder(temp, layer);
    temp = temp->brother;
  }
}

// 后序遍历，先处理孩子节点，再处理本身
int countSize(Tree t){
  int total = 0;

  if(t==NULL)
    return total;

  //如果t不为NULL则对其下每个孩子进行CountSize，并将返回值加到total上
  Tree son = t->son;
  while(son!=NULL){
    total += countSize(son);
    son = son->brother;
  }

  total += t->size;
  return total; 
} 
