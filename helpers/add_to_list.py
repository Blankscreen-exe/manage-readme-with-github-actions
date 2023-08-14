import argparse

def add_line(file_path, file_name, file_link):
    """
    Add a formatted line to a file containing a link with a user-friendly name.
    
    This function takes a file path, a file name, and a file link as input. The file name is
    formatted to enhance its readability by replacing underscores with spaces and capitalizing
    the first letter of each word. The formatted name is then used to create a markdown-style link
    with the provided file link. The formatted line is appended to the specified file, followed
    by a newline character.
    
    Parameters:
        file_path (str): The path to the file where the formatted line will be appended.
        file_name (str): The name of the file, which will be formatted for display.
        file_link (str): The URL or link associated with the file.
        
    Example:
        add_line('links.md', 'example_file.txt', 'https://example.com/files/example_file.txt')
        
    In the 'links.md' file, the following line will be appended:
        - [Example File](https://example.com/files/example_file.txt)
    """
    # check if the file link already exists in README
    with open(file_path, 'r') as fp:
        for l_no, line in enumerate(fp):
            # search string
            if file_link in line:
                print('link found in README')
                print('Line Number:', l_no)
                print('Line:', line)
                # don't look for next lines 
                return

    file_name = file_name.split(".")[0].replace("_", " ").title()
    
    text = f'- [{file_name}]({file_link})'
    
    with open(file_path, 'a') as file:
        # Append the line of file_name followed by a newline character
        file.write(text + '\n')
        
def main():
    parser = argparse.ArgumentParser(description="Append line to a file.")
    parser.add_argument("file_path", type=str, help="Path to the target file")
    parser.add_argument("file_name", type=str, help="String to append in the file")
    parser.add_argument("file_link", type=str, help="Link to the referred file")
    args = parser.parse_args()

    add_line(file_path=args.file_path, file_name=args.file_name, file_link=args.file_link)

if __name__ == "__main__":
    main()
