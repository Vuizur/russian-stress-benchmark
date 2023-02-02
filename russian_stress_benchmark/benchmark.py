import os


def benchmark_everything_in_folder(input_folder: str, output_folder: str, stress_function: callable):
    # Iterate over all txt files, also in subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".txt"):
                # Open file
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    # Read file
                    text = f.read()
                    # Run stress function
                    stressed_text = stress_function(text)
                    # Write result to output file
                    with open(os.path.join(output_folder, file), "w", encoding="utf-8") as f:
                        f.write(stressed_text)
                        