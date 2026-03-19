import requests

def test_compute_sum():
    url = "http://localhost:8021/sum"
    params = {'a': 2, 'b': 3}
    response = requests.get(url, params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["sum"] == 5
    assert data["name"] == "Tung"
    print("Test passed:", data)

if __name__ == "__main__":
    test_compute_sum()