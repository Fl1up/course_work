import operator
from Utils import load_json, number_card, load_dates


def main():
    operations = []

    for _ in range(5):
        operations.append(load_json("operations.json"))
    operations.sort(key=operator.itemgetter("date"))

    for operation in operations:
        load_dict = load_json("operations.json")

        for key, values in load_dict.items():
            if values == "EXECUTED":

                load_date = [load_dates(load_dict)]
                load_to = load_dict["to"]
                print((f'{load_dates(load_dict)}'
                       
                    f' {load_dict["description"]}\n'
                    f'{number_card(load_dict)} -> Счет {"**" + load_to[20:]}\n'
                    f'{load_dict["operationAmount"]["amount"]} {load_dict["operationAmount"]["currency"]["name"]}\n'))

main()