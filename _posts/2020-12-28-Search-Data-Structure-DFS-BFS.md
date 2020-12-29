---
title: "DFS 와 BFS 란? 탐색과 자료구조 알고리즘 이해하기 #1"
excerpt: "DFS 와 BFS 를 이해하기 위해서는 탐색과 자료구조 알고리즘을 알아야 한다."

categories:
    - Algorithm
    - Python
tags:
    - Algorithm
    - Python
    - DFS
    - BFS
last_modified_at: 2020-12-28T22:34:00+09:00

---

DFS 와 BFS 알고리즘은 탐색 시 사용하는 알고리즘이다. 탐색(Search)는 다수의 데이터 중에서 원하는 데이터를 찾아내는 과정을 말한다.

프로그램에서는 주로 그래프와 트리 구조에서 탐색문제를 다루게되기 때문에 DFS 와 BFS 알고리즘 문제를 풀려면 자료구조 중에서도 스택과 큐를 기본적으로 이해하고 있어야한다.

그래서 본격적으로 DFS와 BFS를 알기 전에 먼저 자료구조에 대해서 알아본다. 만약, 이미 알고있는 방문자라면 바로 다음 글로 넘어가도 좋다.

**관련 글**
- [DFS 와 BFS 란? 탐색 알고리즘 구현 및 이해하기 #2]({{ site.url }}/algorithm/python/DFS-BFS-알고리즘이란/){: target="_blank"}

## 1. 자료구조(Data Structure)란?
자료구조란 데이터를 표현허고 관리하고 처리하기 위한 구조를 말하며 주로 삽입과 삭제 연산을 주로하게된다.

- 삽입(push): 데이터를 집어 넣는다.
- 삭제(pop): 데이터를 삭제한다.

이때 데이터가 없는 상태에서 삭제연산을 하려고 하면 에러가 발생하는데 이를 언더플로(underflow)라고 한다.

반대로 데이터가 수용 가능한 용량만큼 가득 차 있는데 삽입 연산을 수행하려고 하면 오버플로(overflow)가 발생한다.

### 1.1. 스택(Stack) 이란?

스택은 말 그대로 자료를 쌓아 올린다고 생각하면된다. 택배 상자를 쌓아 올리게되면 맨 먼저 쌓은 박스는 가장 아래에 위치하게 되고, 가장 마지막에 쌓은 상자는 제일 위에 올라가 있게 된다.

그래서 상자를 꺼낼 때는 가장 위에 있는 것 부터 꺼내서 사용해야 하며, 이를 선입후출 또는 후입선출 이라고 한다. 즉, 먼저 넣은 것은 마지막에 뺄 수 있고, 나중에 넣은것은 바로 뺄 수 있다는 뜻이다.

아래 예시 코드를 참고하자.

```python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) # 최상단 원소부터 출력
```

**출력**  

```
[5, 2, 3, 1]
[1, 3, 2, 5]
```

### 1.2. 큐(Queue) 란?

우리가 흔히 알고 있는 대기열을 생각하면된다. 놀이기구를 타려고 줄을 서면 가장 먼저 줄을 선 사람이 먼저 입장하듯 큐도 그렇게 동작한다. 그래서 이 구조는 선입선출구조 라고 한다.

아래 예시 코드를 참고하자.

```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse() # 반대로 뒤집기
print(queue)
```

**출력**

```
deque([3, 7, 1, 4])
deque([4, 1, 7, 3])
```

참고로 python의 deque 라이브러리는 스택과 큐의 장점을 모두 채택하여 사용할 수 있는 라이브러리로 리스트 보다 데이터 삽입 삭제 속도가 빠르다. 물론 기본 라이브러리기 때문에 코딩 테스트에서도 사용가능하다. deque 객체는 `list()` 매서드를 사용해서 리스트로 변환도 가능하다.

### 1.3. 재귀함수란?

재귀 함수란 말 그대로 자기 자신을 호출하는 함수다. 이때 재귀 함수에 종료조건이 명시되어 있지 않으면 무한정 반복하므로 보통 재귀함수를 사용할 때는 종료조건을 명시하여 사용하게된다.

컴퓨터는 내부적으로 함수 처리 시 스택 구조를 사용하는데, 재귀 함수 또한 마찬가지로 스택 구조를 사용해서 수행하게된다. 때문에 스택 자료구조를 사용하는 알고리즘 문제는 대부분 재귀 함수로 편리하게 풀 수 있다. 그 예시가 바로 DFS이다.

아래 코드는 재귀를 이용한 팩토리얼을 구하는 함수 코드 예시이다.

```python
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))
```

재귀를 사용하면 반복문을 사용했을 때 보다 더 간결한 경우가 많은데, 이는 재귀 함수가 수학의 점화식을 그대로 코드화 한것이기 때문이다. 점화식은 특정한 함수를 자기보다 더 작은 변수에 대한 함수와의 관계로 표현한 것을 말한다. 이는 이후 다이나믹 프로그래밍과 연계된다.

**관련 글**
- [DFS 와 BFS 란? 탐색 알고리즘 구현 및 이해하기 #2]({{ site.url }}/algorithm/python/DFS-BFS-알고리즘이란/){: target="_blank"}

**Recommend:**  
- [백준 1003번: 피보나치함수 파이썬 문제풀이 (BOJ 1003)]({{ site.url }}/algorithm/python/BOJ-1003/){: target="_blank"}
- [알고리즘 코딩테스트 자주 쓰는 파이썬 코드 : 입출력]({{ site.url }}/python/algorithm/python-input-output-tips/){: target="_blank"}
- [깃허브(GitHub) 블로그 시작하기 Jekyll로 쉽게 만드는 방법]({{ site.url }}/blog/How-to-Create-a-GitHub-Blog/){: target="_blank"}    
- [구현 알고리즘 기초 문제 : 상하좌우 (파이썬)]({{ site.url }}/algorithm/python/BOJ-5585/){: target="_blank"}
- [그리디 알고리즘 기초 문제 : 1이 될 때까지 (파이썬)]({{ site.url }}/algorithm/python/알고리즘-구현-상하좌우-문제/){: target="_blank"}