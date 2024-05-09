# Run as
# julia docs/InstallIJulia.jl

using Pkg
Pkg.activate(@__DIR__)
Pkg.instantiate()

import IJulia
IJulia.installkernel("julia-compwa.github.io")
