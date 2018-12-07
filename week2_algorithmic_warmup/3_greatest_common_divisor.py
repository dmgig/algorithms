# Uses python3
import sys

def greatest_common_divisor_fast(a, b):
    aa = max(a, b)
    bb = min(a, b)
    if bb == 0:
        return aa
    divisor = aa % bb
    return greatest_common_divisor_fast(bb, divisor)

if __name__ == '__main__':
    input = sys.stdin.read();
    a, b = map(int, input.split())
    print(greatest_common_divisor_fast(a, b))
