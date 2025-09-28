def EnL(n):
    """Converts a number to its English word representation."""
    if not isinstance(n, int) or n < 0:
        if isinstance(n, str):
            if n == "":
                m = "   You did not enter anything!"
            else:
                m = f"   '{n}' is a string, not a positive integer!"
        elif isinstance(n, float):
            m = f"   {n} is a float, not a positive integer!"
        elif n < 0:
            m = f"   {n} is a negative number, not a positive integer!"
        return m

    if n == 0:
        return "   0 = zero"

    T1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    T2 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    T3 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    T5 = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']

    num_str = str(n)
    groups = []
    while len(num_str) > 0:
        groups.append(num_str[-3:])
        num_str = num_str[:-3]

    words = []
    for i, group_str in enumerate(groups):
        group_int = int(group_str)
        if group_int == 0:
            continue

        group_words = []
        hundreds = group_int // 100
        tens_units = group_int % 100

        if hundreds > 0:
            group_words.append(T1[hundreds])
            group_words.append('hundred')

        if tens_units > 0:
            if hundreds > 0:
                group_words.append('and')

            if tens_units < 10:
                group_words.append(T1[tens_units])
            elif tens_units < 20:
                group_words.append(T2[tens_units - 10])
            else:
                tens = tens_units // 10
                units = tens_units % 10
                if units > 0:
                    group_words.append(f"{T3[tens]}-{T1[units]}")
                else:
                    group_words.append(T3[tens])

        if i > 0:
            group_words.append(T5[i])

        words.insert(0, ' '.join(group_words))

    if len(words) > 1 and 'hundred' not in words[-1]:
        words.insert(len(words) - 1, 'and')

    result = ' '.join(words).replace(' -', '-').replace('  ', ' ').strip()
    return f"   {n} = {result}"

if __name__ == "__main__":
    r = 'y'
    while r.lower() == 'y':
        a = input("Enter the number to convert to words (positive integer): ")
        try:
            val = int(a)
            print(EnL(val))
        except ValueError:
            try:
                val = float(a)
                print(EnL(val))
            except ValueError:
                print(EnL(str(a)))

        r = input("Do you want to enter another number? ('y' or 'n') ")

    q = input("Press 'Enter' to exit")