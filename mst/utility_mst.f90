! MiSTree: Constructs the minimum spanning tree from a given data and runs
! subsequent analysis in python. 'utility_mst.f90' contains a fortran functions
! for getting the degree from the edge indices of a minimum spanning tree.
!
! Copyright (C) 2019 Krishna Naidoo
!
! This program is free software: you can redistribute it and/or modify
! it under the terms of the GNU General Public License as published by
! the Free Software Foundation, either version 3 of the License, or
! (at your option) any later version.
!
! This program is distributed in the hope that it will be useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty of
! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
! GNU General Public License for more details.
!
! You should have received a copy of the GNU General Public License
! along with this program.  If not, see <https://www.gnu.org/licenses/>.


subroutine get_degree_for_index(index1, index2, number_of_nodes, number_of_edges, degree)
    ! Given the edge index this will compute the degree of each node.
    !
    ! Parameters
    ! ----------
    ! index1, index2 : array
    !    The index of the edges of a tree, where the '1' and '2' refer to the ends of each edge.
    ! number_of_nodes : integer
    !    The array integer length of the nodes used to construct the tree.
    ! number_of_edges : integer
    !    The array integer length of the edges forming the constructed tree.
    !
    ! Returns
    ! -------
    ! degree : array
    !    The degree for each node, i.e. the number of edges attached to each node.ß

    implicit none

    integer, intent(in) :: number_of_nodes, number_of_edges
    integer, intent(in) :: index1(number_of_edges), index2(number_of_edges)
    double precision, intent(out) :: degree(number_of_nodes)

    integer :: i

    do i = 1, number_of_nodes
        degree(i) = 0.
    end do

    do i = 1, number_of_edges
        degree(index1(i)+1) = degree(index1(i)+1) + 1.
        degree(index2(i)+1) = degree(index2(i)+1) + 1.
    end do

end subroutine get_degree_for_index
