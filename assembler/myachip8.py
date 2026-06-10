from opcode_table import MNEMONIC_TABLE

"""

"""

class Chip8Assembler:
    def __init__(self, opcode_table = MNEMONIC_TABLE) -> None:
        self.labels = {}
        self.scanned = []
        self.resolved = []
        self.encoded = {}

        self.current_addr = 0x200

        self.opcode_table = opcode_table
    
    def scan(self, line: str) -> list | None:
        line = line.strip()

        if line == "" or line.startswith(';'):
            return None

        if line.endswith(':'):
            label = line[:-1].strip()

            self.labels[label] = self.current_addr
            return None

        if ':' in line:
            instruction, arguments = line.split(":", maxsplit=1)

            instruction = instruction.strip()
            arguments = arguments.strip().split()

        else:
            instruction = line
            arguments = []

        self.current_addr += 0x2

        self.scanned.append({
            "instruction": instruction,
            "args": arguments
        })

        return None
    
    def resolve(self):
        for item in self.scanned:
            instruction = item["instruction"]
            args = item["args"]

            new_args = []

            for arg in args:
                # If a arg is in the labels list, it's a lbel duuh
                # So we generate new args with the value of the label corrected
                if arg in self.labels:
                    new_args.append(self.labels[arg])
                else:
                    new_args.append(arg)
            
            self.resolved.append({
                "instruction": instruction,
                "args": new_args
            })

        return None
    
    def encode(self, instruction: str, args: list):
        opcode_info = self.opcode_table[instruction]

        opcode_base = opcode_info["opcode"]
        expected_args = opcode_info["args"]

        opcode = opcode_base

        for arg_type, arg_value in zip(expected_args, args):

            # -------------------------
            # REGISTER (0-F)
            # -------------------------
            if arg_type == "vx":
                arg_value = arg_value[1:]
                reg = int(arg_value, 16)
                opcode |= (reg << 8)

            elif arg_type == "vy":
                arg_value = arg_value[1:]
                reg = int(arg_value, 16)
                opcode |= (reg << 4)

            # -------------------------
            # BYTE (0-255 or 0xFF)
            # -------------------------
            elif arg_type == "byte":
                if isinstance(arg_value, str) and arg_value.startswith("0x"):
                    value = int(arg_value, 16)
                else:
                    value = int(arg_value)

                opcode |= (value & 0xFF)

            # -------------------------
            # ADDRESS (0x000 - 0xFFF)
            # -------------------------
            elif arg_type == "addr":
                if isinstance(arg_value, str):
                    if arg_value.startswith("0x"):
                        value = int(arg_value, 16)
                    else:
                        value = int(arg_value)
                else:
                    value = arg_value

                opcode |= (value & 0x0FFF)

            # -------------------------
            # NIBBLE (0-15)
            # -------------------------
            elif arg_type == "nibble":
                opcode |= (int(arg_value) & 0xF)

            else:
                raise ValueError(f"Unknown arg type: {arg_type}")

        return opcode.to_bytes(2, byteorder="big")

    def cycle_with_file(self, input_filename: str, output_filename: str):
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                self.scan(line)
        
        self.resolve()

        encoded_bytes = []
        
        for instruction in self.resolved:
            encoded_bytes.append(self.encode(instruction['instruction'], instruction['args']))

        with open(output_filename, 'wb') as output_file:
            for byte in encoded_bytes:
                output_file.write(byte)
        

if __name__=='__main__':

    ca = Chip8Assembler()

    print(ca.cycle_with_file('test.asm', 'test.ch8'))