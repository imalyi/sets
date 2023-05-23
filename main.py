class Sets:
    def __init__(self):
        self.parent = [None] * 10000
        self.rank = [None] * 1000

    def add_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
            if i != self.parent[i]:
                self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def trace(self, i):
        trace = []
        while i != self.parent[i]:

            i = self.parent[i]
            if i != self.parent[i]:
                trace.append(i)
                self.parent[i] = self.find(self.parent[i])
        return trace

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id

        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[i_id] + 1


def main():
    sets = Sets()
    for i in range(9):
        sets.add_set(i)

    pairs = [(0, 1), (2, 3), (1, 2), (5, 6), (7, 8), (3, 5), (0, 7)]
    for pair in pairs:
        sets.union(sets.find(pair[0]), sets.find(pair[1]))

    for i in range(9):
        print(f"dla {i} sciezka {sets.trace(i)}")


if __name__ == "__main__":
    main()
