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

class CVSAnalY(Backend):

    def repositories_list(self):
        query = """SELECT uri
                   FROM repositories"""
        repositories = self.session.execute(query)
        print repositories

    def repository_removal(self, repository):

        # Remove repository
        query = """ DELETE FROM repositories
                    WHERE uri = '%s'""" % (repository)
        self.session.execute(query)

        # Remove commits
        query = """ DELETE FROM scmlog
                    WHERE repository_id not in (
                        SELECT distinct(id)
                        FROM repositories) """
        self.session.execute(query)

        # Remove actions
        query = """ DELETE FROM actions
                    WHERE commit_id not in (
                        SELECT distinct(id)
                        FROM scmlog) """
        self.session.execute(query)

        # Remove branches
        query = """ DELETE FROM branches
                    WHERE id not in (
                        SELECT distinct(branch_id)
                        FROM actions) """
        self.session.execute(query)

        # Remove commits_lines
        query = """ DELETE FROM commits_lines
                    WHERE commit_id not in (
                        SELECT distinct(id)
                        FROM scmlog) """
        self.session.execute(query)

        # Remove files
        query = """ DELETE FROM files
                    WHERE repository_id not in (
                        SELECT distinct(id)
                        FROM repositories) """
        self.session.execute(query)

        # Remove tags
        query = """ DELETE FROM tag_revisions
                    WHERE commit_id not in (
                        SELECT distinct(id)
                        FROM scmlog) """
        self.session.execute(query)

        query = """ DELETE FROM tags
                    WHERE id not in (
                        SELECT distinct(tag_id)
                        FROM tag_revisions) """
        self.session.execute(query)

