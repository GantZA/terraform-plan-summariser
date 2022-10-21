import prettytable
from prettytable import DOUBLE_BORDER
from colorama import Fore, Style


def test_pretty_table():

    x = prettytable.PrettyTable()
    x.hrules = prettytable.ALL
    x.field_names = ["Change", "Name", "Name Count", "Type", "Type Count"]
    x.add_row([
        Fore.GREEN + "ADD" + Style.RESET_ALL,
        "module.proxy[0].module.proxy_launch_template.aws_launch_template.launch_template\nmodule.proxy[1].module.proxy_launch_template.aws_launch_template.launch_template",
        "2",
        "aws_launch_template",
        "1"
    ])
    x.add_row([
        Fore.YELLOW + "UPDATE" + Style.RESET_ALL,
        "module.rds.aws_security_group_rule.database_self",
        "1",
        "aws_security_group_rule",
        "1"
    ])
    # x.add_row([Fore.RED + "DESTROY" + Style.RESET_ALL, "module.rds.aws_security_group_rule.database_self"])

    x.set_style(DOUBLE_BORDER)
    print(type(x))
    print(x)


test_pretty_table()
#
# - group by change
# -group by name
#  - group by type
