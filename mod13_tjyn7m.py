import unittest 

def test_symbol(self):
    self.assertTrue(test_symbol("AAP")) # Valid 
    self.assertTrue(test_symbol("TSL")) # Valid 
    self.assertFalse(test_symbol("asl")) # lowercase 
    self.assertFalse(test_symbol("1234123123")) # Long 
    self.assertFalse(test_symbol("M@l")) # invalid characters

def test_chart_type(self):
    self.assertTrue(test_chart_type("1")) # bar graph
    self.assertTrue(test_chart_type("2"))# line graph
    self.assertFalse(test_chart_type("3")) # invalid 
    self.assertFalse(test_chart_type("A")) # invalid 

def test_time_series(self):
    self.assertTrue(test_time_series("1")) 
    self.assertTrue(test_time_series("2"))
    self.assertTrue(test_time_series("3"))
    self.assertTrue(test_time_series("4"))
    self.assertFalse(test_time_series("5")) # Out of range
    self.assertFalse(test_time_series("A")) # Invalid Character

def test_start_date(self):
    self.assertTrue(test_start_date("2024-01-01"))
    self.assertFalse(test_start_date("01-01-2024")) # Incorrect format 
    self.assertFalse(test_start_date("2024-01-35")) # Invalid Date 
    self.assertFalse(test_start_date("womp-womp-bow")) # Not a date 

def test_end_date(self):
    self.assertTrue(test_end_date("2024-01-01"))
    self.assertFalse(test_end_date("01-01-2024")) # Incorrect format 
    self.assertFalse(test_end_date("2024-01-35")) # Invalid Date 
    self.assertFalse(test_end_date("womp-womp-bow")) # Not a date 

