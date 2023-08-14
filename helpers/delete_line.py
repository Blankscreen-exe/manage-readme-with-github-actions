import argparse

def delete_matching_lines(file_path, search_string, count=0):
    """
    Delete lines containing a specified search string from a file.
    
    This function reads the content of the specified file and searches for lines
    containing the given search string. Depending on the value of the 'count'
    parameter, it performs different actions:
    
    - If 'count' is 0 or positive:
      Deletes all occurrences of lines containing the search string, or only the first 'count'
      occurrences if 'count' is greater than 0.
      
    - If 'count' is negative:
      Deletes the last 'abs(count)' occurrences of lines containing the search string.
    
    The modified content is then written back to the file, effectively removing the
    specified lines. The function provides feedback on the number of removed lines.
    
    Parameters:
        file_path (str): The path to the file from which lines will be deleted.
        search_string (str): The string to search for within the file's lines.
        count (int, optional): The count of lines to delete. Positive values delete from
            the start, negative values delete from the end. Default is 0 (delete all).
            
    Example:
        delete_matching_lines('data.txt', 'obsolete', count=3)
        
    This will remove the last 3 lines containing the word 'obsolete' from 'data.txt'.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        deleted_count = 0
        

        with open(file_path, 'w') as file:
        
            if count >= 0:
                # scenario to delete all or numbered instances in forward direction
                for line in lines:
                    if count == 0:
                        # if count is 0 then delete all occurences
                        if search_string not in line:
                            file.write(line)
                        else:
                            deleted_count += 1
                    else:
                        # if count is some value other than 0 then 
                        if search_string in line and deleted_count < count:
                            deleted_count += 1
                        else:
                            file.write(line)
            else: 
                # scenario to delete numbered instances in reverse direction
                deleted_count = 0
                reversed_lines = list(reversed(lines))
                new_lines = []
                
                for line in reversed_lines:
                    if search_string in line and deleted_count < abs(count):
                        deleted_count += 1
                    else:
                        new_lines.append(line)
                
                with open(file_path, 'w') as file:
                    for line in reversed(new_lines):
                        file.write(line)

        print(f"{deleted_count} line(s) containing '{search_string}' removed from {file_path}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Delete lines containing a specific string from a file.")
    parser.add_argument("search_string", type=str, help="String to search for in the file")
    parser.add_argument("file_path", type=str, help="Path to the target file")
    parser.add_argument("-c", "--count", type=int, default=0, help="Maximum number of matching lines to delete (default: 0)")
    args = parser.parse_args()

    delete_matching_lines(args.file_path, args.search_string, args.count)

if __name__ == "__main__":
    main()
