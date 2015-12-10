# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sae
import main


application = sae.create_wsgi_app(app)