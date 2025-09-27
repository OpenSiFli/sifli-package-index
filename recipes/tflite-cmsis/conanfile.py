from conan import ConanFile
from conan.tools.files import copy, get
import os


class TfliteCmsisRecipe(ConanFile):
    name = "tflite-cmsis"
    package_type = "unknown"

    # Optional metadata
    license = "Apache 2.0"
    author = "SiFli"
    url = "https://github.com/OpenSiFli/tflite-cmsis"
    description = "<Description of hello package here>"
    topics = ("tinyml", "tflm", "ai")

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "*"

    def requirements(self):
        # add your package dependencies here, for example:
        # self.requires("fmt/8.1.1")
        pass
   
    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def generate(self):
        pass

    def build(self):
        pass

    def package(self):
        excludes_files = ["conanbuild.bat", "conanbuildenv.bat", "conanrun.sh", 
                          "conanrunenv.sh", "deactivate_conanbuild.bat", "deactivate_conanbuild.sh",
                          "deactivate_conanrun.sh"]   
        copy(self, "*", src=self.source_folder, dst=self.package_folder,
             excludes=excludes_files)


    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.srcdirs = ["src"]
        # used to indicate the root path for SConscript and Kconfig
        self.cpp_info.libdirs = ["."]

