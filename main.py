# python3
def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        self.name = ""
        if self.type == 'add':
            self.name = query[2] 
       
class QueryProcessor:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]
        self._multiplier = 263
        self._prime = 1000000007

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket
        print(self.buckets)

    def delete(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break

    def find(self, string):
        hashed = self._hash_func(string)
        for s in self.buckets[hashed]:
            if s == string:
                return "yes"
        return "not found"

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    #print('\n'.join(result))
    for r in result:
        print(r)

def process_queries(queries):
    result = []
    bucket_count = 5
    proc = QueryProcessor(bucket_count)
    for query in queries:
        if query.type == "add" and query.name is not None:
            proc.add(query.name)
        elif query.type == "del" and query.name is not None:
            proc.delete(query.name)
        else:
            res = proc.find(query.name)
            if res == "yes":
                result.append(query.name)
            else:
                result.append("not found")
    return result

#def process_queries(queries):
    #result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    #contacts = []
    #for cur_query in queries:
        #if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            #for contact in contacts:
                #if contact.number == cur_query.number:
                    #contact.name = cur_query.name
                    #break
            #else: # otherwise, just add it
                #contacts.append(cur_query)
        #elif cur_query.type == 'del':
            #for j in range(len(contacts)):
                #if contacts[j].number == cur_query.number:
                    #contacts.pop(j)
                    #break
        #else:
            #response = 'not found'
            #for contact in contacts:
                #if contact.number == cur_query.number:
                    #response = contact.name
                    #break
            #result.append(response)
    #return result

if __name__ == '__main__':
    #write_responses(process_queries(read_queries()))
    queries = read_queries()
    result = process_queries(queries)
    write_responses(result)
