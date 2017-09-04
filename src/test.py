import unittest
import igram as instagram


class DownloadTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_download(self):
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BTvAszmgJxb/?taken-by=sofiablackdelia').fetch(), None)

    def test_multiple_images(self):
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BTvAszmgJxb/?taken-by=sofiablackdelia').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BXlVqs0gYJJ/?taken-by=sofiablackdelia').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BWsd0uoDmQu/?taken-by=kendalljenner').fetch(), None)

    def test_multiple_videos(self):
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BYOjMOhgegp/?taken-by=sofiablackdelia').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BX8mD4AAyQI/?taken-by=sofiablackdelia').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BXqVx3qjUwd/?taken-by=kendalljenner').fetch(), None)

    def test_mix_of_both(self):
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BUeZiJyjXtS/?taken-by=kendalljenner').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BRbzdH0DqTk/?taken-by=kendalljenner').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BRWANhLj6ph/?taken-by=kendalljenner').fetch(), None)
        self.assertEqual(instagram.Download('https://www.instagram.com/p/BYdvYl1DJZE/?taken-by=alexisren').fetch(), None)

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
