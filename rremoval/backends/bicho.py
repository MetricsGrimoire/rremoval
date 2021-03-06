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

from rremoval.backends import Backend

class Bicho(Backend):

    def repositories_list(self):
        query = """SELECT url
                   FROM trackers"""
        trackers = self.session.execute(query)
        print trackers

    def repository_removal(self, repository):

        # Remove Trackers
        query = """ DELETE FROM trackers
                    WHERE url = '%s' """ % (repository)
        self.session.execute(query)

        # Remove Issues
        query = """ DELETE FROM issues
                    WHERE tracker_id not in (
                        SELECT distinct(id)
                        FROM trackers)
                """
        self.session.execute(query)

        # Remove Changes
        query = """ DELETE FROM changes
                    WHERE issue_id not in (
                        SELECT distinct(id)
                        FROM issues)
                """
        self.session.execute(query)

        # Remove Comments
        query = """ DELETE FROM comments
                    WHERE issue_id not in (
                        SELECT distinct(id)
                        FROM issues)
                """
        self.session.execute(query)

        # Check log table
        query = """ SELECT TABLE_NAME
                    FROM INFORMATION_SCHEMA.TABLES
                    WHERE TABLE_SCHEMA='%s' AND
                          TABLE_NAME like '%s_log_%s'
                """ % (self.session.dbname, "%", "%")
        table_name = self.session.execute(query)
        table_name = table_name[0]
        if len(table_name):
            # This is an optional table and this may not exist
            query = """ DELETE FROM %s
                        WHERE issue_id not in (
                            SELECT distinct(id)
                            FROM issues)
                    """ % (table_name)
            self.session.execute(query)

        # Check ext table
        query = """ SELECT TABLE_NAME
                    FROM INFORMATION_SCHEMA.TABLES
                    WHERE TABLE_SCHEMA='%s' AND
                          TABLE_NAME like '%s_ext_%s'
                """ % (self.session.dbname, "%", "%")
        table_name = self.session.execute(query)
        table_name = table_name[0]
        if len(table_name):
            # This is an optional table and this may not exist
            query = """ DELETE FROM %s
                        WHERE issue_id not in (
                            SELECT distinct(id)
                            FROM issues)
                    """ % (table_name)
            self.session.execute(query)

