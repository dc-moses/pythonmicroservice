import testtools

import barbicanclient
from barbicanclient import base
from barbicanclient import version


class TestValidateRef(testtools.TestCase):

    def test_valid_ref(self):
        ref = 'http://localhost/ff2ca003-5ebb-4b61-8a17-3f9c54ef6356'
        self.assertTrue(base.validate_ref(ref, 'Thing'))

    def test_invalid_uuid(self):
        ref = 'http://localhost/not_a_uuid'
        self.assertRaises(ValueError, base.validate_ref, ref, 'Thing')

    def test_censored_copy(self):
        d1 = {'a': '1', 'password': 'my_password', 'payload': 'my_key',
              'b': '2'}
        d2 = base.censored_copy(d1, None)
        self.assertEqual(d1, d2, 'd2 contents are unchanged')
        self.assertFalse(d1 is d2, 'd1 and d2 are different instances')
        d3 = base.censored_copy(d1, ['payload'])
        self.assertNotEqual(d1, d3, 'd3 has redacted payload value')
        self.assertNotEqual(d3['payload'], 'my_key', 'no key in payload')

    def test_module_version(self):
        self.assertTrue(hasattr(barbicanclient, '__version__'))
        # Test forward compatibility, please remove the case when all reference
        # switch to barbicanclient.__version__
        self.assertTrue(hasattr(version, '__version__'))
