"""
Isolated script for installing an IJulia kernel on RTD.
"""
import Pkg
Pkg.add("IJulia")

import IJulia
IJulia.installkernel("julia")
# cspell:ignore installkernel
