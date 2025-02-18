import unittest
from ICE3.src.temperature_sensor import validate_temp, temp_process

class TestTemperatureSensor(unittest.TestCase):

    def test_validate_temp_empty(self):
        with self.assertRaises(ValueError) as context:
            validate_temp("")
        self.assertEqual(str(context.exception), "Error: No input provided.")

    def test_validate_temp_out_of_bounds_high(self):
        with self.assertRaises(ValueError) as context:
            validate_temp("151")
        self.assertEqual(str(context.exception), "Error: Out-of-bound value detected.")

    def test_validate_temp_out_of_bounds_low(self):
        with self.assertRaises(ValueError) as context:
            validate_temp("-51")
        self.assertEqual(str(context.exception), "Error: Out-of-bound value detected.")

    def test_validate_temp_invalid_string(self):
        with self.assertRaises(ValueError) as context:
            validate_temp("abc")
        self.assertEqual(str(context.exception), "Error: Invalid input detected.")

    def test_temp_process_valid_single(self):
        temps = ["20"]
        expected = "Min: 20.0°C, Max: 20.0°C, Avg: 20.0°C"
        self.assertEqual(temp_process(temps), expected)

    def test_temp_process_valid_two(self):
        temps = ["15", "35"]
        expected = "Min: 15.0°C, Max: 35.0°C, Avg: 25.0°C"
        self.assertEqual(temp_process(temps), expected)

    def test_temp_process_valid_three(self):
        temps = ["10", "-10", "30"]
        expected = "Min: -10.0°C, Max: 30.0°C, Avg: 10.0°C"
        self.assertEqual(temp_process(temps), expected)

    def test_temp_process_valid_four(self):
        temps = ["-50", "20", "150", "25"]
        expected = "Min: -50.0°C, Max: 150.0°C, Avg: 36.25°C"
        self.assertEqual(temp_process(temps), expected)

    def test_temp_process_invalid_via_validate_temp(self):
        self.assertEqual(temp_process(["10", "abc", "30"]), "Error: Invalid input detected.")

    def test_temp_process_long_integers_via_validate_temp(self):
        self.assertEqual(temp_process(["2**31 - 1", "-2**31"]), "Error: Invalid input detected.")

    def test_temp_process_valid_same(self):
        temps = ["10", "10", "10"]
        expected = "Min: 10.0°C, Max: 10.0°C, Avg: 10.0°C"
        self.assertEqual(temp_process(temps), expected)

    def test_temp_process_mixed_valid_invalid_via_validate_temp(self):
        self.assertEqual(temp_process(["34", "-12", "hi", "121"]), "Error: Invalid input detected.")

    def test_temp_process_valid_negative(self):
        temps = ["-30", "150", "79"]
        expected = "Min: -30.0°C, Max: 150.0°C, Avg: 66.33°C"
        self.assertEqual(temp_process(temps), expected)

    def test_temp_process_out_of_bounds_via_validate_temp(self):
        self.assertEqual(temp_process(["-51", "151"]), "Error: Out-of-bound value detected.")

    def test_temp_process_special_chars_mixed_via_validate_temp(self):
        self.assertEqual(temp_process(["!#$s", "40", "-40", "-39"]), "Error: Invalid input detected.")

if __name__ == "__main__": # pragma: no cover
    unittest.main()