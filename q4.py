import requests

class q4:

    def __init__(self):
        """Solves question 4"""
        response = requests.get("https://dev.beepbeep.tech/v1/sample_customer")
        self.raw = response.json()

    def sort(self):
        """Sorts the the promotion portion of the raw responses"""
        promotions_raw = self.raw["promotions"]
        promotions_sorted = sorted(promotions_raw, key = lambda k: k['title'])
        return promotions_sorted

    def generate_sorted(self):
        """generates the full response with sorted promotions"""
        out = self.raw
        out["promotions"] = self.sort()
        return out

if __name__ == "__main__":
    r = q4()
    print(r.generate_sorted())