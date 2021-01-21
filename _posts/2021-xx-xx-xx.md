---
title: "정렬 알고리즘 문제 : 두 배열의 원소 교체 (python)"
excerpt: "알고리즘 정렬 문제 두 배열의 원소를 교체하여 최대로 만드는 프로그램을 파이썬으로 작성해본다."

categories:
    - Algorithm
    - Python
tags:
    - Algorithm
    - Python
    - Sort
last_modified_at: 2021-01-21T21:36:00+09:00

---

두개의 배열 A, B 가 있고 각 배열은 N개의 원소로 구성되며 원소는 모두 자연수로 이루어진다. 이때 바꾸기 연산을 최대 K 번 수행할 수 있고 바꾸기 연산이란 A에 있는 원소 하나를 B에 있는 원소 하나와 바꾸는 것을 말한다. 우리의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 만들면된다.

N, K 그리고 배열 A, B의 정보가 주어지고, 최대 K 번 바꾸기 연산이 가능할 때 가장 최대의 합을 가지는 A릐 모든 원소의 합의 최대값을 출력하는 프로그램을 작성하시오.

## 입력 조건
- 첫 번째 줄: N, K 가 공백으로 구분되어 입력 (`1 <= N <= 100,000`, `0 <= K <= N`)
- 두 번째 줄: 배열 A의 원소들이 공백으로 구분되어 입력 (원소 `a < 10,000,000`인 자연수)
- 세 번째 줄: 배열 B의 원소들이 공백으로 구분되어 입력 (원소 `b < 10,000,000`인 자연수)


## 출력 조건
- 최대 K번 바꿔치기 연산을 수행해서 가장 최대의 합을 갖는 A의 모든 원소 값의 합을 출력


**입력 예시**
```python
5 3
1 2 5 4 3
5 5 6 6 5
```

**출력 예시**
```python
26
```

## 내가 작성한 코드

```python
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a)
print(b)

a.sort()
b.sort(reverse=True)

for i in range(k):
    a[i], b[i] = b[i], a[i]

print(sum(a))

```

정답이라고 확신하고 작성한 코드다. 책에 있는 답과 거의 유사했지만, 한 부분을 놓친 것을 깨달았다. 무조건 적으로 swap을 하면 안되고, b값이 클 경우에만 바꾸어야 우리가 원하는 최대의 합을 가지는 배열을 만들 수 있다는 점이 간과되었다. 아래는 수정한 코드이다.

## 바르게 수정된 답안 코드

```python
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(a)
print(b)

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
```

참고로 a의 원소와 b의 원소를 비교할 때 b의 원소가 a 보다 작아진 경우 `break` 하는데 이는 a와 b가 모두 정렬된 상태이기 때문에 이후 값은 전부 볼 필요가 없어져서 그렇다.

이때 최대 원소가 100,000개 까지 입력될 수 있으므로 O(NlogN)을 보장할 수 있는 정렬알고리즘을 사용했다.

> 이것이 취업을 위한 코딩 테스트다 with 파이썬

**Recommend:**  
- [선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬 한번에 알고가기 (With 파이썬)]({{site.url}}/algorithm/python/Sort-algorithm/){: target="_blank"}
- [파이썬 정렬 라이브러리 sort, sorted]({{site.url}}/python/algorithm/python-sort-sorted-example/){: target="_blank"}
- [정렬 알고리즘 문제 : 위에서 아래로 (python)]({{site.url}}/algorithm/python/up-down/){:target="_blank"}
- [정렬 알고리즘 문제 : 성적이 낮은 순서로 학생 출력하기 (python)]({{site.url}}/algorithm/python/score-sort/){:target="_blank"}