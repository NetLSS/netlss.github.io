---
title: "알고리즘 코딩테스트 자주 쓰는 파이썬 코드 : 입출력"
excerpt: "코딩테스트, 알고리즘 문제에서 입출력으로 제공되는 것을 처리할 때 자주 쓰는 파이썬(python) 코드"

categories:
    - Python
    - Algorithm
tags:
    - Algorithm
    - Python
    - Tips
last_modified_at: 2020-12-19T19:29:32+09:00

---

## 1. 코딩 테스트 기본 입출력에 사용되는 python 코드

백준, 온라인 저지, 코딩 테스트에서 입출력 시 자주 쓰는 파이썬(python) 코드를 알아두면 유용합니다.

보통 문제가 주어지면, 입력과 출력 예시가 나오고 이는 정해진 형식이 반복되기 때문에 입출력에 대한 기본적인 코드를 알아두는 것이 중요합니다.

그 중에서 코딩 테스트에서 요새 가장 점유율이 높아지고 있는 프로그래밍 언어인 파이썬(python)에 관련된 코드를 알아보도록 하죠.

## 2. 입력을 위한 전형적인 코드

먼저 입력에 보통 첫 번째 라인으로 테스트 케이스(정수)가 입력되는 경우가 많다. 파이썬 `input()` 함수는 이를 문자열로 반환하기 때문에 `int()` 함수를 사용해서 문자열을 **int형**으로 바꿔주는 것이 필요하다.

그리고 라인 마다 데이터가 정수 여러개를 공백문자를 사용해서 주어진다면 이를또 `input()`으로 받고 공백을 `split()` 함수로 나누어서 각각의 문자열에 `int()` 함수를 사용해서 형변환을 해주면된다.

이때 `int()`함수를 모든 원소에 적용해주는 `map()`을 사용해서 `for 문`없이도 간단하게 형변환을 해줄 수 있다. `map()`함수는 리스트가 아닌 이터레이터를 반환하므로 다시 `list()`로 리스트로 변환해서 사용하면된다. 여기서는 정렬을 사용하기위해 리스트로 변환했다.

아래는 위 내용을 모두 적용한 코드이며, 데이터 개수와 정수를 공백으로 구분지어 입력 받아 해당 정수들을 정렬하는 예시 코드이다.

```python
# 데이터 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

```

**결과 예시**
```
5
65 90 85 73 63 99
[99, 90, 85, 73, 65, 63]
```

### 2.1. 공백을 기준으로 구분해서 적은 수의 데이터 입력

때로는 리스트로 받는 것이 아닌 각각의 변수로 받아야 할 때가 있는데, 예를 들어 n개, 최소값 m, 최대값 k 이런식으로 받아야 할 경우에는 아래와 같은 코드를 사용할 수 있다.

```python
# n, m, k를 공백 구분으로 입력
n, m, k = map(int, input().split())

print(n, m, k)
```

**결과 예시**
```
10 20 80
10 20 80
```

### 2.2. 입력이 많은 경우 sys.stdin.readline()

참고로 C++ 에서는 cin 보다 `scanf()`로 입력 받는 것이 더 빠르다고 한다. 마찬가지로 파이썬에서도 `input()` 은 입력이 많은 경우 시간이 느려질 수 있다.

이때 사용할 수 있는 함수가 바로 `sys.stdin.readline()`이다.

```python
import sys
sys.stdin.readline().rstrip()
```

`readline()`으로 입력 받은 경우 `rstrip()`를 사용해서 개행문자를 제거해서 사용해야한다.

```python
import sys

data = sys.stdin.readline().rstrip()
print(data)
```

**결과 예시**
```
hello oilmlio
hello oilmlio
```

## 3. 출력을 위한 전형적인 코드

파이썬 출력은 기본적으로 print()를 사용한다.

**print() 특징**
1. 출력 하고 자동으로 줄바꿈이 기본적으로 된다.
2. `,`를 사용해서 여러개 출력이 가능하다. 이때 공백(space)으로 구분되어 출력된다.
3. 문자열로 출력시 `+`연산자를 사용하는데 `int`형을 더하면 에러이므로 `str()`로 변환후 해주어야 한다.

가장 좋은 방법은 사실 `fstring`을 사용하는 것인데, 문자열 기호 앞에 `f`를 붙여서 `{}`로 안에 변수명을 넣어주면 형변환을 자동으로 해준다.

```python
a = 1234
print(f"비밀번호는 {a}")
```

**출력**
```비밀번호는 1234```

> cf. 이것이 취업을 위한 코딩 테스트다 with 파이썬

**Recommend:**  
- [백준 5585번: 거스름돈 파이썬 문제풀이 (BOJ 5585)]({{ site.url }}/algorithm/python/BOJ-5585/){: target="_blank"}
- [백준 1003번: 피보나치함수 파이썬 문제풀이 (BOJ 1003)]({{ site.url }}/algorithm/python/BOJ-1003/){: target="_blank"}
- [깃허브(GitHub) 블로그 시작하기 Jekyll로 쉽게 만드는 방법]({{ site.url }}/blog/How-to-Create-a-GitHub-Blog/){: target="_blank"}    