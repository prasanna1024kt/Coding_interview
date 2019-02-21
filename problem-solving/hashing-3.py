class hashTableChaining(object):

    def __init__(self,size):
        self.size=size
        self.hash_table = [[] for _ in range(self.size)]


    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self,key):
        hash_key = hash(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self, key):
        hash_key = hash(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print ('Key {} deleted'.format(key))
        else:
            print ('Key {} not found'.format(key))


obj=hashTableChaining(25)

obj.insert(11,'prasanna')
obj.insert(13,'kumar')
obj.insert(12,'ptr')
print(obj.search(11))
print(obj.search(12))
print(obj.hash_table)
print(obj.delete(12))
print(obj.hash_table)
