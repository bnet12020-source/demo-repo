def calculate_total(items):
    return sum(item['price'] for item in items)


def print_receipt(items):
    total = calculate_total(items)
    print(f"Total: {total}")
