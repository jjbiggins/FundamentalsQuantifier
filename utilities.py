import json

def create_drop_down_options(json_file, dictionary=True):
    with open(f"data/{json_file}", "r") as read_file:
        data = json.load(read_file)

    output = []
    for item in data:
        if dictionary is True:
            output.append({'label': item, 'value': data[item]})
        else:
            output.append({'label': item, 'value': item})

    return output




# def create_drop_down_options(data, dictionary=True):
#     data_list = []
#
#     if dictionary is True:
#         for value in data:
#             data_list.append({'label': value, 'value': data[value]})
#     else:
#         for value in data:
#             data_list.append({'label': value, 'value': value})
#
#     return data_list