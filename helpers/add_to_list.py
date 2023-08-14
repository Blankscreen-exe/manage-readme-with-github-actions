import argparse

def add_line(file_path, file_name, file_link):
    
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
