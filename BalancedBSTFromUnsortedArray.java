import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class BalancedBSTFromUnsortedArray {

    public static TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0)
            return null;
        return sortedArrayToBST(nums, 0, nums.length - 1);
    }

    private static TreeNode sortedArrayToBST(int[] nums, int start, int end) {
        if (start > end)
            return null;
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = sortedArrayToBST(nums, start, mid - 1);
        root.right = sortedArrayToBST(nums, mid + 1, end);
        return root;
    }

    public static boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;
        int lh = height(root.left);
        int rh = height(root.right);
        if (Math.abs(lh - rh) <= 1 && isBalanced(root.left) && isBalanced(root.right))
            return true;
        return false;
    }

    private static int height(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + Math.max(height(root.left), height(root.right));
    }

    public static void printTree(TreeNode root) {
        if (root == null) {
            System.out.println("Tree is empty");
            return;
        }
        printTree(root, 0);
    }
    
    private static void printTree(TreeNode root, int level) {
        if (root != null) {
            printTree(root.right, level + 1);
            for (int i = 0; i < level; i++) {
                System.out.print("    ");
            }
            System.out.println(root.val);
            printTree(root.left, level + 1);
        }
    }
    
    public static void main(String[] args) {
        int[] nums = { 15, 10, 20, 8, 12, 16, 25 };
        Arrays.sort(nums); // Sort the array
        TreeNode bstRoot = sortedArrayToBST(nums);

        if (isBalanced(bstRoot))
            System.out.println("The BST is height-balanced.");
        else
            System.out.println("The BST is not height-balanced.");

        System.out.println("Height-Balanced BST:");
        printTree(bstRoot);
    }
}
