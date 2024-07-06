import sys
import subprocess

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 add_output_as_comment.py <filename.py>")
        sys.exit(1)

    # Get the filename from command line arguments
    filename = sys.argv[1]

    # Execute the Python file and capture the output
    try:
        output = subprocess.check_output(["python3", filename], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {filename}: {e.output}")
        sys.exit(1)

    # Read the contents of the file
    with open(filename, 'r') as file:
        file_content = file.read()

    # Write the output as comments at the end of the file
    with open(filename, 'a') as file:
        file.write("\n\n# Output from execution:\n")
        file.write("# " + output.replace("\n", "\n# "))

    print("Output added as comments to", filename)

if __name__ == "__main__":
    main()
