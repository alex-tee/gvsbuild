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

from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add
from gvsbuild.utils.utils import convert_to_msys


@project_add
class Guile3(Tarball, Project):
    def __init__(self):
        Project.__init__(
            self,
            "guile3",
            archive_url="https://ftp.gnu.org/gnu/guile/guile-3.0.8.tar.gz",
            hash="f25ae0c26e911af1b5005292d4f56621879f74d6958b30741cf67d8b6feb2016",
            dependencies=["msys2"],
        )

    def build(self):
        configure_options = (
            "--enable-pic --disable-tmpnam --disable-rpath"
        )
        #if self.builder.opts.configuration == "debug":
        #    configure_options += "--enable-debug_libs"

        target = "x86-win32-vs" if self.builder.x86 else "x86_64-win64-vs"
        target += self.builder.opts.vs_ver

        msys_path = Project.get_tool_path("msys2")

        self.exec_vs(
            r"%s\bash ./configure --target=%s --prefix=%s %s"
            % (
                msys_path,
                target,
                convert_to_msys(self.builder.gtk_dir),
                configure_options,
            ),
            add_path=msys_path,
        )
        self.exec_vs(r"make", add_path=msys_path)
        self.exec_vs(r"make install", add_path=msys_path)

    def post_install(self):
        pass
        # LibVPX generates a static library named 'vpxmd.lib' or 'vpxmdd.lib'
        # in an unusual directory which is not the same as expected by the vpx.pc file
        #if self.builder.opts.configuration == "debug":
        #    lib_name = "vpxmdd.lib"
        #else:
        #    lib_name = "vpxmd.lib"
        #lib_path = f"Win32/{lib_name}" if self.builder.x86 else f"x64/{lib_name}"
        #self.builder.exec_msys(
        #    ["mv", lib_path, "./vpx.lib"],
        #    working_dir=os.path.join(self.builder.gtk_dir, "lib"),
        #)
