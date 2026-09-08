import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ValidationError(Exception):
    pass


def validate_input(data: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")
    if "id" not in data or not isinstance(data["id"], (int, str)):
        raise ValidationError("Invalid or missing 'id' field")
    if "action" not in data or not isinstance(data["action"], str):
        raise ValidationError("Invalid or missing 'action' field")
    if "payload" in data and not isinstance(data["payload"], dict):
        raise ValidationError("'payload' must be a dictionary if provided")
    return data


def process_items(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results = []
    for index, item in enumerate(items):
        try:
            valid_data = validate_input(item)
            item_id = valid_data["id"]
            action_type = valid_data["action"]
            payload = valid_data.get("payload", {})

            logger.info(f"Processing item {item_id} with action '{action_type}'")
            results.append({
                "id": item_id,
                "status": "success",
                "result": f"Executed {action_type} with {len(payload)} parameters"
            })
        except ValidationError as err:
            logger.warning(f"Validation failed for item at index {index}: {err}")
            results.append({
                "index": index,
                "status": "failed",
                "error": str(err)
            })
    return results


if __name__ == "__main__":
    sample_batch = [
        {"id": 101, "action": "sync", "payload": {"target": "db"}},
        {"id": "invalid_no_action"},
        "not_a_dict",
        {"id": 102, "action": "clean"}
    ]
    processed = process_items(sample_batch)
    print(f"Processed {len(processed)} items successfully.")