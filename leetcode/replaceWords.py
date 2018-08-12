class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        def find_root(dict, token: str):

            match = None
            for root in dict:
                if token.startswith(root) and match == None:
                    match = root
                    continue

                if token.startswith(root) and len(root) < len(match):
                    match = root
                    continue

            return match

        input = sentence.split(" ")
        output = list()

        for token in input:
            root = find_root(dict, token)
            if root is not None:
                output.append(root)
                continue
            output.append(token)

        return " ".join(output)

if __name__ == '__main__':
    # n = [3, 9, 20, None, None, 15, 7]

    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    s = Solution().replaceWords(dict, sentence)

    from pprint import pprint
    pprint(s)
