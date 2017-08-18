#!/usr/bin/env julia

const size = parse(Int64, ARGS[1])
const n_step = parse(Int64, ARGS[2])
const dt = parse(Float64, ARGS[3])

function nbody(size::Int64, nstep::Int64, dt::Float64)
    G :: Float64 = 6.6741e-11
	pos :: Array{Float64, 2} = rand(Float64, (size, 2))
	vel :: Array{Float64, 2} = rand(Float64, (size, 2))
	dv_abs :: Float64 = 0.0
    # Update velocity
    for i=1:size, j=1:size
        if i != j
            dv_abs = G / (sqrt((pos[i, 1] - pos[j, 1])^2 + (pos[i, 2] - pos[j, 2])^2)^3)
			vel[j] += dv_abs * dt * (pos[j] - pos[i])
		end
	end
    # Update position
    for i = 1:size
        pos[i] += dt * vel[i]
	end
end


nbody(4, 4, 4.0)
time = @time nbody(size, n_step, dt)
println("JULIA NATIVE: ", time, " seconds")
