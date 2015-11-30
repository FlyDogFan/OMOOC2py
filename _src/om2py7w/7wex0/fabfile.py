# -*- coding: utf-8 -*-
from fabric.api import env, run, local, settings

def git():
	local('pwd'
		    '&& touch fab.txt'
		    '&& echo "WOW" >> fab.txt'
		    '&& date'
        )


def chaos():
    local('date') 