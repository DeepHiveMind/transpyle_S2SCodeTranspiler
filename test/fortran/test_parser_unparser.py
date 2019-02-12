"""Tests for Fortran language support."""

# import collections.abc
# import logging
import unittest

# import typed_astunparse

from transpyle.fortran.parser import FortranParser
from transpyle.fortran.ast_generalizer import FortranAstGeneralizer
from transpyle.fortran.unparser import Fortran77Unparser

from test.common import \
    EXAMPLES_F77_FILES, EXAMPLES_F95_FILES, basic_check_fortran_code, \
    basic_check_fortran_ast, basic_check_python_ast

# _LOG = logging.getLogger(__name__)


class Tests(unittest.TestCase):

    def test_parse(self):
        parser = FortranParser()
        for input_path in EXAMPLES_F77_FILES + EXAMPLES_F95_FILES:
            with self.subTest(input_path=input_path):
                fortran_ast = parser.parse('', input_path)
                basic_check_fortran_ast(self, input_path, fortran_ast)

    def test_generalize(self):
        parser = FortranParser()
        generalizer = FortranAstGeneralizer()
        for input_path in EXAMPLES_F77_FILES + EXAMPLES_F95_FILES:
            with self.subTest(input_path=input_path):
                tree = generalizer.generalize(parser.parse('', input_path))
                basic_check_python_ast(self, input_path, tree)

    @unittest.skip('not ready yet')
    def test_unparse(self):
        parser = FortranParser()
        generalizer = FortranAstGeneralizer()
        unparser = Fortran77Unparser()
        for input_path in EXAMPLES_F77_FILES + EXAMPLES_F95_FILES:
            with self.subTest(input_path=input_path):
                tree = generalizer.generalize(parser.parse('', input_path))
                # _LOG.debug('generalized Fortran tree %s', typed_astunparse.dump(tree))
                code = unparser.unparse(tree)
                basic_check_fortran_code(self, input_path, code)
