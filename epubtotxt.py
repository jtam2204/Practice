import os
import glob
from ebooklib import epub
from bs4 import BeautifulSoup
from tkinter import Tk, filedialog

def extract_text_from_epub(epub_path, txt_path):
    try:
        # Read the EPUB file
        book = epub.read_epub(epub_path)
        
        # Initialize an empty string to store the extracted text
        text = ""

        # Iterate over each item in the EPUB file
        for item in book.get_items():
            # Check if the item is a document
            if item.get_type() == 9:
                # Parse the document content with BeautifulSoup
                soup = BeautifulSoup(item.get_body_content(), 'html.parser')
                # Extract and accumulate the text content
                text += soup.get_text(separator='\n')
        
        # Write the extracted text to a TXT file
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

    except Exception as e:
        print(f"An error occurred while processing {epub_path}: {e}")

def convert_epubs_in_folder(folder_path):
    # Find all EPUB files in the specified folder
    epub_files = glob.glob(os.path.join(folder_path, '*.epub'))
    
    # Iterate over each EPUB file
    for epub_file in epub_files:
        # Define the output TXT file path
        txt_file = os.path.splitext(epub_file)[0] + '.txt'
        # Extract text and save it to the TXT file
        extract_text_from_epub(epub_file, txt_file)
        print(f"Converted {epub_file} to {txt_file}")

def select_folder_and_convert():
    # Create a Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select a folder
    folder_path = filedialog.askdirectory()
    
    if folder_path:
        # Convert all EPUB files in the selected folder
        convert_epubs_in_folder(folder_path)
    else:
        print("No folder selected")

# Example usage
if __name__ == "__main__":
    select_folder_and_convert()
