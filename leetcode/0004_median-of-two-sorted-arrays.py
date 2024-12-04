from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Helper function to find the k-th smallest element in two sorted arrays
        def findKth(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]

            # Find the middle indices and values of nums1 and nums2
            m1, m2 = len(nums1) // 2, len(nums2) // 2
            v1, v2 = nums1[m1], nums2[m2]

            # If the sum of middle indices is less than k
            if m1 + m2 < k:
                # If v1 is less than v2, discard the first half of nums1
                if v1 < v2:
                    return findKth(nums1[m1 + 1 :], nums2, k - m1 - 1)
                # Otherwise, discard the first half of nums2
                else:
                    return findKth(nums1, nums2[m2 + 1 :], k - m2 - 1)
            else:
                # If v1 is less than v2, discard the second half of nums2
                if v1 < v2:
                    return findKth(nums1, nums2[:m2], k)
                # Otherwise, discard the second half of nums1
                else:
                    return findKth(nums1[:m1], nums2, k)

        n1, n2 = len(nums1), len(nums2)
        k = (n1 + n2 - 1) // 2

        # If the total length is even, return the average of the two middle elements
        if (n1 + n2) % 2 == 0:
            return (findKth(nums1, nums2, k) + findKth(nums1, nums2, k + 1)) / 2
        # If the total length is odd, return the middle element
        else:
            return findKth(nums1, nums2, k)
