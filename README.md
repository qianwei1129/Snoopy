# 赛博算命3.0-五运六气

- [Snoopy使用方法](#使用方法)
  - [函数解释](#函数解释)
  - 
### 函数解释

### `calculate(year, month, day)`

主体分为以下三个部分
- [calculate_qi.py](./calculate_qi.py)
- [calculate_yun.pt](./calculate_yun.py)
- [calculate_relationship.py](./calculate_relationship.py)

#### `calculate_qi.py`
```python
from calculate_qi import get_qi
get_qi(year, 
       month, 
       day, 
       start="lichun") 
```
此函数用于计算给定日期的主气和客气，形参有：
- `year`: 必需形参，给定日期的年
- `month`: 必需形参，给定日期的月
- `day`: 必需形参，给定日期的日
- `start`: 可选形参，计算时以什么节气作为开始的节点，可选形参有`dahan`和`lichun`，默认为`lichun`

返回值包括：
- `main_qi`: 指定日期的主气
- `guest_qi`: 指定日期的客气
- `ji_zhi_qi`: 几之气
- `si_tian_zhi_qi`: 司天之气
- `zai_tian_zhi_quan`: 在天之泉

#### `calculate_yun.py`
```python
from calculate_yun import get_yun
get_yun(year, 
       month, 
       day,
       suiyun,
       start="lichun") 
```
用于计算给定日期的主运和客运，形参有：
- `year`: 必需形参，给定日期的年
- `month`: 必需形参，给定日期的月
- `day`: 必需形参，给定日期的日
- `start`: 可选形参，计算时以什么节气作为开始的节点，可选形参有`dahan`和`lichun`，默认为`lichun`

返回值包括：
- `main_yun`: 指定日期的主运
- `guest_yun`: 指定日期的客运
- `ji_zhi_yun`: 几之运

#### `calculate_relationship`
 
用于计算给定日期的主气和客气的关系

```python
from calculate_relationship import determine_relation
determine_relation(main_qi, guest_qi)
```
此函数会返回指定日期的主气、客气的关系，形参有：
- `main_qi`: 指定日期的主气
- `guest_qi`: 指定日期的客气

返回值包括：
- `relation`: 一个列表两个值，第一个为相得/不相得，第二个为顺/逆