# Repository 설명
라벨링한 결과물을 저장하고 날짜를 선택해서 그동안 저장된 결과물을 함께 학습시킵니다. 그리고 학습시킨 가중치를 날짜별로 저장해두는 저장소입니다. 

## Rules
### 라벨링(labeling) 관련
- 라벨링은 [**tzutalin/labelImg**](https://github.com/tzutalin/labelImg)를 이용합니다.
- 라벨링 할 때 왼쪽 사이드바에 옵션 선택에 `yolo`로 변경하면 자동으로 `txt`로 저장을 해줍니다.
### 학습(training) 관련
- 학습을 진행할때는 `obj.names` 순서로 `labelImg` 프로그램 내 클래스가 설정되어있어야합니다.
  - 예를 들어서, 만약 A부터 0까지 대문자와 숫자만 학습을 시킨다면 해당 클래스는 A부터 '0' 그리고 0은 35의 `index`를 가질 것 입니다.
  - A:0, B:1, C:2, D:3, ...
  - 소문자를 학습시키려면 (숫자)0 이후로의 index로 학습을 이어서 진행하면 됩니다. [예시 보러가기](#example)
- 라벨링한 결과물은 `recently_labeled` 디렉토리안에 저장합니다.
  - 저장한 결과물은 지정한 날짜에 학습을 진행합니다.
- 학습을 진행하기전에 먼저 `recently_labeled`에서 `on_training` 디렉토리로 파일들을 이동해 `recently_labeled` 디렉토리를 비워줍니다.
- 학습을 진행하려면 colab을 이용해야하는데 제 생각에는 또 다시 colab 내 VM을 이용해서 저희 repository를 clone해 가는 것도 좋을 것 같습니다.
### 가중치(weights) 관련
- 학습이 종료되면 업데이트된 가중치를 `weights` 디렉토리안에 저장합니다.
  - 저장하는 형식은 `YYYYMMDD_last.weights` / `YYYYMMDD_best.weights`로 저장합니다.

## TODO
**👉 colab에서 clone후 바로 사용할 수 있게 제작**
- [x] `recently_labeled`안에 저장된 txt파일들을 인식해서 자동으로 `train.txt`생성해주는 code 
- [x] `train.txt` 생성 후 `recently_labeled` 에서 `on_training`으로 복사와 내부 디렉토리를 비워주는 code
- [ ] 학습이 종료되면 가중치를 자동으로 저장해주는 code → 저희가 fork한 darknet repository를 수정해야겠네요.

## example
``` bash
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
1
2
3
4
5
6
7
8
9
0
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
```
