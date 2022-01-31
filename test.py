import requests

ENDPOINT = "http://127.0.0.1:5000/predict"

# Example of input with one single input
simple_input = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

res_simple_input = requests.post(ENDPOINT, json=simple_input)
assert res_simple_input.status_code == 200
print(res_simple_input.json())


# Example of input with several inputs
multiple_input = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8],
              [5.0, 0.98, 0.32, 18.9, 0.050, 75.0, 122.0, 0.401, 3.1, 0.21, 1.2]]
}

res_multiple_input = requests.post(ENDPOINT, json=multiple_input)
assert res_multiple_input.status_code == 200
print(res_multiple_input.json())