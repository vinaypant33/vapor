import io
import unittest

from vapor.environment import Environment
from vapor.errors import VaporRuntimeError
from vapor.runner import run_source


def output_of(source):
    buffer = io.StringIO()
    run_source(source, output=buffer)
    return buffer.getvalue()


def value_of(source):
    return run_source(source, output=io.StringIO())
