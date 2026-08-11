class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)

        if endWord not in wordset:
            return 0
        
        quene = deque([(beginWord, 1)])
        visited = {beginWord}

        while quene:
            word, steps = quene.popleft()

            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(ord('a') + j) + word[i + 1:]
                
                    if newWord == endWord:
                        return steps + 1
                    
                    if newWord in wordset and newWord not in visited:
                        visited.add(newWord)
                        quene.append((newWord, steps + 1))
        return 0
