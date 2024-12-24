def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
    except FileNotFoundError:
        print(f"Error: File '" + filename + "' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
# The 'with' statement ensures the file is closed automatically, even if errors occur.