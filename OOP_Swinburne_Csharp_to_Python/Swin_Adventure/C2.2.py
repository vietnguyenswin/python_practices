"""
    Author: vietnguyenswin (Viet Nguyen)
    Name: Pass task 2.2C
    Description: + Object-Oriented Programming with Python programming language.
                 + This is a rework version of required tasks for Object-Oriented Programming with C# unit
                    (COS20007 - Swinburne Semester 2 2016).
                 + The author understands the principles of Object-Oriented Analysis & Design and achieved Distinction
                    grade (COS20007).
                 + The motivation for doing this version is to practice using Python.
                 + The works of this version are public. Nevertheless, you should not copy & paste without understanding
                    the mechanisms behind.
    Instruction: + Update later
    Last modified: 21 Nov 2017
"""
import unittest

# define Identifiable class
class Identifiable(object):
    # constructor adds identifiers to the Identifiable object from the passed list
    def __init__(self, idents):
        self.__identifiers = list(idents)

    # check if the passed in identifier is in the __identifiers
    def are_you(self, id):
        if id in self.__identifiers:
            return True
            # print("oh yeah")
        else:
            return False
            # print("oh no")

    # return the first identifier in __identifiers
    @property
    def first_id(self):
        return self.__identifiers[0]

    # convert the identifier to lowercase and add it to __identifiers list
    def add_identifier(self, new_id):
        self.__identifiers.append(str(new_id).lower())


class TestsIteration(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_are_you(self):
        test = Identifiable(["hello", "hi"])
        self.assertEqual(True, test.are_you("hello"))

    def test_first_id(self):
        test = Identifiable(["hello", "hi"])
        self.assertEqual("hello", test.first_id)

    def test_add_identifier(self):
        test = Identifiable([])
        test.add_identifier("hello")
        self.assertEqual(True, test.are_you("hello"))


class GameObject(Identifiable):
    def __init__(self, ids, name, desc):
        super(GameObject, self).__init__(ids)
        self.__name = name
        self.__desc = desc

    @property
    def name(self):
        return self.first_id

    @property
    def short_description(self):
        return self.__name + " (" + self.first_id + ")"

    @property
    def long_description(self):
        return self.__desc


class Item(GameObject):
    def __init__(self, ids, name, desc):
        super(Item, self).__init__(ids, name, desc)
        if self.are_you(ids[0]):
            self.__name = name
            self.__desc = desc

class Player(GameObject):
    def __init__(self, name, desc):
        super(Player, self).__init__(["me", "inventory"], name, desc)
        self.__name = name
        self.__desc = desc

class Inventory(object):
    def __init__(self):
        self.__items = []

    def has_item(self, input_id):
        for itm in self.__items:
            if itm.are_you(input_id):
                return True
            else:
                return False

    def put_item(self, item):
        self.__items.append(item)

    def take_item(self, input_id):
        for itm in self.__items:
            if itm.are_you(input_id):
                self.__items.remove(itm)
                return itm

    def item_fetch(self, input_id):
        for itm in self.__items:
            if itm.are_you(input_id):
                return itm

class TestInventoryClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_has_item_and_put_item(self):
        shovel = Item(["shovel", "spade"], "a shovel", "This is a might fine...")
        inv = Inventory()
        inv.put_item(shovel)
        self.assertTrue(inv.has_item("spade"))
        self.assertTrue(inv.has_item("shovel"))
        self.assertFalse(inv.has_item("abc"))

class TestItemClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_item_is_identifiable(self):
        shovel = Item(["shovel", "spade"], "a shovel", "This is a might fine...")
        self.assertTrue(shovel.are_you("shovel"))

    def test_item_name(self):
        shovel = Item(["shovel", "spade"], "a shovel", "This is a might fine...")
        self.assertEqual("shovel", shovel.name)

    def test_item_short_description(self):
        shovel = Item(["shovel", "spade"], "a shovel", "This is a might fine...")
        self.assertEqual("a shovel (shovel)", shovel.short_description)

    def test_item_long_description(self):
        shovel = Item(["shovel", "spade"], "a shovel", "This is a might fine...")
        self.assertEqual("This is a might fine...", shovel.long_description)

class TestPlayerClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_player_is_identifiable(self):
        player = Player("Viet", "Python programmer")
        self.assertTrue(player.are_you("me"))
        self.assertTrue(player.are_you("inventory"))


if __name__ == '__main__':
    unittest.main()
