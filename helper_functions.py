import json


# helper function to write to json file
def write_to_json_file(new_product: dict[str, str], filename='products.json') -> dict:
    with open(filename, 'r+') as file:
        # load file as dict
        products_file = json.load(file)
        products_file['products'].append(new_product)
        file.seek(0)
        json.dump(products_file)


# call function 
write_to_json_file(file)
        