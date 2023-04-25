# Open the file for reading
# Open the original file for reading
with open("script/cutVer.txt", "r") as f:
    # Read the text from the file
    text = f.read()
    # Split the text by periods
    segments = text.split('.')
    # Open the output file for writing
    with open("script/final.txt", "w") as output_file:
        # Write each segment to a new line in the output file
        for segment in segments:
            output_file.write(segment.strip() + '\n')





