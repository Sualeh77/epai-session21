# AdvancedNumber Class

The `AdvancedNumber` class is a custom implementation of a numeric type that extends the functionality of standard numbers in Python. It supports various arithmetic operations, comparisons, and custom behaviors such as string representation, formatting, and destruction notifications.

## Table of Contents

- [Initialization](#initialization)
- [Properties](#properties)
- [String Representation](#string-representation)
- [Arithmetic Operations](#arithmetic-operations)
- [Comparison Operations](#comparison-operations)
- [Hashing and Boolean Conversion](#hashing-and-boolean-conversion)
- [Callable Behavior](#callable-behavior)
- [Custom Formatting](#custom-formatting)
- [Destruction](#destruction)

## Initialization
```python
def __init__(self, number) -> None:
```
- **Parameters**: 
  - `number`: The initial value of the `AdvancedNumber` instance.
- **Description**: Initializes an instance of `AdvancedNumber` with the given number.

## Properties
```python
@property
def value(self):
```
- **Returns**: The current value of the `AdvancedNumber` instance.
- **Description**: A read-only property that provides access to the internal value.

## String Representation

### String Format (`__str__`)
```python
def __str__(self) -> str:
```
- **Returns**: A string in the format "Value: {value}"
- **Description**: Provides a human-readable string representation of the number.

### Representation (`__repr__`)
```python
def __repr__(self) -> str:
```
- **Returns**: A string in the format "AdvancedNumber({value})"
- **Description**: Provides a detailed string representation suitable for debugging.

## Arithmetic Operations

The class supports the following arithmetic operations:

- Addition (`+`): `__add__`, `__radd__`
- Subtraction (`-`): `__sub__`, `__rsub__`
- Multiplication (`*`): `__mul__`, `__rmul__`
- Division (`/`): `__truediv__`, `__rtruediv__`
- Modulo (`%`): `__mod__`, `__rmod__`

All operations work with both `AdvancedNumber` instances and regular numbers.

## Comparison Operations

Supports all standard comparison operations:

- Equal to (`==`): `__eq__`
- Less than (`<`): `__lt__`
- Greater than (`>`): `__gt__`
- Less than or equal to (`<=`): `__le__`
- Greater than or equal to (`>=`): `__ge__`
- Not equal to (`!=`): `__ne__`

## Hashing and Boolean Conversion

### Hash Function (`__hash__`)
```python
def __hash__(self) -> int:
```
- **Returns**: Hash value of the internal number
- **Description**: Makes `AdvancedNumber` instances usable as dictionary keys or set elements.

### Boolean Conversion (`__bool__`)
```python
def __bool__(self):
```
- **Returns**: `True` if the value is non-zero, `False` otherwise
- **Description**: Allows using `AdvancedNumber` instances in boolean contexts.

## Callable Behavior

### Call Method (`__call__`)
```python
def __call__(self):
```
- **Returns**: Square of the internal value
- **Description**: Makes instances callable, returning the square of their value.

## Custom Formatting

### Format Method (`__format__`)
```python
def __format__(self, format_spec: str) -> str:
```
- **Parameters**:
  - `format_spec`: Format specification string
- **Returns**: Formatted string representation of the value
- **Description**: Supports custom formatting using Python's format specification mini-language.

## Destruction

### Destructor (`__del__`)
```python
def __del__(self):
```
- **Description**: Prints a message when an instance is being destroyed by the garbage collector.

## Usage Examples

```python
# Creating instances
num1 = AdvancedNumber(10)
num2 = AdvancedNumber(5)

# Arithmetic operations
result = num1 + num2  # AdvancedNumber(15)
product = num1 * 2    # AdvancedNumber(20)

# Comparison
is_greater = num1 > num2  # True

# Callable behavior
squared = num1()  # 100

# Formatting
formatted = format(num1, ".2f")  # "10.00"
hex_format = format(num1, "#x")  # "0xa"

# Using in collections
number_set = {num1, num2}  # Set of unique values
```

## Testing

The class comes with a comprehensive test suite that verifies all functionality. Run the tests using pytest:

```bash
pytest test_advanced_number.py
```

The test suite covers:
- Initialization and property access
- String representation
- Arithmetic operations
- Comparison operations
- Hashing and set operations
- Boolean conversion
- Callable behavior
- Custom formatting
- Destruction notification