Você pode colocar algo assim no README:

````markdown
# Chip8 Assembler made with Python

It's a simple assembler for a custom Chip-8 assembly language made by me.

## Syntax

Instructions are written using the following format:

```text
INSTRUCTION: ARG1 ARG2 ARG3
````

Examples:

```text
CLS
RET

LD VX BYTE: V0 10
LD VX BYTE: V1 20

ADD VX VY: V0 V1

JP ADDR: loop

loop:
    DRW VX VY NIBBLE: V0 V1 5
```

## Labels

Labels mark memory locations and can be used as jump targets.

```text
loop:
    ADD VX VY: V1 V2
    JP ADDR: loop
```

The assembler automatically resolves labels to their correct memory addresses.

## Argument Types

| Type     | Description                             | Examples                |
| -------- | --------------------------------------- | ----------------------- |
| `vx`     | Chip-8 register X                       | `V0`, `V1`, `VA`, `VF`  |
| `vy`     | Chip-8 register Y                       | `V0`, `V1`, `VA`, `VF`  |
| `byte`   | 8-bit value (decimal or hexadecimal)    | `10`, `255`, `0xFF`     |
| `addr`   | Memory address (decimal or hexadecimal) | `512`, `0x200`, `0xABC` |
| `nibble` | 4-bit value (0-15)                      | `0`, `5`, `15`          |

## Examples

### Load a value into a register

```text
LD VX BYTE: V0 42
```

### Add two registers

```text
ADD VX VY: V1 V2
```

### Jump to a label

```text
start:
    CLS
    JP ADDR: start
```

### Draw a sprite

```text
DRW VX VY NIBBLE: V0 V1 5
```

## Assembly Process

The assembler works in three phases:

1. **Scan**

   * Reads instructions and collects labels.

2. **Resolve**

   * Replaces label references with memory addresses.

3. **Encode**

   * Converts instructions into Chip-8 machine code.

Output is generated as a `.ch8` binary file ready to run in a Chip-8 emulator.
