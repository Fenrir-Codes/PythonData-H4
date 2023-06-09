#!/usr/bin/env python3
import re #re for regular expressions

def integers_in_brackets(s):
    pattern = r"\[\s*([+-]?\d+)\s*\]"
    L = re.findall(pattern, s)
    L = [int(n) for n in L]

    return L

def main():
    print(integers_in_brackets("  afd [asd] [12] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
