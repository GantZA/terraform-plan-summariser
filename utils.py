import json
from typing import List

from model.terraform_plan import TerraformPlan, ResourceChange, Change


def read_tf_plan_json(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
    return data


def extract_actions(change_dict):
    return {
        "actions": change_dict["actions"]
    }


def extract_change(resource_change_dict):
    return {
        "change": extract_actions(resource_change_dict["change"])
    }


def extract_resource_change(resource_change_dict):
    return {
        "address": resource_change_dict["address"],
        "module_address": resource_change_dict["module_address"],
        "mode": resource_change_dict["mode"],
        "type": resource_change_dict["type"],
        "name": resource_change_dict["name"],
        "provider_name": resource_change_dict["provider_name"],
        "change": extract_change(resource_change_dict),
        "action_reason": resource_change_dict.get("action_reason")
    }


def remove_no_op_changes(resource_changes_dicts):
    filtered_changes = []
    for i in resource_changes_dicts:
        if "no-op" not in i["change"]["actions"]:
            filtered_changes.append(extract_resource_change(i))

    return filtered_changes


def dict_to_change(data: dict) -> Change:
    change: Change = Change()
    setattr(change, "actions", data["actions"])
    return change


def dict_to_resource_change(data: List[dict]) -> List[ResourceChange]:
    resource_changes: List[ResourceChange] = []
    for res in data:
        if "no-op" not in res["change"]["actions"]:
            resource_change: ResourceChange = ResourceChange()
            for key, value in res.items():
                if key == "change":
                    value = dict_to_change(value)
                setattr(resource_change, key, value)
            resource_changes.append(resource_change)
    return resource_changes


def dict_to_terraform_plan(data: dict) -> TerraformPlan:
    terraform_plan: TerraformPlan = TerraformPlan()
    for key, value in data.items():
        if key == "resource_changes":
            value = dict_to_resource_change(value)
        setattr(terraform_plan, key, value)
    return terraform_plan
