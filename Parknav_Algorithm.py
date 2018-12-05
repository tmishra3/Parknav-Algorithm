# Solved by Tanmay Mishra
# tmishra2003@gmail.com

# The following function finds the minimum number of cameras needed to cover a set of parking spaces assuming that
# each camera is covered on top of a parking spot and can cover cameraRange amount parking spots to its left
# and cameraRange parking spots to its right. Therefore, it has a total coverage of 1+2*cameraRange (including itself).

# The following is a diagram of a camera:

#           Camera
#            |   |
#      <------>1<------>
#  cameraRange   CameraRange

# The locations list represents a list of locations of occupied parking spots. The algorithm we're applying is going to
# go through the beginning to the end of the list and group the cars into distinct sections of camera coverages, with
# the total number of distinct coverages being the number of cameras needed. This algorithm works to minimize the
# number of cameras needed and is designed around that parameter.

# As an example, if we have cameraRange=1 and the number of occupied locations=[1,2,3,7,9], we would need 3 cameras: One
# above 2 encompassing [1,2,3], one above 7, and one above 9.
#
# We can't cover 7 and 9 with one camera because the coverage of the camera above spot 7 encompasses [6,7,8] and the one
# above spot 9 encompasses [8,9,10].

# Final Thoughts:
# We are not solving for the spots the cameras will be on but rather the number of distinct groupings. In the scope of
# the problem, this is an easier perspective to take as it reduces the solution complexity. Therefore, we simply keep
# track of how many distinct groupings we get and that is our return value.

def findMinimumNumberofCameras(cameraRange, locations=[]):

    numLocations = len(locations)  # Stores the number of parking spots. Static value.

    numCameras = 0  # Stores the number of cameras needed.

    sweep = 0  # Stores the distance between the last parking spot and the current parking spot.

    coverage = 0  # Stores the coverage of the current camera "collecting" parking spots as we sweep through the
    # list of parking spots.

    for currentLocationIndex in range(0, numLocations):  # currentLocationIndex is storing the index of the current
        # parking spot as we cycle through the list of locations.

        if currentLocationIndex > 0:  # If we're not looking at a first spot, then we take the distance between this one
            # and the last one.

            sweep = locations[currentLocationIndex] - locations[currentLocationIndex - 1]

        else:  # If we're looking at the first spot, in the framing of our problem, we can assume it to be 0.

            sweep = 0

        # If the current spot and the previous spot are still in range of one "side" of the camera AND
        # if the coverage taking this current spot into account is within the coverage of a camera (2*cameraRange)
        # ,then we can accept this spot and move on. We do this by adding this sweep amount into the coverage.

        if (sweep <= cameraRange) and ((coverage + sweep) <= (2 * cameraRange)):

            coverage += sweep

        else:

            # If the else condition applies, it means that either the sweep amount is larger than the cameraRange and/or
            # the coverage including the current spot exceeds 2*cameraRange. This means that we have reached the end of
            # spots needed for a camera coverage with the LAST spot completing the set for a new camera. The current
            # spot becomes the start of a set representing a new camera coverage. Therefore, to implement this, we reset
            # the coverage to 0 and increase the camera amount by 1.

            numCameras += 1
            coverage = 0

        # If we're at the last location, we add an additional camera. This is because regardless of if we reset the
        # coverage or not, we have to "end" this new/existing coverage into a camera.

        if currentLocationIndex == (numLocations - 1):
            
            numCameras += 1

    # When the list of locations have been traversed, sorted, and counted, we return the
    # value of numCameras.

    return numCameras

##################################################
#                                                #
#                  TEST CASES                    #
#                                                #
##################################################

print(findMinimumNumberofCameras(10, [1, 3, 4, 200, 202, 203, 240, 280, 290, 292, 301])) # -> 5
print(findMinimumNumberofCameras(1, [1, 2, 3, 4, 5])) # -> 2
