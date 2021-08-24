from methods import *


if __name__ == '__main__':
    with open("encoded.txt") as file:
        encoded = file.read().replace("\n" , "")

    print(f"input: {encoded}")
    strings = get_key_lenght_text(encoded)
    decoded_strings = adecuated_string_to_decoded_strings(strings)
    decoded = reverse_decoded_strings(decoded_strings)


    with open("decoded.txt" , "w") as file:
        file.write(decoded)
    print(f"\noutput : {decoded}")

