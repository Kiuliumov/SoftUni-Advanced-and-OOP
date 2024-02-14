def rectangle(length, height):
    if type(length) is int and type(height) is int:
        def area():
            return length * height
        def perimeter():
            return length + height + length + height
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    else:
        return 'Enter valid values!'
import unittest

class RectangleTests(unittest.TestCase):
   def test(self):
      result = rectangle('2', 10)
      self.assertEqual(result, "Enter valid values!")

if __name__ == "__main__":
   unittest.main()