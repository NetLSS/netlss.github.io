---
title: "정렬 알고리즘 문제 : 성적이 낮은 순서로 학생 학생 출력하기 (python)"
excerpt: "파이썬 라이브러리를 사용해서 풀어보는 정렬 알고리즘 문제 풀이 두 번째"

categories:
    - Algorithm
    - Python
tags:
    - Algorithm
    - Python
    - Sort
last_modified_at: 2021-01-20T22:22:00+09:00

---

## 문제 설명

N명의 학생의 성적 정보가 주어진다. 형식은 `이름 성적` 으로 주어지는데 이때 이들의 성적이 낮은 순으로 학생 이름을 출력하는 문제다.

### 입력 조건

- 첫 번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
- 두 번째 줄 부터 N+1 번째 줄 까지 학생의 이름 그리고 성적이 공백으로 주어진다. 학생이름 길이는 100이하, 성적은 100이하 자연수로 주어진다.

### 출력 조건
- 모든 학생의 이름을 성적이 낮은 순으로 출력하면된다. 동일한 성적은 자유롭게 출력하면된다.

#### 입력 예시

```python
2
홍길동 96
이순신 78
```

### 출력 예시

```python
이순신 홍길동
```

## 정답 구현 코드

```python
n = int(input())

arr = []
for i in range(n):
    tup = input().split()
    arr.append((tup[0], int(tup[1])))

arr.sort(key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')
```

100,000개 데이터가 입력되는 경우 이므로 O(NlogN) 또는 O(N)을 보장하는 계수 정렬을 사용하면된다. 위 코드에서는 파이썬 기본 정렬 라이브러리를 사용해서 정렬했다. 파이썬 람다 기능을 사용해서 정렬후 출력했다.

**Recommend:**  
- [선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬 한번에 알고가기 (With 파이썬)]({{site.url}}/algorithm/python/Sort-algorithm/){: target="_blank"}
- [파이썬 정렬 라이브러리 sort, sorted]({{site.url}}/python/algorithm/python-sort-sorted-example/){: target="_blank"}
- [정렬 알고리즘 문제 : 위에서 아래로 (python)]({{site.url}}/algorithm/python/up-down/){:target="_blank"}