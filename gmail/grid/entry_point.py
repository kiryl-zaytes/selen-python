import nose
import datetime
__author__ = 'kiryl_zayets'

current_date = datetime.datetime.now().isoformat()
report_name = '{0}/grid/report/{1}{2}'.format('--xunit-file=',str(current_date),'.xml')
noseargs = ['foo', '-v','--with-xunit', report_name, '--processes=3','--process-timeout=40' ,'--tests=tests/face_page.py']
nose.run(argv=noseargs)
