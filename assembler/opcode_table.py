"""

Chip8 Opcode Table

Mnemonic = Opcode

"""

MNEMONIC_TABLE = {
    "CLS": {"opcode": 0x00E0, "args": []},

    "RET": {"opcode": 0x00EE, "args": []},

    "JP ADDR": {"opcode": 0x1000, "args": ["addr"]},

    "JP V0 ADDR": {
        "opcode": 0xB000,
        "args": ["addr"]
    },

    "CALL ADDR": {
        "opcode": 0x2000,
        "args": ["addr"]
    },

    "SE VX BYTE": {
        "opcode": 0x3000,
        "args": ["vx", "byte"]
    },

    "SE VX VY": {
        "opcode": 0x5000,
        "args": ["vx", "vy"]
    },

    "SNE VX BYTE": {
        "opcode": 0x4000,
        "args": ["vx", "byte"]
    },

    "SNE VX VY": {
        "opcode": 0x9000,
        "args": ["vx", "vy"]
    },

    "LD VX BYTE": {
        "opcode": 0x6000,
        "args": ["vx", "byte"]
    },

    "LD VX VY": {
        "opcode": 0x8000,
        "args": ["vx", "vy"]
    },

    "LD I ADDR": {
        "opcode": 0xA000,
        "args": ["addr"]
    },

    "LD VX DT": {
        "opcode": 0xF007,
        "args": ["vx"]
    },

    "LD VX K": {
        "opcode": 0xF00A,
        "args": ["vx"]
    },

    "LD DT VX": {
        "opcode": 0xF015,
        "args": ["vx"]
    },

    "LD ST VX": {
        "opcode": 0xF018,
        "args": ["vx"]
    },

    "LD F VX": {
        "opcode": 0xF029,
        "args": ["vx"]
    },

    "LD B VX": {
        "opcode": 0xF033,
        "args": ["vx"]
    },

    "LD I VX": {
        "opcode": 0xF055,
        "args": ["vx"]
    },

    "LD VX I": {
        "opcode": 0xF065,
        "args": ["vx"]
    },

    "ADD VX BYTE": {
        "opcode": 0x7000,
        "args": ["vx", "byte"]
    },

    "ADD VX VY": {
        "opcode": 0x8004,
        "args": ["vx", "vy"]
    },

    "ADD I VX": {
        "opcode": 0xF01E,
        "args": ["vx"]
    },

    "OR VX VY": {
        "opcode": 0x8001,
        "args": ["vx", "vy"]
    },

    "AND VX VY": {
        "opcode": 0x8002,
        "args": ["vx", "vy"]
    },

    "XOR VX VY": {
        "opcode": 0x8003,
        "args": ["vx", "vy"]
    },

    "SUB VX VY": {
        "opcode": 0x8005,
        "args": ["vx", "vy"]
    },

    "SUBN VX VY": {
        "opcode": 0x8007,
        "args": ["vx", "vy"]
    },

    "SHR VX": {
        "opcode": 0x8006,
        "args": ["vx"]
    },

    "SHL VX": {
        "opcode": 0x800E,
        "args": ["vx"]
    },

    "RND VX BYTE": {
        "opcode": 0xC000,
        "args": ["vx", "byte"]
    },

    "DRW VX VY NIBBLE": {
        "opcode": 0xD000,
        "args": ["vx", "vy", "nibble"]
    },

    "SKP VX": {
        "opcode": 0xE09E,
        "args": ["vx"]
    },

    "SKNP VX": {
        "opcode": 0xE0A1,
        "args": ["vx"]
    }
}