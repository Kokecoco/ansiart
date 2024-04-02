import sys
import os
# ルートディレクトリへのパスを追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ansiart import image_to_ansi, save_ansi_art, load_ansi_art
import unittest

class TestANSIArt(unittest.TestCase):

    def test_image_to_ansi(self):
        # 正常にANSIアート文字列が生成されるかをテスト
        result = image_to_ansi('tests/test_image.jpg', 100, 0.5)
        self.assertNotEqual(result, "")
        result2 = image_to_ansi('tests/test_image.png', 100, 0.5)
        self.assertNotEqual(result2, "")

    def test_save_and_load_ansi_art(self):
        # ANSIアートがファイルに保存され、正確に読み込まれるかをテスト
        test_art = "Test ANSI Art"
        save_ansi_art('test_art.txt', test_art)
        loaded_art = load_ansi_art('test_art.txt')
        self.assertEqual(test_art, loaded_art)
        os.remove('test_art.txt')

if __name__ == '__main__':
    unittest.main()
