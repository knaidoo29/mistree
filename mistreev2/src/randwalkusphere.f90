include "linalg.f90"


subroutine usphererotate(phi, theta, phi_start, theta_start, phi_end, theta_end, phi_new, theta_new)
  ! Rotates a point on a unit sphere from (phi_start, theta_start) to (phi_end, theta_end)
  !
  ! Parameters
  ! ----------
  ! phi, theta : float
  !   Point on a unit sphere.
  ! phi_start, theta_start : float
  !   Starting point of rotation.
  ! phi_end, theta_end : float
  !   Ending point of rotation.

  implicit none

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp) :: pi = 4*atan(1.)

  ! define variables

  real(kind=dp), intent(in) :: phi, theta
  real(kind=dp), intent(in) :: phi_start, theta_start, phi_end, theta_end
  real(kind=dp), intent(out) :: phi_new, theta_new

  real(kind=dp) :: u(3), v(3), n1(3), n(3), t(3), inpos(3), outpos1(3), outpos2(3), outpos(3)
  real(kind=dp) :: dotvt, dotvu, alpha, r
  real(kind=dp) :: rmatrix(9), tmatrix(9), invtmatrix(9)

  u(1) = cos(phi_start)*sin(theta_start)
  u(2) = sin(phi_start)*sin(theta_start)
  u(3) = cos(theta_start)

  v(1) = cos(phi_end)*sin(theta_end)
  v(2) = sin(phi_end)*sin(theta_end)
  v(3) = cos(theta_end)

  call crossvector3(u, v, n1)
  call normalisevector(n1, 3, n)

  call crossvector3(n, u, t)

  call dotvector3(v, t, dotvt)
  call dotvector3(v, u, dotvu)

  alpha = atan2(dotvt, dotvu)

  rmatrix(1) = cos(alpha)
  rmatrix(2) = -sin(alpha)
  rmatrix(3) = 0.
  rmatrix(4) = sin(alpha)
  rmatrix(5) = cos(alpha)
  rmatrix(6) = 0.
  rmatrix(7) = 0.
  rmatrix(8) = 0.
  rmatrix(9) = 1.

  tmatrix(1) = u(1)
  tmatrix(2) = t(1)
  tmatrix(3) = n(1)
  tmatrix(4) = u(2)
  tmatrix(5) = t(2)
  tmatrix(6) = n(2)
  tmatrix(7) = u(3)
  tmatrix(8) = t(3)
  tmatrix(9) = n(3)

  call inv3by3(tmatrix, invtmatrix)

  inpos(1) = cos(phi)*sin(theta)
  inpos(2) = sin(phi)*sin(theta)
  inpos(3) = cos(theta)

  call dot3by3mat3vec(invtmatrix, inpos, outpos1)
  call dot3by3mat3vec(rmatrix, outpos1, outpos2)
  call dot3by3mat3vec(tmatrix, outpos2, outpos)

  r = sqrt(outpos(1)**2 + outpos(2)**2 + outpos(3)**2)
  phi_new = atan2(outpos(2), outpos(1))
  if (phi_new < 0) then
    phi_new = phi_new + 2.*pi
  end if
  theta_new = acos(outpos(3)/r)

end subroutine usphererotate


subroutine randwalkusphere(steps, prand, phi0, theta0, length, phi, theta)
  ! Generates a random walk on a 2D grid.
  !
  ! Parameters
  ! ----------
  ! steps : float
  !    Array of steps sizes.
  ! prand : array
  !    Random angles.
  ! phi0, theta0 : float
  !    Starting phi & theta coordinates.
  ! length : int
  !    Length of the phi & theta coordinates.
  !
  ! Returns
  ! -------
  ! phi, theta : array
  !    The coordinates of the random walk simulation on the unit sphere.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: length
  real(kind=dp), intent(in) :: steps(length-1), prand(length-1)
  real(kind=dp), intent(in) :: phi0, theta0
  real(kind=dp), intent(out) :: phi(length), theta(length)
  integer :: i
  real(kind=dp) :: dphi, dtheta, phinow, thetanow, phinew, thetanew, phipol, thetapol

  phipol = 0.
  thetapol = 0.

  phi(1) = phi0
  theta(1) = theta0

  phinow = phi0
  thetanow = theta0

  do i = 2, length

    dphi = prand(i-1)
    dtheta = steps(i-1)

    call usphererotate(dphi, dtheta, phipol, thetapol, phinow, thetanow, phinew, thetanew)

    phinow = phinew
    thetanow = thetanew

    phi(i) = phinow
    theta(i) = thetanow

  end do

end subroutine randwalkusphere
