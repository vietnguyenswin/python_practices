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
        return False

    def put_item(self, item):
        self.__items.append(item)

    def take_item(self, input_id):
        for itm in self.__items:
            if itm.are_you(input_id):
                self.__items.remove(itm)

    def item_fetch(self, input_id):
        for itm in self.__items:
            if itm.are_you(input_id):
                return itm

    @property
    def item_list(self):
        list_details = ""
        for itm in self.__items:
            list_details += itm.short_description + "\n"
        return list_details

class TestsIteration(unittest.TestCase):
    def setUp(self):
        self.test = Identifiable(["hello", "hi"])

    def tearDown(self):
        pass

    def test_are_you(self):
        self.assertEqual(True, self.test.are_you("hello"))

    def test_first_id(self):
        self.assertEqual("hello", self.test.first_id)

    def test_add_identifier(self):
        self.assertEqual(True, self.test.are_you("hello"))

class TestInventoryClass(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        self.shovel = Item(["shovel", "spade"], "a shovel", "This is a might fine...")
        self.computer = Item(["computer", "pc"], "a computer", "This is a desktop")
        self.inv.put_item(self.shovel)
        self.inv.put_item(self.computer)

    def tearDown(self):
        pass

    def test_has_item_and_put_item(self):
        self.assertTrue(self.inv.has_item("spade"))
        self.assertTrue(self.inv.has_item("shovel"))
        self.assertTrue(self.inv.has_item("computer"))
        self.assertTrue(self.inv.has_item("pc"))
        self.assertFalse(self.inv.has_item("abc"))

    def test_item_fetch(self):
        self.assertIsNotNone(self.inv.item_fetch("shovel"))
        self.assertIsNotNone(self.inv.item_fetch("spade"))
        self.assertIsNotNone(self.inv.item_fetch("computer"))
        self.assertIsNotNone(self.inv.item_fetch("pc"))
        self.assertIsNone(self.inv.item_fetch("abc"))

    def test_take_item(self):
        self.assertIsNotNone(self.inv.item_fetch("shovel"))
        self.assertIsNotNone(self.inv.item_fetch("computer"))
        self.assertIsNone(self.inv.take_item("shovel"))
        self.assertIsNone(self.inv.take_item("computer"))

    def test_item_list(self):
        self.assertEqual("a shovel (shovel)\na computer (computer)\n", self.inv.item_list)

class TestItemClass(unittest.TestCase):
    def setUp(self):
        self.shovel = Item(["shovel", "spade"], "a shovel", "This is a might fine...")

    def tearDown(self):
        pass

    def test_item_is_identifiable(self):
        self.assertTrue(self.shovel.are_you("shovel"))

    def test_item_name(self):
        self.assertEqual("shovel", self.shovel.name)

    def test_item_short_description(self):
        self.assertEqual("a shovel (shovel)", self.shovel.short_description)

    def test_item_long_description(self):
        self.assertEqual("This is a might fine...", self.shovel.long_description)

class TestPlayerClass(unittest.TestCase):
    def setUp(self):
        self.player = Player("Viet", "Python programmer")

    def tearDown(self):
        pass

    def test_player_is_identifiable(self):
        self.assertTrue(self.player.are_you("me"))
        self.assertTrue(self.player.are_you("inventory"))


if __name__ == '__main__':
    unittest.main()
