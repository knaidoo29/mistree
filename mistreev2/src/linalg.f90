
subroutine dotvector3(a, b, c)
  ! Calculates the dot product of two vectors of length 3.
  !
  ! Parameters
  ! ----------
  ! a : array
  !   Input vector.
  ! b : array
  !   Input vector.
  !
  ! Returns
  ! -------
  ! c : array
  !   Output dot product, i.e. c = a . b

  implicit none

  integer, parameter :: dp = kind(1.d0)

  real(kind=dp), intent(in) :: a(3), b(3)
  real(kind=dp), intent(out) :: c

  c = a(1)*b(1) + a(2)*b(2) + a(3)*b(3)

end subroutine dotvector3


subroutine dot3by3mat3vec(a, b, c)
  ! Calculates the dot product a 3 by 3 matrix and vector of length 3.
  !
  ! Parameters
  ! ----------
  ! a : array
  !   Input 3 by 3 matrix.
  ! b : array
  !   Input vector of length 3.
  !
  ! Returns
  ! -------
  ! c : array
  !   Output dot product, i.e. c = a . b

  implicit none

  integer, parameter :: dp = kind(1.d0)

  real(kind=dp), intent(in) :: a(9), b(3)
  real(kind=dp), intent(out) :: c(3)

  c(1) = a(1)*b(1) + a(2)*b(2) + a(3)*b(3)
  c(2) = a(4)*b(1) + a(5)*b(2) + a(6)*b(3)
  c(3) = a(7)*b(1) + a(8)*b(2) + a(9)*b(3)

end subroutine dot3by3mat3vec


subroutine crossvector3(a, b, c)
  ! Calculates the cross product of two vectors of length 3.
  !
  ! Parameters
  ! ----------
  ! a : array
  !   Input vector.
  ! b : array
  !   Input vector.
  !
  ! Returns
  ! -------
  ! c : array
  !   Output cross product, i.e. c = a x b.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  real(kind=dp), intent(in) :: a(3), b(3)
  real(kind=dp), intent(out) :: c(3)

  c(1) = a(2)*b(3) - a(3)*b(2)
  c(2) = a(3)*b(1) - a(1)*b(3)
  c(3) = a(1)*b(2) - a(2)*b(1)

end subroutine crossvector3


subroutine normalisevector(vecin, length, vecout)
  ! Normalises an input vector.
  !
  ! Parameters
  ! ----------
  ! vec : array
  !   Input vector.
  ! length : int
  !   Length of the input vector.

  implicit none

  integer, parameter :: dp = kind(1.d0)

  integer, intent(in) :: length
  real(kind=dp), intent(in) :: vecin(length)
  real(kind=dp), intent(out) :: vecout(length)

  real(kind=dp) :: mag
  integer :: i

  mag = 0.

  do i = 1, length
    mag = mag + vecin(i)**2
  end do

  mag = sqrt(mag)

  do i = 1, length
    vecout(i) = vecin(i) / mag
  end do

end subroutine normalisevector


subroutine inv3by3(m, invm)
  ! Invert 3 by 3 matrix.
  !
  ! Parameters
  ! ----------
  ! m : array
  !     3 by 3 matrix.
  !
  ! Returns
  ! -------
  ! invm : array
  !     3 by 3 inverse matrix.

  implicit none
  integer, parameter :: dp = kind(1.d0)

  ! Declare variables.

  real(kind=dp), intent(in) :: m(9)
  real(kind=dp), intent(out) :: invm(9)

  real(kind=dp) :: a, b, c, d, e, f, g, h, i, detm
  real(kind=dp) :: aa, bb, cc, dd, ee, ff, gg, hh, ii

  a = m(1)
  b = m(2)
  c = m(3)
  d = m(4)
  e = m(5)
  f = m(6)
  g = m(7)
  h = m(8)
  i = m(9)

  aa = e*i - f*h
  bb = -(d*i - f*g)
  cc = d*h - e*g
  dd = -(b*i - c*h)
  ee = a*i - c*g
  ff = -(a*h - b*g)
  gg = b*f - c*e
  hh = -(a*f - c*d)
  ii = a*e - b*d

  detM = a*aa + b*bb + c*cc

  invm(1) = aa / detm
  invm(2) = dd / detm
  invm(3) = gg / detm
  invm(4) = bb / detm
  invm(5) = ee / detm
  invm(6) = hh / detm
  invm(7) = cc / detm
  invm(8) = ff / detm
  invm(9) = ii / detm

end subroutine inv3by3
