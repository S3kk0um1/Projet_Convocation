import re

def add_space_at_index(original_string, index_to_add_space):
    if index_to_add_space < 0 or index_to_add_space > len(original_string):
        return original_string  # Invalid index, return the original string unchanged

    # Create the new string with the added space at the specified index
    modified_string = original_string[:index_to_add_space] + ' ' + original_string[index_to_add_space:]
    return modified_string
def delete_words_regex(original_string, words_to_delete):
    # Create a regular expression pattern with all the words to be deleted
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_delete) + r')\b'
    return re.sub(pattern, '', original_string)
def delete_spaces(input_string):
    pattern = r'\s+'  # Regular expression pattern to match one or more spaces
    return re.sub(pattern, '', input_string)
def modify_letter(original_string, index_to_modify, new_letter):
    if index_to_modify < 0 or index_to_modify >= len(original_string):
        return original_string  # Invalid index, return the original string unchanged

    # Create the new string with the modified letter
    modified_string = original_string[:index_to_modify] + new_letter + original_string[index_to_modify + 1:]
    return modified_string
def delete_before_character(input_string, character):
    pattern = re.escape(character)  # Escape the character in case it's a special regex character
    return re.sub(r'^.*?' + pattern, '', input_string)
