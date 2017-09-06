import unittest
import igram as instagram


class DownloadTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def test_download(self):
        try:
            instagram.Download('https://www.instagram.com/p/BTvAszmgJxb/?taken-by=sofiablackdelia')
        except (IndexError, KeyError) as e:
            self.fail(e)

    def test_multiple_images(self):
        try:
            instagram.Download('https://www.instagram.com/p/BTvAszmgJxb/?taken-by=sofiablackdelia')
            instagram.Download('https://www.instagram.com/p/BXlVqs0gYJJ/?taken-by=sofiablackdelia')
            instagram.Download('https://www.instagram.com/p/BWsd0uoDmQu/?taken-by=kendalljenner')
        except (IndexError, KeyError) as e:
            self.fail(e)

    def test_multiple_videos(self):
        try:
            instagram.Download('https://www.instagram.com/p/BYOjMOhgegp/?taken-by=sofiablackdelia')
            instagram.Download('https://www.instagram.com/p/BX8mD4AAyQI/?taken-by=sofiablackdelia')
            instagram.Download('https://www.instagram.com/p/BXqVx3qjUwd/?taken-by=kendalljenner')
        except (IndexError, KeyError) as e:
            self.fail(e)

    def test_mix_of_both(self):
        try:
            instagram.Download('https://www.instagram.com/p/BUeZiJyjXtS/?taken-by=kendalljenner')
            instagram.Download('https://www.instagram.com/p/BRbzdH0DqTk/?taken-by=kendalljenner')
            instagram.Download('https://www.instagram.com/p/BRWANhLj6ph/?taken-by=kendalljenner')
            instagram.Download('https://www.instagram.com/p/BYdvYl1DJZE/?taken-by=alexisren')
        except (IndexError, KeyError) as e:
            self.fail(e)

    def test_image_slideshow(self):
        try:
            instagram.Download('https://www.instagram.com/p/BX1MmNIgkUj/?taken-by=sofiablackdelia')
        except (IndexError, KeyError) as e:
            self.fail(e)

    def test_mix_slideshow(self):
        try:
            instagram.Download('https://www.instagram.com/p/BXq_rYZjAD5/?taken-by=alexisren')
        except (IndexError, KeyError) as e:
            self.fail(e)

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
