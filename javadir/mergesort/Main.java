class Main {
    public static void main(String[] args) {
        Mergesort solution = new Mergesort();
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int[] nums2 = {2, 5, 6};
        int m = 3, n = 3;

        solution.merge(nums1, m, nums2, n);

        // Output: [1, 2, 2, 3, 5, 6]
        for (int num : nums1) {
            System.out.print(num + " ");
        }
    }
}
