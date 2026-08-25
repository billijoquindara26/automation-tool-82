def validate_item(item):
    if not isinstance(item, dict):
        return False
    if 'id' not in item or not isinstance(item['id'], int) or item['id'] <= 0:
        return False
    if 'value' not in item or not isinstance(item['value'], (int, float)) or item['value'] <= 0:
        return False
    if 'name' not in item or not isinstance(item['name'], str) or len(item['name'].strip()) == 0:
        return False
    return True

def process_data(data_list):
    results = []
    for item in data_list:
        if validate_item(item):
            processed = {
                'id': item['id'],
                'name': item['name'].strip().title(),
                'value': round(item['value'] * 1.05, 2)
            }
            results.append(processed)
    return results

def main():
    input_data = [
        {'id': 1, 'value': 100.5, 'name': '  item one  '},
        {'id': 2, 'value': -20, 'name': 'item two'},
        {'id': 3, 'value': 150, 'name': ''},
        {'id': 4, 'value': 75, 'name': 'item four'},
        {'id': 0, 'value': 200, 'name': 'item five'},
        {'id': 5, 'value': 50, 'name': 'item six'}
    ]
    output = process_data(input_data)
    for result in output:
        print(result)

if __name__ == '__main__':
    main()