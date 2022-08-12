# cspell:ignore installkernel
import Pkg
using IJulia

Pkg.add("IJulia")
installkernel("julia")
