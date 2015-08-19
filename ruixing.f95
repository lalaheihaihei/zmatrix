!===============================================================================
!  ruixing.f95
!===============================================================================

!-------------------------------------------------------------------------------
      implicit real*8(a-h,o-z)
      integer, parameter :: DP = 8
      integer, parameter :: nmax=100
      integer :: a,b,c,d ! count of atoms

      character(len=132) :: moji
      character(len=2), dimension(nmax) :: atom

      real(DP), parameter :: pi = 3.141592653589793238_DP ! pi
      real(DP), dimension(nmax) :: x, y, z
      real(DP), dimension(nmax,nmax,3) :: vector  ! vector of two atoms, where nmax/nmax stands for two atoms, 3(1/2/3) stands for x/y/z
      real(DP), dimension(nmax,nmax,nmax) :: angle ! angle(a,b,c) stands for bondangle of (a,b,c)
      real(DP)  innerproduct, product
      real(DP), dimension(nmax,nmax) :: distance
      real(DP), dimension(nmax,nmax,nmax,4) :: nvector,dihedral !normal vector of the plane of 3 atoms a,b,c; 4(1/2/3) stands for xyz. 4 is used for dihedral(a,b,c,d), which stands for the dihedral angle of abc and bcd.
      character(len=80) :: arg1
      integer :: narg
!-------------------------------------------------------------------------------

!---- open XYZ

      narg = iargc()
      if(narg /= 1) goto 999
      call getarg(1,arg1)
      open(1,file=arg1,status='unknown')

!---- read XYZ

      read(1,*) natoms
      read(1,'(a132)') moji
      do i=1,natoms
         read(1,*) atom(i), x(i), y(i), z(i)
         write(6,*) atom(i), x(i), y(i), z(i)
      enddo
 !---- calculate distances between any two atoms
      do a=1,natoms
         do b=(a+1),natoms
            vector(a,b,1) = (x(b)-x(a))
            vector(a,b,2) = (y(b)-y(a))
            vector(a,b,3) = (z(b)-z(a))
            write(*,*) "vector of ",atom(b),"->",atom(a)," is (",vector(a,b,1),",",vector(a,b,2),",",vector(a,b,3),")"
            enddo
      enddo
      do a=1,natoms
         do b=a+1,natoms
            distance(a,b) = sqrt(vector(a,b,1)**2 + vector(a,b,2)**2 + vector(a,b,3)**2)
            write(*,*) "distance between ", atom(a)," and ",atom(b)," is ",distance(a,b)
          enddo
      enddo
!----- calculate bondangle , where atoms are like 1-2-3, 2-3-4, 3-4-5... 
      do a=1,natoms-2
         b=a+1
         c=a+2
         innerproduct = (vector(a,b,1)*vector(b,c,1)+vector(a,b,2)*vector(b,c,2)+vector(a,b,3)*vector(b,c,3))
         product = distance(a,b) * distance(b,c)
         angle(a,b,c) = acos(innerproduct/product)/(2*pi) * 360
         write(*,*) "angle of ",atom(c),atom(b),atom(a)," is ", 180-angle(a,b,c)
      enddo
!----- calculate dihedral angle, where atoms on a plane are like 1-2-3, 2-3-4...
      do a=1,natoms-2
         b=a+1
         c=a+2
         nvector(a,b,c,1)=(vector(a,b,3)*vector(b,c,2) - vector(b,c,3)*vector(a,b,2))/(vector(a,b,1)*vector(b,c,2)-vector(b,c,1)*&
         vector(a,b,2))
         nvector(a,b,c,2)=(vector(a,b,3) * vector(b,c,1) - vector(b,c,3)*vector(a,b,1))/(vector(a,b,1)*vector(b,c,2)-vector(b,c,1)*&
         vector(a,b,2))
         nvector(a,b,c,3)=1
      enddo
      do a=1,natoms-3
         b=a+1
         c=a+2
         d=a+3
         innerproduct = (nvector(a,b,c,1)*nvector(b,c,d,1)+nvector(a,b,c,2)*nvector(b,c,d,2)+nvector(a,b,c,3)*nvector&
         (b,c,d,3))
         product = sqrt(nvector(a,b,c,1)**2+nvector(a,b,c,2)**2+nvector(a,b,c,3)**2)*sqrt(nvector(b,c,d,1)**2+nvector(b,c,d,2)&
         **2+nvector(b,c,d,3)**2)
         dihedral(a,b,c,d) = acos(innerproduct/product)/(2*pi) * 360
         write(*,*) "dihedral angle of ",atom(c),atom(b),atom(a), " and ",atom(d),atom(c),atom(b)," is ", 180-dihedral(a,b,c,d)
      enddo
   999 stop
      end

