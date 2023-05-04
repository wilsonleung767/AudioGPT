
# Split the script into parts according to chunk_size
def split_text_to_list(filename, chunk_size):
    with open(filename, "r") as file:
        text = file.readline()

    splitted_text_list = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return splitted_text_list

text = split_text_to_list('script\podcast\podcast_A0_S0.txt',3000)

print(text)
