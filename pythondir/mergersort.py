# Mergesort Array InPlace
class Solution():
    def merger(self, nums1, m, nums2, n):
        #nums1[] = {1, 2, 3, 0, 0, 0}
        #nums2[] = {2, 5, 6}
        #merge nums 2 to 1 to be 122356        
        # Define the last position in nums1
        last = (m + n) - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:  # Compare last elements
                nums1[last] = nums1[m - 1]  # Place the larger at the end
                m -= 1  # Move nums1 pointer back
            else:
                nums1[last] = nums2[n - 1]  # Place the larger at the end
                n -= 1  # Move nums2 pointer back
            last -= 1  # Move the `last` pointer back

        # If nums2 still has elements, add them
        while n > 0:
            nums1[last] = nums2[n - 1]  # Fill nums1 with nums2's remaining elements
            n -= 1
            last -= 1

