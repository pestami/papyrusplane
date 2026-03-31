import os

def postprocess_nc_files():
    
    # Tuncate lines from top of  *RAW.nc
    nTruncate=16
    # List of search and replacement strings
    replacements = [
        # FEED VELOCITIES G0 = rapid positioning
        ["G3 ", "G3 S1000 F500 "],
        ["G2 ", "G2 S1000 F500 "],
        ["G1 ", "G1 S1000 F500 "],
        ["G0 ", "G0 S0000 F1000 "],
        ["F60000.000", ""],
        # LASER ON
        
        #LASER OFF
             
        # REMOVE VERTICAL FEEDS
        ["Z-1.000", "Z0"],
        
        # Add more search and replacement pairs as needed
    ]
    sHeader='''
(======START=====================)
(Motion Modes:)
 (G0 [rapid positioning], )
 (G1 [linear interpolation], )
 (G2 [clockwise circular interpolation], )
 (G3 [counterclockwise circular interpolation])

(======CODE MANDATORY============)
M3 S0  (M03 – Spindle on in a clockwise)
(================================)


'''
    # Get the current directory
    current_dir = os.path.dirname(__file__)
    print(f"PCurrent Directory: {current_dir}")

    # Iterate through files in the current directory
    for filename in os.listdir(current_dir):
        # Check if the file matches the pattern {name}_RAW.NC
        if filename.endswith("_RAW.nc"):
            # Extract the file name without the extension
            name = os.path.splitext(filename)[0].replace("_RAW", "")

            # Open the file and read its content
            with open(os.path.join(current_dir, filename), 'r') as file:
                
                #content = file.read()
                lines = file.readlines()
                # Remove the first 10 lines
                content =sHeader+ ''.join(lines[nTruncate:])

            # Iterate through the search and replacement pairs
            for search, replace in replacements:
              content = content.replace(search, replace)
              print(f"SEARCH: {search} -> Replace:{replace}")

            # Save the modified content to a new file
            new_filename = f"{name}_POSTPROCESSED.NC"
            with open(os.path.join(current_dir, new_filename), 'w') as new_file:
                new_file.write(content)

            print(f"Processed file: {filename} -> {new_filename}")

if __name__ == "__main__":
    print('=====================================================')
    print('BEGIN')
    print('=====================================================')
    postprocess_nc_files()

