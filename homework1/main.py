class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = {} 

    def hash(self, key):
        return hash(key)

    def _resize(self):
        old_items = list(self.table.items())
        self.capacity *= 2
        self.table = {}
        self.size = 0

        #put all to table
        for key, value in old_items:
            self.put(key, value)

    def put(self, key, value):
        #filling factor if more 70%
        if self.size / self.capacity > 0.7:
            self._resize()
        key_hash = self.hash(key)
        index = key_hash % self.capacity

        #comparing idx in table with each other
        original_index = index
        while index in self.table:
            existing_key, _ = self.table[index]
            if existing_key == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity
            if index == original_index:
                raise Exception("Hash table is full")

        self.table[index] = (key, value)
        self.size += 1

        print(key_hash)
        print(index)

    def get(self, key):
        key_hash = self.hash(key)
        index = key_hash % self.capacity
        start_index = index

        while index in self.table:
            s_key, s_value = self.table[index]

            if s_key == key:
                return s_value
            index = (index + 1) % self.capacity
            #try to find next idx
            if index == start_index:
                break
        return None


#class instance
hash_table = HashTable()
hash_table.put("name", "Denis")
hash_table.put("address", "street Stree")
hash_table.put("ndawdwdaame", "WCBWABBW")
hash_table.put("adddawdawress", "stbdwaffwaStree")