import unittest
class TestHexCalc(unittest.TestCase):
    def test_hex_to_binary(self):
        self.assertEqual(convert_hex_to_binary('2FFFF'), '101111111111111111')
    def test_binary_to_hex(self):
        self.assertEqual(convert_binary_to_hex('101111111111111111'), '2ffff')
    def test_binary_ones_complement(self):
        self.assertEqual(str(binary_ones_complement('101111111111111111')), '10000000000000000')
    def test_binary_twos_complement(self):
        self.assertEqual(str(binary_twos_complement('101111111111111111')), '10000000000000001')
    def add_in_binary(self):
        self.assertEqual(add_in_binary('1011', '1011'), '10110')
    def subtract_in_binary(self):
        self.assertEqual(subtract_in_binary('1011', '1011'), '0')
    
def hex_chart():
    hex_chart = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                 '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                 '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    return hex_chart
def convert_hex_to_binary(hex_num):
    return bin(int(hex_num, 16))[2:]
def convert_binary_to_hex(binary_num):
    return hex(int(binary_num, 2))[2:]

def binary_ones_complement(binary_num):
    binary_num = str(binary_num)
    new = binary_num.replace('0', 'x').replace('1', '0').replace('x', '1')
    return int(new)

def binary_twos_complement(binary_num):
    length = len((binary_num))
    binary_num = str(binary_ones_complement(binary_num))
    print('1 complement:', binary_num.zfill(length))
    binary_num = add(binary_num, '1')
    print('2 complement:', binary_num.zfill(length))
    return binary_num

def add(binary_num1, binary_num2):
    return bin(int(binary_num1, 2) + int(binary_num2, 2))[2:]

def subtract(binary_num1, binary_num2):
    return bin(int(binary_num1, 2) - int(binary_num2, 2))[2:]

def add_in_binary(binary_num1, binary_num2):
    ans = int(binary_num1) + int(binary_num2)
    ans = carry(str(ans), '+',)
    return ans
 
def subtract_in_binary(binary_num1, binary_num2):
    length = max(len(binary_num1), len(binary_num2))
    binary_num1 = binary_num1.zfill(length)
    binary_num2 = binary_num2.zfill(length)
    print(f'{binary_num1} - {binary_num2}')
    ans = int(binary_num1) + int(binary_twos_complement(binary_num2))
    ans = carry(str(ans), '-')
    return ans

def twos_complement_to_binary(binary_num):
    if binary_num[0] == '1':
        sign = '-'
        binary_num = binary_twos_complement(binary_num)
    else:
        sign = ''
        binary_num = binary_num
    print(f'{sign}{binary_num}')

def carry(binary_num1, operation):
    carry = False
    new_binary_num1 = ''
    for i in reversed(binary_num1):
        if carry == True:
            i = ord(i)+1
            i = chr(i)
        if i == '0':
            new_binary_num1 += '0'
            carry = False
        if i == '1':
            new_binary_num1 += '1'
            carry = False
        if i == '2':
            new_binary_num1 += '0'
            carry = True
        elif i == '3':
            new_binary_num1 += '1'
            carry = True
        else:
            carry = False
    if carry == True and operation == '+':
        new_binary_num1 += '1'
    if (carry == True) and (operation == '-') and (overflow == True):
       print('Overflow value: 1')
       new_binary_num1 = new_binary_num1[:-1]
    return new_binary_num1[::-1]

def binary_to_decimal(binary_num):
    return int(binary_num, 2)

if __name__ == '__main__':
    base = '2'
    global overflow
    overflow = False
    while True:
        print(f'''Choose a mode:
              1. Add
              2. Subtract
              3. Change base (current base is {base})
              4. Convert hex to binary
              5. Convert binary to hex
              6. View Hex Chart
              7. Exit 
              8. Toggle overflow (for subtraction, if seeing overflow is desired)
              9. Run Tests
              ''')
        mode = input('Enter a mode: ')
        if mode == '1':
            if base == '2':
                UserIn1 = input('Enter a binary number: ')
                UserIn2 = input('Enter another binary number: ')
            elif base == '16':
                UserIn1 = input('Enter a hex number: ')
                UserIn2 = input('Enter another hex number: ')
                UserIn1 = convert_hex_to_binary(UserIn1)
                UserIn2 = convert_hex_to_binary(UserIn2)
                print(f"Convert to binary: Input1 = {UserIn1}, Input2 = {UserIn2}")
            ans = add_in_binary(UserIn1, UserIn2)
            decimal = binary_to_decimal(ans)
            print("Binary form:", ans)
            if base == '16':
                ans = convert_binary_to_hex(ans)
                print("Hex form:", ans)
            print("Decimal form:", decimal)
        elif mode == '2':
            if base == '2':
                UserIn1 = input('Enter a binary number: ')
                UserIn2 = input('Enter another binary number: ')
            elif base == '16':
                UserIn1 = input('Enter a hex number: ')
                UserIn2 = input('Enter another hex number: ')
                UserIn1 = convert_hex_to_binary(UserIn1)
                UserIn2 = convert_hex_to_binary(UserIn2)
                print(f"Convert to binary: Input1 = {UserIn1}, Input2 = {UserIn2}")
            ans = subtract_in_binary(UserIn1, UserIn2)
            print("2s complement form:", ans)
            if base == '16':
                hex = convert_binary_to_hex(ans)
                print("Hex 2s complement form:", hex)
            print("Convert to normal form:")
            (twos_complement_to_binary(ans))
            

        elif mode == '3':
            base = input('Enter a base: ')
            base = str(base)
        elif mode == '4':
            hex_num = input('Enter a hex number: ')
            converted = convert_hex_to_binary(hex_num)
            print(converted)
            #make sure it works by converting back to user input
            assert convert_binary_to_hex(converted) == hex_num
        elif mode == '5':
            binary_num = input('Enter a binary number: ')
            converted = convert_binary_to_hex(binary_num)
            print(converted)
            #make sure it works by converting back to user input
            assert convert_hex_to_binary(converted) == binary_num
        elif mode == '6':
            print(hex_chart())
        elif mode == '7':
            exit()
        elif mode == '8':
            overflow = input(f'Would you like to see overflow? (y/n), currently {overflow}')
            if overflow == 'y':
                overflow = True
            elif overflow == 'n':
                overflow = False
            else:
                print('Invalid input. Please try again.')
        elif mode == '9':
            unittest.main()
        else:
            print('Invalid mode. Please try again.')
    