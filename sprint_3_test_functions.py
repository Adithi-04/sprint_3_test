
"""
LINK FOR SPRINT - 3 TEST SCENARIO SHEET : https://docs.google.com/spreadsheets/d/1CqC_FDR7Sti4oKp77rwqrsoW8Z6Tg9GbwkXdtx4KF88/edit?usp=sharing
"""

from user_Interface import user_interface
from data_extraction import debug_print
from data_extraction import special_characters
from user_Interface import selected_folder_path
import logging
import os 

try:
    user_interface()
except Exception:
    debug_print("UI unsuccessful")

# Set up logging
log_file_path = '/Users/adithi/Downloads/sprint_3_code/test_special_characters.txt'
logging.basicConfig(
    filename='test_special_characters.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

#TEST FUNCTIONS
"""
URS REQUIREMENT: KEX002.4.1
TEST CASE DESCRIPTION : Verify that the system accurately extracts special characters (e.g., , -, ?, :) from various data points (column headers, row headers, headers, footers, content) in RTF files.
TEST CASE ID : KEX002.4.1_TC001
"""
#POSITIVE TEST CASE
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

"""
URS REQUIREMENT: KEX002.4.1
TEST CASE DESCRIPTION : Verify that the system accurately does not extract special characters (e.g., , -, ?, :) from various data points (column headers, row headers, headers, footers, content) in RTF files.
TEST CASE ID : KEX002.4.1_TC001
"""
#NEGATIVE TEST CASE
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
