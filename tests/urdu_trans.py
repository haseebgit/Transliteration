#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
sys.path.append('..')
import transliteration
import unittest

class TransliterationTest(unittest.TestCase):
	def setUp(self):
		self.t = transliteration.getInstance()
		self.ur = u"خندٍٍؕ ؇رٍرٍ عهتبٍ"
		self.en = "This is a english text for transliteration"

	def testUrduToEnglish(self):
		result = self.t.transliterate(self.ur,"en_US")
		print result.encode('utf-8')
		self.assertEqual(result.strip(),u"meyk irr hepan")


	def testEnglishToUrdu(self):
		result = self.t.transliterate(self.en,"ur_IN")
		print result.encode('utf-8')
		self.assertEqual(result.strip(),u"ئؿظٍ ؇ظٍ ؅ ؇ٍٍؙؗزؿطٍ رٍرنٍؕظٍرٍرٍ ثًذٍ")



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TransliterationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

