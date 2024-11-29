import find_1
import recursion_2
import dynamic_3
import graph_4

def test_finder():
    result = find_1.finder(5, 100, 50, [10, 30, 60, 80, 100])
    print(f"Actual result: {result}")
    assert result == 500
    print("Max Fuel Test Passed")

def test_recursion():
    tree = [
        [], [2, 3], [1, 4], [1], [2]
    ]
    n = len(tree) - 1
    dp = [[-1 for _ in range(2)] for _ in range(n + 1)]
    
    result = recursion_2.recursion(1, -1, True, dp, tree)
    
    print(f"Actual result: {result}")
    assert result == 2
    print("Vertex Cover Test Passed")

def test_dynamic():
    test_cases = [
        ("123", 3),
        ("226", 3),
        ("06", 0),
        ("1", 1),
        ("12345", 3),
    ]
    
    for inp, expected in test_cases:
        result = dynamic_3.dynamic(inp)
        print(f"Input: {inp}, Expected: {expected}, Got: {result}")
        assert result == expected, f"Test failed for input {inp}. Expected {expected}, but got {result}"
    
    print("All Count Decodings Tests Passed")

def test_graph():
    n = 4
    m = 4
    edges = [(1, 2), (2, 3), (3, 4)]
    result = graph_4.graph(n, m, edges)
    print(f"Test 1 - Expected: 3, Got: {result}")
    assert result == 3, f"Test 1 Failed: Expected 3, but got {result}"

    n = 4
    m = 5
    edges = [(1, 2), (2, 3), (3, 4), (4, 2)]
    result = graph_4.graph(n, m, edges)
    print(f"Test 2 - Expected: 2, Got: {result}")
    assert result == 2, f"Test 2 Failed: Expected 2, but got {result}"

    n = 4
    m = 3
    edges = [(1, 2), (2, 3)]
    result = graph_4.graph(n, m, edges)
    print(f"Test 3 - Expected: -1, Got: {result}")
    assert result == -1, f"Test 3 Failed: Expected -1, but got {result}"

    n = 1
    m = 0
    edges = []
    result = graph_4.graph(n, m, edges)
    print(f"Test 4 - Expected: 0, Got: {result}")
    assert result == 0, f"Test 4 Failed: Expected 0, but got {result}"

    n = 10
    m = 9
    edges = [(i, i+1) for i in range(1, 10)]
    result = graph_4.graph(n, m, edges)
    print(f"Test 5 - Expected: 9, Got: {result}")
    assert result == 9, f"Test 5 Failed: Expected 9, but got {result}"

    print("All BFS Shortest Path Tests Passed")

def run_tests():
    test_finder()
    test_recursion()
    test_dynamic()
    test_graph()

if __name__ == "__main__":
    run_tests()
