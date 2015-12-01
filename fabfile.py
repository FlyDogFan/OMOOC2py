# -*- coding: utf-8 -*-
from fabric.api import env, run, local, settings
from datetime import datetime

def deploy(m='This guy left nothing to decribe this commit!'):
    '''deploy:m = "COMMIT LOGGING"\t(default as 'This guy left 
		        nothing to decribe this commit!')
	'''
    _touch(m)
    _git(m)

def _count():
	with open('commit.log', 'r') as f:
		lines = f.readlines()
		if not lines:
			return 1
		else:
			number = 0
			for line in lines:
				number += 1
			return number


def _touch(m="nothing left..."):
    '''_touch:m = "COMMIT LOGGING"\t(default as 'nothing left...')
	'''
    now = datetime.today()
    number = _count()
    local('pwd'	
    	    '&& touch commit.log'
		    '&& echo "{number}\t""{now}""\t{msg}" >> commit.log'
		    '&& date'.format(number = number, now = now, msg = m)
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
