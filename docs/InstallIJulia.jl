# Run as
# julia docs/InstallIJulia.jl

using Pkg
Pkg.add("IJulia")

import IJulia
IJulia.installkernel("julia-compwa.github.io")
