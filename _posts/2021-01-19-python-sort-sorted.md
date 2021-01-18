---
title: " "
excerpt: " "

categories:
    - Python
    - Algorithm
tags:
    - Algorithm
    - Python
    - BFS
last_modified_at: 2021-01-19T21:24:00+09:00

---

## 1. 파이썬 정렬 sorted(), sort()

파이썬 기본 정렬 라이브러리에는 sort()와 sorted()가 있다. 내부적으로는 퀵과 비슷한 병합 정렬을 채택했다고한다. 시간 복잡도는 최악의 경우에도 O(NlogN)를 보장하게 구현되어있다.


### 1.1. 에제 코드 1

**코드**
```python
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

```

**출력**
```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 1.2. 예제 코드 2

**코드**
```python
array = [7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

```

**출력**
```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 1.3. 예제 코드 3

**코드**
```python
array = [('바나나', 2), ('사과',5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

```

**출력**
```python
[('바나나', 2), ('당근', 3), ('사과', 5)]
```
  
  
**Recommend:**  
- [알고리즘 코딩테스트 자주 쓰는 파이썬 코드 : 입출력]({{ site.url }}/python/algorithm/python-input-output-tips/){: target="_blank"}