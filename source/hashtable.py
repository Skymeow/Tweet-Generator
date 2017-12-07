#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all keys in each of the buckets
        # O(n2) time?
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all values in each of the buckets
        # O(n2) time?
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all pairs of key-value entries in each of the buckets
        # O(n) time
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # O(n2)?
        # Count number of enties of each bucket
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        # O(l) for l items in bucket,  O(1) best case,  O(l) wrost case
        bucket_index = self._bucket_index(key)
        found_bucket = self.buckets[bucket_index]
        # Check if an entry with the given key exists in that bucket
        entry = found_bucket.find(lambda linked_item: linked_item[0] == key)
        if entry:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        # O(n) time wrost if the item neat tail, O(1) if near head or doesn't exsit
        bucket_index = self._bucket_index(key)
        found_bucket = self.buckets[bucket_index]
        # Find the entry with the given key in that bucket, if one exists
        entry = found_bucket.find(lambda linked_item: linked_item[0] == key)
        if entry:
            # print('this is get entry', entry)
            return entry[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value."""
        # Find the bucket the given key belongs in
        # O(n) time
        bucket_index = self._bucket_index(key) #o(1)
        found_bucket = self.buckets[bucket_index] #o(1)
        # Find the entry with the given key in that bucket, if one exists
        # O(l) for l items in bucket,  O(1) best case,  O(l) wrost case
        entry = found_bucket.find(lambda linked_item: linked_item[0] == key)
        if entry:
            found_bucket.delete(entry) # O(l) for l items in bucket (LL)
        found_bucket.append((key, value)) # O(1)


    def delete(self, key):
        # Find the bucket the given key belongs in
        # # O(l) for l items in bucket,  O(1) best case,  O(l) wrost case
        bucket_index = self._bucket_index(key)
        found_bucket = self.buckets[bucket_index]
        # Find the entry with the given key in that bucket, if one exists
        entry = found_bucket.find(lambda linked_item: linked_item[0] == key)
        if entry:
            found_bucket.delete(entry)
        else:
            raise KeyError('key not exists: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
