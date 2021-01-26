'''
import barcode

hold = barcode.get_barcode_class('ean13')

_test_case = hold('5617881729208')

_save_here = _test_case.save('111')
'''

import barcode

from barcode.writer import ImageWriter

hold = barcode.get_barcode_class('code39')

_test_case = hold('AAAAABAHAc', writer=ImageWriter())

_save_here = _test_case.save('108')
