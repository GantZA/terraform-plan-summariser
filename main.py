import argparse
from utils import read_tf_plan_json, dict_to_terraform_plan
from output.table import summarise_as_table


def execute(args):
    data = read_tf_plan_json(args.path)
    terraform_plan = dict_to_terraform_plan(data)
    print(summarise_as_table(terraform_plan, query=args.query))


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(
        prog="tps",
        description="Terraform Plan Summariser. Given a Terraform Plan JSON as input, TPS will output a short summary"
                    " with granular details highlighting the important parts of the plan."
    )

    # Add the arguments
    my_parser.add_argument(
        "--path",
        metavar="-p",
        type=str,
        help="The path to the JSON Plan file.",
        required=True
    )

    my_parser.add_argument(
        "--query",
        metavar="-q",
        type=str,
        help="Optional query to further filter the resources you are looking at",
        default="",
        required=False
    )

    args = my_parser.parse_args()
    execute(args)
