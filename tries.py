import tries_utility

WORDS = ['dog', 'deer', 'deal']


# problem 1 - naive solution
def autocomplete_1(prefix):
    results = set()
    for word in WORDS:
        if word.startswith(prefix):
            results.add(word)
    return results


class TrieEx:
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[tries_utility.ENDS_HERE] = True

    def find(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                return []
            trie = trie[char]
        return self._elements(trie)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == tries_utility.ENDS_HERE:
                sub_result = ['']
            else:
                sub_result = [c + s for s in self._elements(v)]
            result.extend(sub_result)
        return result


def autocomplete_2(prefix, trie):
    suffices = trie.find(prefix)
    return [prefix + w for w in suffices]


# problem 2
class TrieNode:
    def __init__(self):
        self.letters = {}
        self.total = 0


class PrefixMapSum:
    def __init__(self):
        self._trie = TrieNode()
        self.map = {}

    def insert(self, key, value):
        value -= self.map.get(key, 0)
        self.map[key] = value

        trie = self._trie
        for char in key:
            if char not in trie.letters:
                trie.letters[char] = TrieNode()

            trie = trie.letters[char]
            trie.total += value

    def get_sum(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d.letters:
                d = d.letters[char]
            else:
                return 0
        return d.total


# problem 3
class TrieEx2:
    def __init__(self, k):
        self._trie = {}
        self.size = k

    def insert(self, item):
        trie = self._trie

        for i in range(self.size, -1, -1):
            bit = bool(item & (1 << i))
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]

    def find_max_xor(self, item):
        trie = self._trie
        xor = 0

        for i in range(self.size, -1, -1):
            bit = bool(item & (1 << i))
            if (1 - bit) in trie:
                xor |= 1 << i
                trie = trie[1-bit]
            else:
                trie = trie[bit]

        return xor


def find_max_xor(array):
    k = max(array).bit_length()
    trie = TrieEx2(k)

    for num in array:
        trie.insert(num)

    xor = 0
    for num in array:
        xor = max(xor, trie.find_max_xor(num))

    return xor

if __name__ == "__main__":
    print("\n#####***** Solution 1 ******#####")
    print(autocomplete_1('de'))
    trie = TrieEx()
    for w in WORDS:
        trie.insert(w)
    print(autocomplete_2('de', trie))

    print("\n#####***** Solution 2 ******#####")
    map_sum = PrefixMapSum()
    map_sum.insert('col', 2)
    map_sum.insert('column', 22)
    map_sum.insert('color', 3)
    print(map_sum.get_sum('colo'))
    print(map_sum.get_sum('pet'))

    print("\n#####***** Solution 3 ******#####")
    array = [7,6,0]
    print(find_max_xor(array))