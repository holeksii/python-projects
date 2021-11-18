import unittest
from Patterns.Memento import Memento

class TestMemento(unittest.TestCase):
    
    
    def test__init__(self):
        m = Memento()
        self.assertEqual(m.conditions, [])
        self.assertEqual(m.index, -1)
        
    def test_add_condition(self):
        m = Memento()
        m.add_condition((1, 2, 3, 4, 5))
        m.add_condition((5, 4, 3, 2, 1))
        self.assertEqual(m.conditions, [(1, 2, 3, 4, 5), (5, 4, 3, 2, 1)])
        self.assertEqual(m.index, 1)
        
        
    def test_top_index(self):
        m = Memento()
        m.add_condition((1, 2, 3, 4, 5))
        m.add_condition((5, 4, 3, 2, 1))
        self.assertEqual(m.top_index(), 1)
        
        
    def test_top_condition(self):
        m = Memento()
        m.add_condition((1, 2, 3, 4, 5))
        m.add_condition((5, 4, 3, 2, 1))
        self.assertEqual(m.top_condition(), (5, 4, 3, 2, 1))
        
        
    def test_undo(self):
        m = Memento()
        m.add_condition((1, 2, 3, 4, 5))
        m.add_condition((5, 4, 3, 2, 1))
        m.undo()
        self.assertEqual(m.index, 0)
        
        
    def test_redo(self):
        m = Memento()
        m.add_condition((1, 2, 3, 4, 5))
        m.add_condition((5, 4, 3, 2, 1))
        m.undo()
        self.assertEqual(m.index, 0)
        m.redo()
        self.assertEqual(m.index, 1)
        
        
    def test_get_current(self):
        m = Memento()
        m.add_condition((1, 2, 3, 4, 5))
        m.add_condition((5, 4, 3, 2, 1))
        m.undo()
        self.assertEqual(m.get_current(), (1, 2, 3, 4, 5))



if __name__ == "__main__":
    unittest.main()
