# 赛博算命3.0-五运六气

- [Snoopy使用方法](#使用方法)

- [五运六气计算法](#五运六气计算方法)

***胡屹莹：沈天威觉得世界上的人都是傻逼，包括他自己***

## 使用方法

## 调用方法

### `calculate(year, month, day)`
返回值包括：
- 主气
- 客气
- 几之气 
- 主运
- 客运
- 几之运 
- 司天之气
- 在泉之气

主体分为以下三个部分
- [calculate_qi.py](./calculate_qi.py)
- [calculate_yun.pt](./calculate_yun.py)
- [calculate_relationship.py](./calculate_relationship.py)

### `calculate_qi.py`

用于计算给定日期的主气和客气，start是以什么节气作为节点，可选择的有大寒和立春，默认为立春 
```python
from calculate_qi import get_qi
get_qi(year, # 给定日期的年
       month, # 给定日期的月
       day, # 给定日期的日
       start="lichun") 
```
此函数会返回指定日期的主气、客气、几之气、司天之气和在天之气

### `calculate_yun.py`
 
用于计算给定日期的主运和客运，start是以什么节气作为节点，可选择的有大寒和立春，默认为立春
```python
from calculate_qi import get_qi
get_qi(year, # 给定日期的年
       month, # 给定日期的月
       day, # 给定日期的日
       start="lichun") 
```
此函数会返回指定日期的主气、客气、几之气、司天之气和在天之气

### `calculate_relationship`
 
用于计算给定日期的主气和客气的关系
```python
from calculate_relationship import determine_relation
determine_relation(main_qi, guest_qi)
```
此函数会返回指定日期的主气、客气的关系



## 小备注：总是无法push到github的方法

### 取消原代理设置

```cmd
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### 刷新 DNS 解析缓存

```cmd
ipconfig /flushdns
```

### 重新设置代理

```cmd
git config --global https.proxy http://127.0.0.1:7890
git config --global https.proxy https://127.0.0.1:7890
```

其中的7890来自于网络与Internet代理设置里面的本机端口号