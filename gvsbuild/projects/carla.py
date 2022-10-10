#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#  Copyright (C) 2022 - Alexandros Theodotou
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

import os

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add
from gvsbuild.utils.utils import convert_to_msys


@project_add
class CarlaGCC(Tarball, Project):
    def __init__(self):
        Project.__init__(
            self,
            "carlagcc",
            archive_url="https://github.com/falkTX/Carla/archive/refs/tags/v2.5.1.tar.gz",
            hash="c47eea999b2880bde035fbc30d7b42b49234a81327127048a56967ec884dfdba",
            dependencies=["msys2", "pkg-config"],
            patches=["0001-Fix-gtkbuild.patch"],
        )

    def build(self):
        msys_path = Project.get_tool_path("msys2")
        self.exec_vs(
            r"%s\bash build\build.sh %s %s"
            % (
                msys_path,
                convert_to_msys(self.pkg_dir),
                convert_to_msys(self.builder.gtk_dir),
                #self.builder.opts.configuration,
            ),
            add_path=msys_path,
        )

@project_add
class CarlaMSVC(Tarball, Meson):
    def __init__(self):
        Project.__init__(
            self,
            "carlamsvc",
            archive_url="https://github.com/alex-tee/Carla/archive/refs/heads/for_zrythm.tar.gz",
            hash="d82864b051ef9db3076d92b19ad30bbfcc3c660d00a0ba013cf66810b2589db4",
            dependencies=["fluidsynth", "fontconfig", "freetype", "liblo", ],
        )

    def build(self):
        Meson.build(
                self,
                meson_params="-Dcpp_args=-D__WIN32__ -Dc_args=-D__WIN32__",
                )
