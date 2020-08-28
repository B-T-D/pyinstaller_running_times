"""Return a Python dictionary containing inputted results in the standard
format."""

def txt_to_dict(filename: str) -> dict:
    """
    Args:
        filename (str): Name of a txt file, including the file extension.
    """
    results_dict = {}
    fobj = open(filename, mode='r')
    for line in fobj:
        line = line.rstrip() # strip extra newline characters
        tokens = line.split(sep=":") # number before the colon is the key
        key = int(tokens[0])
        value = float(tokens[1].lstrip()) # strip leading whitespaces
        results_dict[key] = value

    #assert len(results_dict) == n # good to check against whitespace messups
                                    # but will need to pass in n.

                                    # This prob supports doing a wider class
                                    #   with n as an attribute.
    return results_dict

def main():
    filename = "results pure C.txt"
    c_results = txt_to_dict(filename)
    print(f"c_results dict used n={len(c_results)}")

if __name__ == '__main__':
    main()
    
