from builtins import chr
import base64

def base_64_to_byte_array(base64_str):
    binary_string = base64.encode(base64_str);
    lenght = len(binary_string);

    result: int = [];
    for i in range(0,lenght):
        result.append(chr(binary_string[i]));

    return result;