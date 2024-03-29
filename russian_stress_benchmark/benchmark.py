import os
from typing import Callable
from stressed_cyrillic_tools import unaccentify, remove_yo


def benchmark_everything_in_folder(input_folder: str, output_folder: str, stress_function: Callable[[str], str], rmv_yo: bool = False) -> None:
    # Iterate over all txt files, also in subfolders
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".txt") or file.endswith(".ref"):
                # Open file
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    # Subtract the input folder from the root path to get the relative path
                    relative_path = os.path.relpath(root, input_folder)
                    # Read file
                    text = f.read()

                    if rmv_yo:
                        text = unaccentify(remove_yo(text))
                    else:
                        text = unaccentify(text)

                    # Run stress function
                    stressed_text = stress_function(text)
                    output_path = os.path.join(
                        output_folder, relative_path, file)
                    # Create output path if it doesn't exist
                    if not os.path.exists(os.path.dirname(output_path)):
                        os.makedirs(os.path.dirname(output_path))
                    # Write result to output file
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(stressed_text)
