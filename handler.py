import sys

def validate_input(data):
    if not isinstance(data, dict):
        return False
    if 'id' not in data or not isinstance(data['id'], int):
        return False
    if 'payload' not in data or not isinstance(data['payload'], str):
        return False
    return True

def process_stream(input_data):
    for entry in input_data:
        if not validate_input(entry):
            print(f'invalid data format: {entry}', file=sys.stderr)
            continue
        
        try:
            execute_task(entry)
        except Exception as e:
            print(f'execution failure: {e}', file=sys.stderr)

def execute_task(data):
    print(f'processing item {data["id"]}')

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'payload': 'task_alpha'},
        {'id': 'invalid', 'payload': 'fail'},
        {'id': 2, 'payload': 'task_beta'}
    ]
    process_stream(sample_data)