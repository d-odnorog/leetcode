# https://leetcode.com/problems/search-suggestions-system/
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        product = []
        for i in range(len(searchWord)):
            p = []
            for prod in products:
                if prod.startswith(searchWord[: i + 1]):
                    p.append(prod)
            p = sorted(p)[:3]
            product.append(p)

        return product


if __name__ == "__main__":
    s = Solution()

    assert s.suggestedProducts(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        "mouse",
    ) == [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
    assert s.suggestedProducts(["havana"], "havana") == [
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
        ["havana"],
    ]
    assert s.suggestedProducts(
        ["bags", "baggage", "banner", "box", "cloths"],
        "bags",
    ) == [
        ["baggage", "bags", "banner"],
        ["baggage", "bags", "banner"],
        ["baggage", "bags"],
        ["bags"],
    ]
