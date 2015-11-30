# -*- coding: utf-8 -*-
from fabric.api import env, run, local, settings
from datetime import datetime

def git(m='This guy left nothing to decribe this commit!'):
	'''git:m = "COMMIT LOGGING"\t(default as 'This guy left 
		        nothing to decribe this commit!')
	'''
	now = datetime.today()
	local('pwd'		    
		    '&& touch fab.txt'
		    '&& echo "{now}""\t{msg}" >> fab.txt'
		    '&& git add .'
		    '&& git commit -am "{msg}"'
		    '&& git push origin master'
		    '&& date'.format(now = now, msg = m )
        )


def chaos():
    local('date') 