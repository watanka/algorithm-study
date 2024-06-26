## 그리디
- 탐욕이라는 뜻으로 문제를 해결하기 위한 모든 옵션을 탐색한다. 
- 각 옵션(스텝)에서 미래를 고려하지 않고, 최적의 해만을 탐색한다.
- 가장 단순명료한 접근인만큼, 시간이나 메모리 제한에 걸릴 수 있다.
- 시간이나 메모리 제한에 걸리는 경우, 종료 조건을 추가하거나, 배열에 중복되는 연산을 기록해 연산량을 줄이는 DP를 활용할 수 있다.

## 구현코드
```
n = 4900
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types: # 가장 큰 화폐부터 빼나감
    count += n // coin # 큰 화폐로 처리할 수 있는 가장 큰 값을 처리한다.
    n %= coin

print(count)
```

