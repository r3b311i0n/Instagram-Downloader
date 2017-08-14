import unittest
import igram as instagram


class DownloadTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_download(self):
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BTvAszmgJxb/?taken-by=sofiablackdelia').fetch(), None)

    def test_mutiple_files(self):
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BTvAszmgJxb/?taken-by=sofiablackdelia').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BXlVqs0gYJJ/?taken-by=sofiablackdelia').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BWsd0uoDmQu/?taken-by=kendalljenner').fetch(), None)

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
