class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                graph[pattern].append(word)
            
        queue = deque([beginWord])
        visited = set([beginWord])
        level = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return level
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for w in graph[pattern]:
                        
                        if w not in visited:
                            queue.append(w)
                            visited.add(w)
            
            level += 1
        
        return 0
                        