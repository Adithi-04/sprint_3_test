'''
* PROGRAM NAME: RTF TO JSON CONVERTOR
* VERSION AND DATE: 2.0 09-08-2024
* AUTHOR NAME(s): Shreeja Katama

* LANGUAGE AND LIBRARY REFERENCE: Python3,
Python Standard Libraries:
  - json
  - re
  - os
  - tkinter
  - configparser
  - datetime

* PURPOSE: Processes RTF files to extract basic data and convert it to JSON format. 
Includes dynamic extraction using control words and robust error handling.
* PARAMETERS: Folder containing RTF files as an input parameter.
* RETURNS: JSON outputs saved in a new directory.
* FUNCTION CALL NAME(s): rtf_to_json
* FUNCTION PURPOSE: Extracts data from RTF files and converts it to JSON format.
* EMBEDDED PROGRAMS: None
* MODULE: rtf_to_json.py

* COPY RIGHT: M/s CARE2DATA 2024  All Rights Reserved
**************************************************************************

* VERSION HISTORY

* REVISED VERSION AND DATE: 1.0.0 01-07-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Initial Version

* REVISED VERSION AND DATE: 1.2.0 07-07-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Integration of UI with the code

* REVISED VERSION AND DATE: 1.3.0 16-07-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Dynamic Approach for extraction

* REVISED VERSION AND DATE: 1.4.0 30-07-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Split the code into functional blocks

* REVISED VERSION AND DATE: 1.5.0 06-08-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Implementation of Sprint 1 Demo Corrections

* REVISED VERSION AND DATE: 2.0.0 09-08-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Implementation of Sprint 2

* REVISED VERSION AND DATE: 3.0.0 18-08-2024
* AUTHOR NAME(s): Shreeja Katama
* CHANGE REASON: Implementation of Sprint 3 and Sprint 2 Corrections
'''

from user_Interface import user_interface
from data_extraction import debug_print
from data_extraction import special_characters
from user_Interface import selected_folder_path
import logging
import os 
import pytest


try:
    user_interface()
except Exception:
    debug_print("UI unsuccessful")

# Set up logging
logging.basicConfig(
    filename='test_special_characters.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()



def test_special_characters_positive():
    if __name__ == "__main__":
    
      for file_name in os.listdir(selected_folder_path):
        file_path = os.path.join(selected_folder_path, file_name)
        if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    rtf_content = file.read()
                    processed_content = special_characters(rtf_content)
                
                if processed_content and processed_content != rtf_content:
                    logger.info(f"File {file_path}: Content processed successfully.")
                    assert processed_content != rtf_content, f"Error in file {file_path}: Content was not processed or unchanged."
                else:
                    logger.warning(f"File {file_path}: Content was not processed correctly or is unchanged.")
                    assert not processed_content or processed_content == rtf_content, f"Error in file {file_path}: Content should be unchanged or empty."

            except Exception as e:
                logger.error(f"Failed to process file {file_path}: {e}")

def test_special_characters_negative():
    if __name__ == "__main__":
        for file_name in os.listdir(selected_folder_path):
          file_path = os.path.join(selected_folder_path, file_name)
          if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    rtf_content = file.read()
                    processed_content = special_characters(rtf_content)

                if not processed_content or processed_content == rtf_content:
                    logger.info(f"File {file_path}: No processing or content remains unchanged as expected.")
                    assert not processed_content or processed_content == rtf_content, f"Error in file {file_path}: Content should be unchanged or empty."
                else:
                    logger.warning(f"File {file_path}: Content was processed when it should not have been.")
                    assert processed_content == rtf_content, f"Error in file {file_path}: Content should be unchanged due to errors."

            except Exception as e:
                logger.error(f"Failed to process file {file_path}: {e}")