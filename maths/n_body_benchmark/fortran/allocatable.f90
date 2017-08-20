
      program allocatable
          implicit none
          character(len=10) :: arg1, arg2, arg3
          integer :: i, j, t
          integer :: num
          integer :: n_step
          real :: dt
          real, parameter :: G = 6.6741e-11
          real :: r
          real :: dv_abs
          real :: dv_x
          real :: dv_y
          real :: d2
          real :: start, finish
          real, dimension(:, :), allocatable :: pos
          real, dimension(:, :), allocatable :: vel
          
          call getarg(1, arg1)
          call getarg(2, arg2)
          call getarg(3, arg3)

          read(arg1, *) num
          read(arg2, *) n_step
          read(arg3, *) dt
          call cpu_time(start)

          allocate(pos(num, 2), vel(num, 2))
          
          ! Initialize particles
          do i = 1,num
            pos(i, 1) = rand()
            pos(i, 2) = rand()
            vel(i, 1) = rand()
            vel(i, 2) = rand()
          end do
         
          ! Time loop
          do t = 1,n_step
            ! Update velocity
            do i = 1,num
              dv_x = 0.0
              dv_y = 0.0
              do j = 1,num
                if (i .NE. j) then
                  d2 = (pos(i,1) - pos(j,1))**2 + (pos(i,2) - pos(j,2))**2
                  dv_abs = G / (d2 + sqrt(d2))
                  dv_x = dv_x + (dv_abs * (pos(j, 1) - pos(i, 1)))
                  dv_y = dv_y + (dv_abs * (pos(j, 2) - pos(i, 2)))
                end if
              end do
              vel(i, 1) = vel(i, 1) + dv_x
              vel(i, 2) = vel(i, 2) + dv_y
            end do

            ! Update position
            do i = 1,num
              pos(i,1) = pos(i,1) + dt * vel(i,1)
              pos(i,2) = pos(i,2) + dt * vel(i,2)
            end do
          end do
          call cpu_time(finish)


          print *, "FORTRAN ALLOCATABLE: ", finish-start, " seconds"
        

      end program allocatable
