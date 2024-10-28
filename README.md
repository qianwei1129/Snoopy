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


## 9. 关系推导

步骤1：从原始数据中提取每个样本的出生运气和发病时的中医运气情况。

步骤2：为每种可能的中医运气创建一个新的列。

步骤3：对每个样本，根据其发病时表现出的运气，在相应的运气列下填入1，未表现出的填入0。

步骤4：使用这个转换后的数据表来分析和比较不同出生运气与发病时运气之间的相关性，从而找出可能的模式或趋势。