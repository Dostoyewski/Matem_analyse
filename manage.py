import sys, os

cwd = os.getcwd()
INTERP = cwd+'/venv/bin/python'
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(cwd)
sys.path.append(cwd + '/venv')

sys.path.insert(0,cwd+'/venv/bin')
sys.path.insert(0,cwd+'/venv/lib/python3.5/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "Matem_analyse.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
