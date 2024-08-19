import json
import os
from datetime import datetime
import logging1

def json_conversion(json_dictionary, item, output_directory):
    '''
    Function to create json file
    '''
    output_file = os.path.join(
        output_directory,
        f"{os.path.splitext(os.path.basename(item))[0]}.json"
        )

    with open(output_file, 'w', encoding = "utf-8") as f:
        json.dump(json_dictionary , f, ensure_ascii=False, indent=4)
    logging1.write_success(datetime.now().isoformat() + f" Data successfully written to {output_file}\n")

    return "Successful", ""
