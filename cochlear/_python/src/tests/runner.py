import unittest
import os.path
import sys
import time
import logging
import traceback
import cProfile
import pstats
from cStringIO import StringIO

logging.basicConfig(level=logging.CRITICAL)

class TestResult(unittest.TextTestResult):
    _lastTestCase = None

    def startTest(self, test):
        self._started = time.time()
        self._profiler = cProfile.Profile()
        self._profiler.enable()

        if self._lastTestCase != test.__class__:
            self._lastTestCase = test.__class__
            print >> self.stream
            print >> self.stream, test.__class__.__name__, sys.modules[test.__module__].__file__

        print >> self.stream, test._testMethodName.rjust(50), '\t',
        super(TestResult, self).startTest(test)

    def stopTest(self, test):
        delta = time.time() - self._started
        self._profiler.disable()
        s = StringIO()
        ps = pstats.Stats(self._profiler, stream=self.stream).sort_stats('cumulative')

        maxTime = 0.1
        if hasattr(test, 'maxTime'):
            maxTime = test.maxTime
        if delta > maxTime:
            print >> self.stream
            ps.print_stats(10)
        else:
            print >> self.stream

    def _printFail(self, test, err=None):
        print >> self.stream, 'FAIL',
        if isinstance(err, tuple):
            formatted_err = ''.join(traceback.format_exception(*err))
        elif isinstance(err, basestring):
            formatted_err = err
        else:
            formatted_err = ''

        self.failures.append((test, formatted_err))

    def _printPass(self):
        print >> self.stream, 'PASS',

    def addError(self, test, err):
        self._printFail(test, err)

    def addFailure(self, test, err):
        self._printFail(test, err)

    def addSuccess(self, test):
        self._printPass()

    def addSkip(self, test, reason):
        self._printFail(test, reason)

    def addExpectedFailure(self, test, err):
        self._printPass(test, err)

    def addUnexpectedSuccess(self, test):
        self._printFail(test)



class Runner(unittest.runner.TextTestRunner):
    def __init__(self, stream=None, descriptions=True, verbosity=1):
        if stream is None:
            stream = sys.stderr

        super(Runner, self).__init__(stream, descriptions, verbosity)

        self._testResult = TestResult(self.stream, self.descriptions, self.verbosity)

    def _makeResult(self):
        return self._testResult

loader = unittest.TestLoader()
tests = loader.discover(os.path.dirname(__file__))

print >> sys.stderr
print >> sys.stderr, 'Running unit tests:'
print >> sys.stderr, '==================='
print >> sys.stderr
runner = Runner(stream=sys.stderr)
r = runner.run(tests)

print >> sys.stderr

if r.errors or r.failures:
    print >> sys.stderr, "Failing due to:", r.errors, r.failures
    sys.exit(1)
