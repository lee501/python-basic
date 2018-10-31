// 二分法查找 数组
int binarySearch(int *a, int n, int target){
  int left = 0;
  int right = n-1;
  int middle = (left + right)/2;

  while(left != right){
    if(a[middle] == target)
      return middle;
    if(a[middle] < target)
      right = middle - 1;
    if(a[middle] > targer)
      left = middle + 1;
    middle = (left + right)/2;
  }
  return -1;
}