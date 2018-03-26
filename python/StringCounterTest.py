import unittest
import operator
from StringCounter import countStrings

class TestStringCounter(unittest.TestCase):

    def test_counts(self):
        test_str = "the quick brown fox jumped over the lazy dog quick fox the"
        l = len(test_str)
        print("length",l)
        print(test_str[20:24])
        ans = {'the': 3, 'the ': 2, 'the q': 1, 'the qu': 1, 'the qui': 1, 'he ': 2, 'he q': 1, 'he qu': 1, 'he qui': 1, 'he quic': 1, 'e q': 1, 'e qu': 1, 'e qui': 1, 'e quic': 1, 'e quick': 1, ' qu': 2, ' qui': 2, ' quic': 2, ' quick': 2, ' quick ': 2, 'qui': 2, 'quic': 2, 'quick': 2, 'quick ': 2, 'quick b': 1, 'uic': 2, 'uick': 2, 'uick ': 2, 'uick b': 1, 'uick br': 1, 'ick': 2, 'ick ': 2, 'ick b': 1, 'ick br': 1, 'ick bro': 1, 'ck ': 2, 'ck b': 1, 'ck br': 1, 'ck bro': 1, 'ck brow': 1, 'k b': 1, 'k br': 1, 'k bro': 1, 'k brow': 1, 'k brown': 1, ' br': 1, ' bro': 1, ' brow': 1, ' brown': 1, ' brown ': 1, 'bro': 1, 'brow': 1, 'brown': 1, 'brown ': 1, 'brown f': 1, 'row': 1, 'rown': 1, 'rown ': 1, 'rown f': 1, 'rown fo': 1, 'own': 1, 'own ': 1, 'own f': 1, 'own fo': 1, 'own fox': 1, 'wn ': 1, 'wn f': 1, 'wn fo': 1, 'wn fox': 1, 'wn fox ': 1, 'n f': 1, 'n fo': 1, 'n fox': 1, 'n fox ': 1, 'n fox j': 1, ' fo': 2, ' fox': 2, ' fox ': 2, ' fox j': 1, ' fox ju': 1, 'fox': 2, 'fox ': 2, 'fox j': 1, 'fox ju': 1, 'fox jum': 1, 'ox ': 2, 'ox j': 1, 'ox ju': 1, 'ox jum': 1, 'ox jump': 1, 'x j': 1, 'x ju': 1, 'x jum': 1, 'x jump': 1, 'x jumpe': 1, ' ju': 1, ' jum': 1, ' jump': 1, ' jumpe': 1, ' jumped': 1, 'jum': 1, 'jump': 1, 'jumpe': 1, 'jumped': 1, 'jumped ': 1, 'ump': 1, 'umpe': 1, 'umped': 1, 'umped ': 1, 'umped o': 1, 'mpe': 1, 'mped': 1, 'mped ': 1, 'mped o': 1, 'mped ov': 1, 'ped': 1, 'ped ': 1, 'ped o': 1, 'ped ov': 1, 'ped ove': 1, 'ed ': 1, 'ed o': 1, 'ed ov': 1, 'ed ove': 1, 'ed over': 1, 'd o': 1, 'd ov': 1, 'd ove': 1, 'd over': 1, 'd over ': 1, ' ov': 1, ' ove': 1, ' over': 1, ' over ': 1, ' over t': 1, 'ove': 1, 'over': 1, 'over ': 1, 'over t': 1, 'over th': 1, 'ver': 1, 'ver ': 1, 'ver t': 1, 'ver th': 1, 'ver the': 1, 'er ': 1, 'er t': 1, 'er th': 1, 'er the': 1, 'er the ': 1, 'r t': 1, 'r th': 1, 'r the': 1, 'r the ': 1, 'r the l': 1, ' th': 2, ' the': 2, ' the ': 1, ' the l': 1, ' the la': 1, 'the l': 1, 'the la': 1, 'the laz': 1, 'he l': 1, 'he la': 1, 'he laz': 1, 'he lazy': 1, 'e l': 1, 'e la': 1, 'e laz': 1, 'e lazy': 1, 'e lazy ': 1, ' la': 1, ' laz': 1, ' lazy': 1, ' lazy ': 1, ' lazy d': 1, 'laz': 1, 'lazy': 1, 'lazy ': 1, 'lazy d': 1, 'lazy do': 1, 'azy': 1, 'azy ': 1, 'azy d': 1, 'azy do': 1, 'azy dog': 1, 'zy ': 1, 'zy d': 1, 'zy do': 1, 'zy dog': 1, 'zy dog ': 1, 'y d': 1, 'y do': 1, 'y dog': 1, 'y dog ': 1, 'y dog q': 1, ' do': 1, ' dog': 1, ' dog ': 1, ' dog q': 1, ' dog qu': 1, 'dog': 1, 'dog ': 1, 'dog q': 1, 'dog qu': 1, 'dog qui': 1, 'og ': 1, 'og q': 1, 'og qu': 1, 'og qui': 1, 'og quic': 1, 'g q': 1, 'g qu': 1, 'g qui': 1, 'g quic': 1, 'g quick': 1, 'quick f': 1, 'uick f': 1, 'uick fo': 1, 'ick f': 1, 'ick fo': 1, 'ick fox': 1, 'ck f': 1, 'ck fo': 1, 'ck fox': 1, 'ck fox ': 1, 'k f': 1, 'k fo': 1, 'k fox': 1, 'k fox ': 1, 'k fox t': 1, ' fox t': 1, ' fox th': 1, 'fox t': 1, 'fox th': 1, 'fox the': 1, 'ox t': 1, 'ox th': 1, 'ox the': 1, 'x t': 1, 'x th': 1, 'x the': 1}
        a = countStrings(test_str,3,8)
        # print(sorted(a.items(), key=operator.itemgetter(1)))

        self.assertEqual(a, ans)




if __name__ == '__main__':
    unittest.main()