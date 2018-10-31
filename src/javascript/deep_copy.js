var obj = { a:1, arr: [2,3] };
// 浅拷贝实现方式
function shallowCopy(src) {
  var disc = {};
  for(var prop in src){
    if(src.hasOwnProperty(prop)){
      disc[prop] = src[prop];
    }
  }
  return disc;
};

// 判断是否是对象
function isObject(val) {
  return val != null && typeof val === 'object' && Array.isArray(val) === false;
};
// 递归深拷贝
function deepCopy(obj){
  // 确定参数是数组还是对象
  var clone = Array.isArray(obj) ? [] : {};
  if(obj && typeof(obj) === 'object'){
    for(var key in obj){
      if(obj.hasOwnProperty(key)){
        // 判断子元素是否是对象
        if(typeof(obj[key]) === 'object'){
          clone[key] = deepCopy(obj[key]);
        } else {
          clone[key] = obj[key]；
        }
      }
    }
  }
  return clone;
}

// 使用json解析反解析实现深拷贝
b = JSON.parse( JSON.stringify(a) )
