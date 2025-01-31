#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
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

from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Cogl(Tarball, Project):
    def __init__(self):
        Project.__init__(
            self,
            "cogl",
            archive_url="https://download.gnome.org/sources/cogl/1.22/cogl-1.22.8.tar.xz",
            hash="a805b2b019184710ff53d0496f9f0ce6dcca420c141a0f4f6fcc02131581d759",
            dependencies=["python", "glib", "cairo", "pango", "gdk-pixbuf"],
            patches=[
                "001-cogl-missing-symbols.patch",
                "002-cogl-pango-missing-symbols.patch",
            ],
        )

    def build(self):
        self.builder.mod_env("INCLUDE", f"{self.builder.gtk_dir}\\include\\harfbuzz")
        self.exec_msbuild_gen(r"build\win32", "cogl.sln", add_pars="/p:UseEnv=True")

        self.install(r".\COPYING share\doc\cogl")
