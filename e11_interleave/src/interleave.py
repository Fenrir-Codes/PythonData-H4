#!/usr/bin/env python3

def interleave(*lists):
    list = []
    for i in zip(*lists):
        list.extend(i)
    return list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
