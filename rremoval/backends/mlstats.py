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

class MLStats(Backend):

    def repositories_list(self):
        query = """SELECT mailing_list_url
                   FROM mailing_lists"""
        mailing_lists = self.session.execute(query)
        print mailing_lists

    def repository_removal(self, repository):

        # Remove compressed_files mailing list
        # This code assumes this database is using INNODB engine
        query = """ DELETE FROM compressed_files
                    WHERE mailing_list_url = '%s' """ % (repository)
        self.session.execute(query)

        # Remove mailing lists
        # This code assumes this database is using INNODB engine
        # This will delete the rest of the information in cascade
        query = """ DELETE FROM mailing_lists
                    WHERE mailing_list_url = '%s' """ % (repository)
        self.session.execute(query)

