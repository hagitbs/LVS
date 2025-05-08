import csv

def unpivot_csv_long(input_csv_file, output_txt_file):
    """
    Unpivots a CSV file with a specified structure to a long format
    with 'ELEMENT', 'DOCUMENT', and 'VALUE' columns.

    Args:
        input_csv_file (str): Path to the input CSV file.
        output_txt_file (str): Path to the output text file.
    """
    try:
        with open(input_csv_file, 'r', newline='') as infile, \
             open(output_txt_file, 'w') as outfile:
            reader = csv.reader(infile)
            header = next(reader)  # Read the header row (C1...C10)

            if not header:
                print("Error: CSV file is empty or has no header.")
                return

            outfile.write("ELEMENT\tDOCUMENT\tVALUE\n")  # Write the output header

            row_index = 1
            for row in reader:
                element = f"I{row_index}"
                for col_index, value in enumerate(row):
                    document = header[col_index]
                    outfile.write(f"{element}\t{document}\t{value}\n")
                row_index += 1

        print(f"Successfully unpivoted '{input_csv_file}' to '{output_txt_file}' in long format.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    input_csv = 'data/bio/GSE164999_edited.csv'  # Replace with your input CSV file name
    output_txt = 'data/bio/GSE164999_edited_unpivot.csv' # Replace with your desired output text file name
    unpivot_csv_long(input_csv, output_txt)