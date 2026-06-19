class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        idx = []
        count = 0
        for st in strs:
            string+=st+">>>>>"
        print("encode: "+string)
        return string

    def decode(self, s: str) -> List[str]:
        my_list = s.split(">>>>>")
        print(f"decode: {my_list}")
        return my_list[:-1]
