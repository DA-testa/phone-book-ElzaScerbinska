# python3

class HashTable:
    def __init__(self, bucket_count=10):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]
        self._prime = 1000000007
        self._multiplier = 263

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, key, string):
        #hashed = self._hash_func(string)
        hashed = self._hash_func(key)
        bucket = self.buckets[hashed]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, item)
                return
        bucket.append((key, item))
        #if string not in bucket:
            #self.buckets[hashed] = [string] + bucket
        print(self.buckets)

    def delete(self, key):
        hashed = self._hash_func(key)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                break

    def find(self, key):
        hashed = self._hash_func(key)
        for item in self.buckets[hashed]:
            if item[0] == key:
                return item[1]
        #hashed = self._hash_func(string)
        #if string in self.buckets[hashed]:
            #return self.buckets[hashed][0]
        return "not found"

hash_table = HashTable()
num_queries = int(input())
output = []

for i in range(num_queries):
    query = input().split()
    if query[0] == "add":
        key, item = query[1], query[2]
        hash_table.add(key, item)
    elif query[0] == "del":
        hash_table.delete(query[1])
    elif query[0] == "find":
        output.append(hash_table.find(query[1]))

print("\n".join(output))
