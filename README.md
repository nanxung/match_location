# match_location
python实现 nginx 的 location 匹配规则

## 实现的匹配规则
 - 非正则严格匹配 `=`
 - 精准最长前缀匹配 `^~ 或者 /sample/`
 - 正则匹配 `~`
 - 不区分大小写正则匹配 `~*`
 - 匹配所有请求 `/`
 - 优先度排序为   非正则严格匹配  > 精准最长前缀匹配  > 正则匹配  > 不区分大小写正则匹配  > 匹配所有请求  > 未成功匹配 

## 怎么使用代码
 - 打开location.py文件
 - 在match_location(location,rules)函数中 location 为需要匹配的字段 ,rules为需要的匹配的规则数组
