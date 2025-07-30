# Scientific Calculator

A comprehensive scientific calculator built with Python and tkinter, featuring a sleek modern UI and all essential scientific functions.

## Features

### Basic Operations
- Addition, subtraction, multiplication, division
- Clear (C) and Clear Entry (CE) functions
- Backspace functionality
- Negative/positive toggle (±)

### Scientific Functions
- **Trigonometric Functions**: sin, cos, tan
- **Inverse Trigonometric**: asin, acos, atan
- **Logarithmic Functions**: ln (natural log), log (base 2), log10 (base 10)
- **Exponential Functions**: e^x, 10^x, 2^x
- **Power Functions**: x^2, x^y, √ (square root)
- **Other Functions**: 1/x (reciprocal), |x| (absolute value), n! (factorial)

### Constants
- π (pi)
- e (Euler's number)

### Memory Functions
- MC (Memory Clear)
- MR (Memory Recall)
- M+ (Memory Add)
- M- (Memory Subtract)

### Advanced Features
- **Angle Mode Toggle**: Switch between DEG (degrees) and RAD (radians)
- **Keyboard Support**: Full keyboard input support
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Modern UI**: Dark theme with color-coded buttons

## Installation

1. Ensure you have Python 3.x installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the calculator:
```bash
python scientific_calculator.py
```

### Keyboard Shortcuts
- **Numbers**: 0-9, decimal point (.)
- **Operators**: +, -, *, /
- **Enter/Return**: Calculate result
- **Escape**: Clear all
- **Backspace**: Delete last character

### How to Use

1. **Basic Calculations**: Enter numbers and operators, press = or Enter
2. **Scientific Functions**: Enter a number, then press the function button
3. **Memory Operations**: Use M+, M-, MR, MC buttons for memory operations
4. **Angle Mode**: Toggle between degrees and radians using the DEG/RAD button

## Examples

- **Basic**: `2 + 3 × 4 = 14`
- **Trigonometric**: Enter `30`, press `sin` (in DEG mode) = `0.5`
- **Logarithmic**: Enter `100`, press `log10` = `2`
- **Exponential**: Enter `2`, press `e^x` = `7.3890560989306495`
- **Power**: Enter `4`, press `x^2` = `16`

## Technical Details

- **Framework**: tkinter (Python's standard GUI library)
- **Architecture**: Object-oriented design with modular button creation
- **Error Handling**: Try-catch blocks for all mathematical operations
- **UI Design**: Modern dark theme with intuitive color coding

## Features Overview

| Category | Functions |
|----------|-----------|
| Basic | +, -, ×, ÷, C, CE, ⌫, ± |
| Trigonometric | sin, cos, tan, asin, acos, atan |
| Logarithmic | ln, log, log10 |
| Exponential | e^x, 10^x, 2^x |
| Power | x^2, x^y, √ |
| Other | 1/x, \|x\|, n! |
| Constants | π, e |
| Memory | MC, MR, M+, M- |
| Mode | DEG/RAD toggle |

The calculator provides a professional-grade scientific computing experience with an intuitive interface suitable for students, engineers, and scientists.