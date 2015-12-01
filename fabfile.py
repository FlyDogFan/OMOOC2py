# -*- coding: utf-8 -*-
from fabric.api import env, run, local, settings
from datetime import datetime

def deploy(m='This guy left nothing to decribe this commit!'):
    '''deploy:m = "COMMIT LOGGING"\t(default as 'This guy left 
		        nothing to decribe this commit!')
	'''
    _touch(m)
    _git(m)


def _touch(m="nothing left..."):
    '''_touch:m = "COMMIT LOGGING"\t(default as 'nothing left...')
	'''
    now = datetime.today()
    local('pwd'	
    	    '&& touch fab.txt'
		    '&& echo "{now}""\t{msg}" >> fab.txt'
		    '&& date'.format(now = now, msg = m)
		)

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


def chaos():
    local('date')