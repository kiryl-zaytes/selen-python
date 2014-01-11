import nose
import datetime
import os

__author__ = 'kiryl_zayets'

current_date = datetime.datetime.now().isoformat()

report_name = '{0}{1}/report/{2}{3}'.format('--xunit-file=',os.path.dirname(__file__),str(current_date),'.xml')
tests = '--tests={0}/{1}'.format( os.path.dirname(__file__),'tests/face_page.py')

noseargs = ['foo', '-v','--with-xunit',report_name, '--processes=3','--process-timeout=40', tests]
nose.run(argv=noseargs)
