#!/usr/bin/python
# Copyright (C) 2015 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors:
#   Daniel Izquierdo Cortazar <dizquierdo@bitergia.com>

BICHO = 'bicho'
CVSANALY = 'cvsanaly'
EVENTIZER = 'eventizer'
IRC = 'irc'
MLSTATS = 'mlstats'
PULLPO = 'pullpo'
SIBYL = 'sibyl'
WIKI = 'wiki'

class Backend(object):
    """ Root class to deal with backends """

    def __init__(self, session):
        self.session = session

    def repositories_list(self):
        """ List of repositories for the selected backend"""
        raise NotImplementedError

    def repository_removal(self, repository):
        """ Remove the repository from the selected backend"""
        raise NotImplementedError


