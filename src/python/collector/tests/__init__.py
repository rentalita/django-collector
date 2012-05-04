# -*- coding: utf-8 -*-

import subprocess
import threading

from django.conf import settings

smtpd = None


class Process(threading.Thread):

    def __stop(self):
        self.subproc.wait()
        self.is_running = False

    def stop(self):
        self.subproc.terminate()
        self.__stop()

    def kill(self):
        self.subproc.kill()
        self.__stop()


class SMTPD(Process):

    def run(self):
        self.is_running = True

        command = 'python -m smtpd -n -c DebuggingServer %s:%s' % \
            (settings.EMAIL_HOST, settings.EMAIL_PORT)

        self.subproc = subprocess.Popen(command.split(),
                                        stdout=subprocess.PIPE)

        while self.is_running:
            print self.subproc.stdout.readline()


def setup():
    global smtpd
    smtpd = SMTPD()
    smtpd.start()


def teardown():
    global smtpd
    smtpd.stop()
    smtpd.join()

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
