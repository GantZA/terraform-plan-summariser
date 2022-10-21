import prettytable
# from prettytable.colortable import ColorTable, Themes
from prettytable import PrettyTable, DOUBLE_BORDER
from colorama import Fore, Style

from model.terraform_plan import TerraformPlan, ResourceChange, Action


def summarise_as_table(terraform_plan: TerraformPlan, query: str = "") -> str:
    create_list: list[ResourceChange] = []
    update_list: list[ResourceChange] = []
    delete_list: list[ResourceChange] = []

    unique_create_types: dict[str, int] = {}
    unique_update_types: dict[str, int] = {}
    unique_delete_types: dict[str, int] = {}

    for resource_change in terraform_plan.resource_changes:
        actions = resource_change.change.actions
        if query in resource_change.type:
            if Action.CREATE.value in actions:
                create_list.append(resource_change)
                unique_create_types.update({resource_change.type: unique_create_types.get(resource_change.type, 0) + 1})
            elif Action.UPDATE.value in actions:
                update_list.append(resource_change)
                unique_update_types.update({resource_change.type: unique_update_types.get(resource_change.type, 0) + 1})
            elif Action.DELETE.value in actions:
                delete_list.append(resource_change)
                unique_delete_types.update({resource_change.type: unique_delete_types.get(resource_change.type, 0) + 1})
            else:
                print(f"WARN: Unknown resource change change action: {actions}")
    pt: PrettyTable = PrettyTable()
    pt.set_style(DOUBLE_BORDER)
    pt.hrules = prettytable.ALL
    pt.field_names = [Fore.BLUE + "Change" + Style.RESET_ALL, Fore.BLUE + "Name" + Style.RESET_ALL,
                      Fore.BLUE + "Resource Count" + Style.RESET_ALL, Fore.BLUE + "Type" + Style.RESET_ALL,
                      Fore.BLUE + "Type Count" + Style.RESET_ALL]

    pt.add_row([Fore.GREEN + "ADD" + Style.RESET_ALL,
                "\n".join([i.address for i in create_list]),
                len(create_list),
                "\n".join(unique_create_types.keys()),
                "\n".join(map(str, list(unique_create_types.values()))),
                ])

    pt.add_row([Fore.YELLOW + "CHANGE" + Style.RESET_ALL,
                "\n".join([i.address for i in update_list]),
                len(update_list),
                "\n".join(unique_update_types.keys()),
                "\n".join(map(str, list(unique_update_types.values()))),
                ])

    pt.add_row([Fore.RED + "DESTROY" + Style.RESET_ALL,
                "\n".join([i.address for i in delete_list]),
                len(delete_list),
                "\n".join(unique_delete_types.keys()),
                "\n".join(map(str, list(unique_delete_types.values()))),
                ])

    return pt.get_string()
