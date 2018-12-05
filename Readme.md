The following function finds the minimum number of cameras needed to cover a set of parking spaces assuming that
each camera is covered on top of a parking spot and can cover cameraRange amount parking spots to its left
and cameraRange parking spots to its right. Therefore, it has a total coverage of 1+2*cameraRange (including itself).

The following is a diagram of a camera:

           Camera
            |   |
      <------>1<------>
   cameraRange   CameraRange

The locations list represents a list of locations of occupied parking spots. The algorithm we're applying is going to
go through the beginning to the end of the list and group the cars into distinct sections of camera coverages, with
the total number of distinct coverages being the number of cameras needed. This algorithm works to minimize the
number of cameras needed and is designed around that parameter.

As an example, if we have cameraRange=1 and the number of occupied locations=[1,2,3,7,9], we would need 3 cameras: One
above 2 encompassing [1,2,3], one above 7, and one above 9.

We can't cover 7 and 9 with one camera because the coverage of the camera above spot 7 encompasses [6,7,8] and the one
above spot 9 encompasses [8,9,10].

Final Thoughts:
We are not solving for the spots the cameras will be on but rather the number of distinct groupings. In the scope of
the problem, this is an easier perspective to take as it reduces the solution complexity. Therefore, we simply keep
track of how many distinct groupings we get and that is our return value.
