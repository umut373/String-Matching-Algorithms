import datetime

def generate_bad_symbol_table() :
    for i in range(p_length-1) :
        bad_symbol[pattern[i]] = p_length - i - 1


def generate_good_suffix_table() :
    i = p_length 
    j = p_length + 1
    bpos = [0] * (p_length + 1)
    bpos[i] = j

    while i > 0 :
        while j <= p_length and pattern[i-1] != pattern[j-1] :
            if good_suffix[p_length-j] == 0 :
                good_suffix[p_length-j] = j - i

            j = bpos[j]
        
        i -= 1
        j -= 1
        bpos[i] = j


    j = bpos[0]
    for i in range(p_length  + 1) :
        if good_suffix[p_length-i] == 0 :
            good_suffix[p_length-i] = j

        if i == j :
            j = bpos[j]

    good_suffix[p_length] = p_length


def search() :
    i = 0
    while i < (t_length - p_length) :
        count = 0
        for j in range(p_length) :
            t_ch = text[p_length+i-j-1]
            p_ch = pattern[p_length-j-1]
            if t_ch ==  p_ch :
                count += 1
            else :
                d1 = max((bad_symbol.get(t_ch, p_length) - count), 1)
                d2 = good_suffix[count]
                i += max(d1, d2) - 1
                break

        if count == p_length :
            output = text[:i] + "<MARK>" + pattern + "</MARK>" + text[i+p_length:]
            output_file.write(output)
            i += good_suffix[p_length] - 1
            
        i += 1

    output_file.close()
   

def print_tables() :
    print("-----Bad Symbol Table-----")
    for element in bad_symbol :
        print(element, end = ' -> ')
        print(bad_symbol[element])
    print("* ->", p_length, "\n")

    print("-----Good Suffix Table-----")
    print("k     shift")
    for i in range(p_length+1) :
        print(i, end = '\t')
        print(good_suffix[i])



if __name__ == "__main__" :
    input_file = open("input.html", "r")
    output_file = open("output.html", "w")

    text = input_file.readline() 
    input_file.close()
    pattern = input("Enter a pattern: ")

    t_length = len(text)
    p_length = len(pattern)

    bad_symbol = {}
    good_suffix = [0] * (p_length + 1)

    generate_bad_symbol_table()
    generate_good_suffix_table()

    print_tables()

    start_time = datetime.datetime.now()
    search()
    exec_time = datetime.datetime.now() - start_time
    print("Execution time is", exec_time.microseconds)