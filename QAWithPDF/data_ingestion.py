from llama_index.core import SimpleDirectoryReader
import os

def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:

        # Save the uploaded file temporarily
        file_path = "temp_uploaded_file.pdf"  # Temporary file name
        with open(file_path, "wb") as f:
            f.write(data.getbuffer())

        # Assuming SimpleDirectoryReader can work with a single file by creating a directory
        os.makedirs("temp_dir", exist_ok=True)  # Create a temporary directory
        os.rename(file_path, os.path.join("temp_dir", file_path))  # Move the file to the directory

        # Now load the document from the temporary directory
        loader = SimpleDirectoryReader("temp_dir")
        documents = loader.load_data()

        # Clean up: Remove the temporary directory and file
        os.remove(os.path.join("temp_dir", file_path))
        os.rmdir("temp_dir")

        return documents
    except Exception as e:
        print(e)


    