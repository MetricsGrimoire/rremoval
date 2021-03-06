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

import MySQLdb

class Database(object):
    """ Class to deal with database access

    This is dependant from MySQL
    """

    def __init__(self, dbuser, dbpassword, dbname, hostname="localhost", port=3306):
        """ Start session and init database variables """

        self.dbuser = dbuser
        self.dbname  = dbname

        self.db = MySQLdb.connect(host=hostname,
                             port=int(port),
                             user=dbuser,
                             passwd=dbpassword,
                             db=dbname)
        self.cursor = self.db.cursor()

    def execute(self, query):
        """ Execute query in the current session"""

        data =[]

        results = int(self.cursor.execute(query))
        if results > 0:
            result1 = self.cursor.fetchall()
            if len(result1) > 0:
                # Let's parse the repositories
                for result in result1:
                    data.append(result[0])
        self.db.commit()
        return data

    def close_session(self):
        """ Close database session"""
        self.db.close()

