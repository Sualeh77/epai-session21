from typing import Any


class AdvancedNumber:
    def __init__(self, number) -> None:
        self._value = number

    @property
    def value(self):
        return self._value

    def __str__(self) -> str:
        return f"Value: {self.value}"

    def __repr__(self) -> str:
        return f"AdvancedNumber({self.value})"
    
    def __add__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value + other.value)
        else:
            return AdvancedNumber(self.value + other)
        
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value - other.value)
        else:
            return AdvancedNumber(self.value - other)
        
    def __rsub__(self, other):
        if isinstance(other, AdvancedNumber):
            return  AdvancedNumber(other.value - self.value)
        else:
            return AdvancedNumber(other - self.value)
        
    def __mul__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value * other.value)
        else:
            return AdvancedNumber(self.value * other)
        
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value / other.value)
        else:
            return AdvancedNumber(self.value / other)
        
    def __rtruediv__(self, other):
        if isinstance(other, AdvancedNumber):
            return  AdvancedNumber(other.value / self.value)
        else:
            return AdvancedNumber(other / self.value)
        
    def __mod__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value % other.value)
        else:
            return AdvancedNumber(self.value % other)
        
    def __rmod__(self, other):
        if isinstance(other, AdvancedNumber):
            return  AdvancedNumber(other.value % self.value)
        else:
            return AdvancedNumber(other % self.value)
        
    def __eq__(self, other) -> bool:
        if isinstance(other, AdvancedNumber):
            return  self.value == other.value
        else:
            return self.value == other
        
    def __lt__(self, other) -> bool:
        if isinstance(other, AdvancedNumber):
            return self.value < other.value
        else:
            return self.value < other
        
    def __gt__(self, other) -> bool:
        if isinstance(other, AdvancedNumber):
            return self.value > other.value
        else:
            return self.value > other
        
    def __le__(self, other) -> bool:
        if isinstance(other, AdvancedNumber):
            return self.value <= other.value
        else:
            return self.value <= other
        
    def __ge__(self, other) -> bool:
        if isinstance(other, AdvancedNumber):
            return self.value >= other.value
        else:
            return self.value >= other
        
    def __ne__(self, other) -> bool:
        if isinstance(other, AdvancedNumber):
            return  self.value != other.value
        else:
            return self.value != other
        
    def __hash__(self) -> int:
        return hash(self.value)
        
    def __bool__(self):
        return bool(self.value)
    
    def __call__(self):
        return self.value**2
    
    def __format__(self, format_spec: str) -> str:
        return format(self.value, format_spec)
    
    def __del__(self):
        print(f"AdvancedNumber with value {self.value} is being destroyed")
    