def limited_hash(left: int, right: int, hash_function=hash):
    def inner_hash_function(obj):
        hash_value = hash_function(obj)
        if hash_value < left:
            hash_value = right - (left - hash_value - 1) % (right - left + 1)
        elif hash_value > right:
            hash_value = left + (hash_value - right - 1) % (right - left + 1)
        return hash_value
    return inner_hash_function