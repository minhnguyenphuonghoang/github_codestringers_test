def input_data ():
    data = []
    while True:
        try:
            x = raw_input("Enter a number:")
            if x == "done":
                break
            data.append(float(x))
        
        except ValueError:
            print "Invalid number"
    return data

def split_array (array):
    final_array = [array[0], array[len(array)-1]]
    return final_array

if __name__ == "__main__":
    temp_array = []
    temp_array = input_data()
    temp_array = split_array(temp_array)
    print temp_array