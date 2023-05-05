import unittest
from TestCard import TestCard
from TestDeck import TestDeck
from TestPlayer import TestPlayer
from TestSuit import TestSuit
from TestUser import TestUser

if __name__ == '__main__':
    loader = unittest.TestLoader()

    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TestCard))
    suite.addTest(loader.loadTestsFromTestCase(TestDeck))
    suite.addTest(loader.loadTestsFromTestCase(TestPlayer))
    suite.addTest(loader.loadTestsFromTestCase(TestSuit))
    suite.addTest(loader.loadTestsFromTestCase(TestUser))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    print(f"\nTotal tests run: {result.testsRun}, Failures: {len(result.failures)}, Errors: {len(result.errors)}")
    for test, output in result.failures + result.errors:
        print(f"\n{test.id()} Failed:")
        print(output)
