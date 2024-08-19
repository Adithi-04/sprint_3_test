import os
import re
from data_extraction import special_characters
from user_Interface import selected_folder_path




#positive test case
def test_special_characters_positive():
    if __name__ == "__main__":
        valid_files = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        processed_content = special_characters(rtf_content)

                    # Log the processed content for debugging
                    logger.info(f"File {file_path}: Processed content = {processed_content}")

                    # Check if the content was processed without errors (basic sanity check)
                    assert processed_content != rtf_content, \
                        f"Error in file {file_path}: Content was not processed or unchanged."
                    valid_files.append(file_path)
                    logger.info(f"File {file_path}: Content processed successfully.")

                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")
                    
        for file in valid_files:
            try:
                content = open(file, 'r', encoding='utf-8').read()
                processed_content = special_characters(content)
                assert processed_content != content, \
                    f"File {file} should have processed content."
                logger.info(f"File {file}: Content processed successfully.")
            except Exception as e:
                logger.error(f"Failed to verify processed content in valid file {file}: {e}")
                assert False, f"Failed to verify processed content for file {file}."

#negative test case 

def test_special_characters_negative():
    if __name__ == "__main__":
        invalid_files = []

        # Process each RTF file in the selected folder
        for file_name in os.listdir(selected_folder_path):
            file_path = os.path.join(selected_folder_path, file_name)
            if os.path.isfile(file_path) and file_path.lower().endswith('.rtf'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        rtf_content = file.read()
                        processed_content = special_characters(rtf_content)

                    # Log the processed content for debugging
                    logger.info(f"File {file_path}: Processed content = {processed_content}")

                    # Check if the content remains unchanged (negative scenario)
                    if processed_content == rtf_content:
                        invalid_files.append(file_path)
                        logger.info(f"File {file_path}: No changes as expected.")

                except Exception as e:
                    logger.error(f"Failed to process file {file_path}: {e}")
                    invalid_files.append(file_path)

        for file in invalid_files:
            try:
                content = open(file, 'r', encoding='utf-8').read()
                processed_content = special_characters(content)
                assert processed_content == content, \
                    f"File {file} should not have processed content due to errors."
                logger.info(f"File {file}: No changes as expected.")
            except Exception as e:
                logger.error(f"Failed to verify absence of processing in invalid file {file}: {e}")
                assert False, f"Failed to verify absence of processing for file {file}."

