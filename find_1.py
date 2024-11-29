# https://www.spoj.com/problems/TTBRM/en/

def finder(n, m, d, stations):
    stations.sort()
    total_fuel = 0
    last_position = 0

    for i in range(n):
        if stations[i] - last_position > d:
            print(f"A(z) {stations[i]}-es kút túl messze van a {last_position} helyről, megállunk.")
            break
        
        total_fuel += m
        last_position = stations[i]

    print(f"Összes felhasznált üzemanyag: {total_fuel}")
    return total_fuel

def main():
    n = int(input())  # kutak száma
    m = int(input())  # maximális üzemanyag kapacitás
    d = int(input())  # maximális távolság a kutak között
    stations = list(map(int, input().split()))  # a kutak helyei
    
    print(finder(n, m, d, stations))

if __name__ == "__main__":
    main()
