class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 1:
            return strs[0]

        i = 0
        for z in zip(*strs):
            for c in z:
                if c != z[0]:
                    return strs[0][:i]
            i += 1

        return strs[0][:i]


# test it out
def main():
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))


if __name__ == "__main__":
    main()
