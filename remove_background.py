import rembg

input_path = "" #path to your input file

output_path = "" #path to your output file

try:
    with open(input_path, "rb") as i:
        with open(output_path, "wb") as o:
            input_file = i.read()
            output_file = rembg.remove(input_file)
            o.write(output_file)
            print("Done!")

except Exception as e:
    print(e)


"""
This is a ready-to-use code snippet.
"""