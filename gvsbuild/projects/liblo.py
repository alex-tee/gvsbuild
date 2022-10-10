#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#  Copyright (C) 2016 - Alexandros Theodotou
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import CmakeProject
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add

@project_add
class Liblo(Tarball, CmakeProject):
    def __init__(self):
        Project.__init__(
            self,
            "liblo",
            archive_url="http://downloads.sourceforge.net/liblo/liblo-0.31.tar.gz",
            hash="2b4f446e1220dcd624ecd8405248b08b7601e9a0d87a0b94730c2907dbccc750",
            dependencies=["cmake", "ninja"],
        )

    def build(self):
        CmakeProject.build(self, use_ninja=True, source_part="cmake")
