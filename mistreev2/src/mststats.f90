

subroutine getgraphdegree(i1, i2, nnodes, nedges, degree)
    ! Given the edge index this will compute the degree of each node.
    !
    ! Parameters
    ! ----------
    ! i1, i2 : array
    !    The index of the edges of a tree, where the '1' and '2' refer to the ends of each edge.
    ! nnodes : integer
    !    The array integer length of the nodes used to construct the tree.
    ! nedges : integer
    !    The array integer length of the edges forming the constructed tree.
    !
    ! Returns
    ! -------
    ! degree : array
    !    The degree of a node, i.e. the number of edges connecting to each node.


    implicit none

    integer, intent(in) :: nnodes, nedges
    integer, intent(in) :: i1(nedges), i2(nedges)
    double precision, intent(out) :: degree(nnodes)

    integer :: i

    do i = 1, nnodes
        degree(i) = 0.
    end do

    do i = 1, nedges
        degree(i1(i)+1) = degree(i1(i)+1) + 1.
        degree(i2(i)+1) = degree(i2(i)+1) + 1.
    end do

end subroutine getgraphdegree
