#** Reverse a String**

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        temp = ""
        for c in s:
            if c != " ":
                temp += c
            elif temp != "":
                ans.append(temp)
                temp = ""
        if temp != "":
            ans.append(temp)
        
        i = 0
        j = len(ans) - 1
        while i < j:
            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1

        return " ".join(ans)

# Example usage:
sol = Solution()
print(sol.reverseWords("the sky is blue"))  # Output should be "blue is sky the"
