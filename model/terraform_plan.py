from enum import Enum
from typing import List


class Action(Enum):
    CREATE: str = "create"
    UPDATE: str = "update"
    DELETE: str = "delete"


class Change:
    actions: List[Action]


class ResourceChange:
    address: str
    module_address: str
    mode: str
    type: str
    name: str
    provider_name: str
    change: Change


class TerraformPlan:
    format_version: str
    terraform_version: str
    prior_state: dict
    configuration: dict
    planned_values: dict
    # proposed_unknown: dict
    variables: dict
    resource_drift: List[dict]
    output_changes: dict
    resource_changes: List[ResourceChange]
