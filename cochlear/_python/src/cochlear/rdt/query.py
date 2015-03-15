'''
Created on 23 May 2013

@author: szczepan
'''
import sys


class _Query(object):
    """Provides interactive IO for test cases."""
    screen = sys.stdout
    merge_description = None
    desription_buffer = list()
    question_buffer = list()
    check_buffer = list()

    def __init__(self, logger=None):
        if logger:
            self._logger = logger

    def __input(self, string):
        string = str(string)
        self.screen.write(string)
        input_ = raw_input()
        self._logger.debug(string.translate(None, '\t\n'))
        if input_.strip():
            self._logger.debug(input_.translate(None, '\t\n'))

        return input_

    def __write(self, string):
        string = str(string)
        self.screen.write(string)
        self._logger.debug(string.translate(None, '\t\n'))

    def do_this(self, message):
        if self.merge_description:
            _Query.desription_buffer.append(message)
        else:
            self.__write("\n%s" % message)

    def prompt(self, message):
        if self.merge_description:
            _Query.desription_buffer.append(message)
        else:
            self.__input('\n%s\nPress Enter to continue...' % message)

    def check_that(self, message):
        if self.merge_description:
            _Query.check_buffer.append(message)
            return True
        else:
            self.__write("\n%s" % message)

            done = False
            while not done:
                ret = self.__input("\tPass (p) or fail (f)? ")

                if ret == 'f':
                    raise AssertionError
                elif ret == 'p':
                    done = True  # exit loop and try next test
                else:
                    pass  # get another response

    def question(self, message):
        if self.merge_description:
            _Query.question_buffer.append(message)
            return True
        else:
            self.__write("\n%s" % message)

            done = False
            while not done:
                ret = self.__input("\n\tYes (y) or no (n)? ")

                if ret == 'y':
                    return True
                elif ret == 'n':
                    return False
                else:
                    pass  # get another response

    def ask_and_get_input(self, message):
        return self.__input("\n%s" % message)

    @staticmethod
    def clear_buffers():
        del _Query.desription_buffer[:]
        del _Query.question_buffer[:]
        del _Query.check_buffer[:]

    def Merge_descriptions(self, description):
        return self._Merge_descriptions(self, description)

    class _Merge_descriptions(object):
        def __init__(self, query, description):
            self.query = query
            _Query.merge_description = True
            self.query.do_this(description)

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_value, traceback):
            _Query.merge_description = False
            self.query.prompt('\n- '.join(self.query.desription_buffer))
            for ask in self.query.question_buffer:
                if not self.query.question(ask):
                    _Query.clear_buffers()
                    raise Exception(ask)
            for check in self.query.check_buffer:
                self.query.question(check)
            _Query.clear_buffers()
