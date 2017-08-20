#!/usr/bin/env julia

const size = parse(Int64, ARGS[1])
const n_step = parse(Int64, ARGS[2])
const dt = parse(Float64, ARGS[3])

#using Plots
#pyplot()

function nbody(size::Int64, nstep::Int64, dt::Float64)
    G :: Float64 = 6.6741e-11
    pos :: Array{Float64, 2} = rand(Float64, (size, 2))
    vel :: Array{Float64, 2} = zeros(Float64, (size, 2))
    dv_abs :: Float64 = 0.0
    dv_x :: Float64 = 0.0
    dv_y :: Float64 = 0.0
	d2 :: Float64 = 0.0
	
	# Time loop
	#@gif for t=1:n_step
	for t=1:n_step
        # Update velocity
        for i=1:size
			dv_x = 0.0
			dv_y = 0.0
			for j=1:size
            	if i != j
					d2 = (pos[i, 1] - pos[j, 1])^2 + (pos[i, 2] - pos[j, 2])^2
					dv_abs = G / (d2 + sqrt(d2))
					dv_x += dv_abs * dt * (pos[j, 1] - pos[i, 1])
					dv_y += dv_abs * dt * (pos[j, 2] - pos[i, 2])
				end
            end
            vel[i, 1] += dv_x
            vel[i, 2] += dv_y
        end
        # Update position
        for i = 1:size
            pos[i, 1] += dt * vel[i, 1]
            pos[i, 2] += dt * vel[i, 2]
        end
		#scatter(pos[:, 1], pos[:, 2], xlims=(0,1), ylims=(0,1))
	end
end


nbody(4, 4, 4.0)
time = @timed nbody(size, n_step, dt)
println(" JULIA NATIVE:    ", time[2], "    seconds")
