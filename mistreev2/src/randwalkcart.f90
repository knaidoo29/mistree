
subroutine periodicboundary(x, boxsize)
  ! Ensures particles remain within a periodic box.
  !
  ! Parameters
  ! ----------
  ! x : float
  !   X value.
  ! boxsize : float
  !   Box size.
  !
  ! Returns
  ! -------
  ! x : float
  !   X value.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  ! define variables

  real(kind=dp), intent(inout) :: x
  real(kind=dp), intent(in) :: boxsize

  do while (x < 0. .or. x > boxsize)
      if (x < 0.) then
          x = x + boxsize
      else if (x > boxsize) then
          x = x - boxsize
      end if
  end do

end subroutine


subroutine randwalkcart2d(steps, prand, boxsize, x0, y0, useperiodic, length, x, y)
  ! Generates a random walk on a 2D grid.
  !
  ! Parameters
  ! ----------
  ! steps : float
  !    Array of steps sizes.
  ! prand : array
  !    Random angles.
  ! boxsize : float
  !    Box size.
  ! x0, y0 : float
  !    Starting x & y coordinates.
  ! useperiodic : {0, 1}, int
  !    0 = does not enforce periodic boundary conditions.
  !    1 = enforces periodic boundary conditions.
  ! length : int
  !    Length of the x & y coordinates.
  !
  ! Returns
  ! -------
  ! x, y : array
  !    The coordinates of the random walk simulation.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: length
  real(kind=dp), intent(in) :: steps(length), prand(length)
  real(kind=dp), intent(in) :: boxsize, x0, y0
  integer, intent(in) :: useperiodic
  real(kind=dp), intent(out) :: x(length), y(length)
  integer :: i
  real(kind=dp) :: dx, dy, xnow, ynow

  x(1) = x0
  y(1) = y0

  xnow = x0
  ynow = y0

  do i = 2, length

    dx = steps(i-1)*cos(prand(i-1))
    dy = steps(i-1)*sin(prand(i-1))

    xnow = xnow + dx
    ynow = ynow + dy

    if (useperiodic == 1) then
        call periodicboundary(xnow, boxsize)
        call periodicboundary(ynow, boxsize)
    end if

    x(i) = xnow
    y(i) = ynow

  end do

end subroutine randwalkcart2d


subroutine randwalkcart3d(steps, prand, trand, boxsize, x0, y0, z0, useperiodic, length, x, y, z)
  ! Generates a random walk on a 3D grid.
  !
  ! Parameters
  ! ----------
  ! steps : float
  !    A set of input step size values.
  ! prand, trand : array
  !    Random angles on the unit sphere: phi (longitude) and theta (latitude) angles.
  ! boxsize : float
  !    Box size.
  ! x0, y0, z0 : float
  !    Starting x, y & z coordinates.
  ! useperiodic : {0, 1}, int
  !    0 = does not enforce periodic boundary conditions.
  !    1 = enforces periodic boundary conditions.
  ! length : int
  !    Length of the x, y & z coordinates.
  !
  ! Returns
  ! -------
  ! x, y, z: array
  !    The coordinates of the random walk simulation.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: length
  real(kind=dp), intent(in) :: steps(length-1), prand(length-1), trand(length-1)
  real(kind=dp), intent(in) :: boxsize, x0, y0, z0
  integer, intent(in) :: useperiodic
  real(kind=dp), intent(out) :: x(length), y(length), z(length)
  integer :: i
  real(kind=dp) :: dx, dy, dz, xnow, ynow, znow

  x(1) = x0
  y(1) = y0
  z(1) = z0

  xnow = x0
  ynow = y0
  znow = z0

  do i = 2, length

    dx = steps(i-1)*cos(prand(i-1))*sin(trand(i-1))
    dy = steps(i-1)*sin(prand(i-1))*sin(trand(i-1))
    dz = steps(i-1)*cos(trand(i-1))

    xnow = xnow + dx
    ynow = ynow + dy
    znow = znow + dz

    if (useperiodic == 1) then
      call periodicboundary(xnow, boxsize)
      call periodicboundary(ynow, boxsize)
      call periodicboundary(znow, boxsize)
    end if

    x(i) = xnow
    y(i) = ynow
    z(i) = znow

  end do

end subroutine randwalkcart3d
