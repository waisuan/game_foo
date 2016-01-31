import unittest


class BeforeTest(unittest.TestCase):

    def test_story_parser(self):
        file_object = open("../map/whirland.txt", "r")
        print file_object.readline().rstrip()
        content = file_object.readlines()
        for line in content:
            tokens = line.rstrip().split(';')
            for token in tokens:
                print token
        file_object.close()

# if __name__ == '__main__':
#    unittest.main()
