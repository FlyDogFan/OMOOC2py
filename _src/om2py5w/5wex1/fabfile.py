# -*- coding: utf-8 -*-
from fabric.api import local
from datetime import datetime

def deploy(m='This guy left nothing to decribe this commit!'):
    '''deploy:m = "COMMIT LOGGING"\t(default as 'This guy left 
		        nothing to decribe this commit!')
	'''
    _git(m)


def _git(m='This guy left nothing to decribe this commit!'):
	'''git:m = "COMMIT LOGGING"\t(default as 'This guy left 
		        nothing to decribe this commit!')
	'''	
	local('pwd'		    
		    '&& git add .'
		    '&& git commit -am "{msg}"'
		    '&& git push origin master'
		    '&& date'.format(msg = m)
        )
