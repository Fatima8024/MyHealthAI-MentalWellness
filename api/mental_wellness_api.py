import json

def load_flows():
    with open('data/mental_wellness_flows.json') as f:
        return json.load(f)

def get_response(intent, step):
    flows = load_flows()
    return flows["mental_wellness_flows"][intent]["flow"][step]["response"]

if __name__ == "__main__":
    print(get_response("stress", 0))

