def get_last(items):
    if items:
        return items[-1]
    return None


items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]

print(get_last(items))

print(get_last([]))


