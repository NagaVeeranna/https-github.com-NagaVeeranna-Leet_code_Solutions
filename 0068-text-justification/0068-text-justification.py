from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            line = []
            line_length = len(words[i])
            line.append(words[i])
            i += 1

            while i < n and line_length + 1 + len(words[i]) <= maxWidth:
                line_length += 1 + len(words[i])
                line.append(words[i])
                i += 1

            if i == n or len(line) == 1:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
                result.append(s)
                continue

            total_word_length = sum(len(word) for word in line)
            total_spaces = maxWidth - total_word_length
            gaps = len(line) - 1
            spaces, extra = divmod(total_spaces, gaps)

            justified = ""
            for j in range(gaps):
                justified += line[j]
                justified += " " * (spaces + (1 if j < extra else 0))
            justified += line[-1]

            result.append(justified)

        return result