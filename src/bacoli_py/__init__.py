import logging
_fmt = logging.Formatter(
    '%(asctime)s - %(levelname)-8s - %(name)s -> %(message)s'
)
_h = logging.StreamHandler()
_h.setFormatter(_fmt)
_logger = logging.getLogger('bacoli-py')
_logger.addHandler(_h)
_logger.setLevel('INFO')

from bacoli_py.ProblemDefinition import ProblemDefinition
from bacoli_py.Evaluation import Evaluation
from bacoli_py.Solver import Solver
from bacoli_py.Compile import f2py_compile
