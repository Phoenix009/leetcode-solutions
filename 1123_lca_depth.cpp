TreeNode* helper(TreeNode* root, int& depth) {
  if (root == nullptr) return nullptr;

  int leftDepth = depth + 1, rightDepth = depth + 1;
  TreeNode* leftLCA = helper(root->left, leftDepth);
  TreeNode* rightLCA = helper(root->right, rightDepth);

  if (leftDepth == rightDepth) {
    depth = leftDepth;
    return root;
  } else if (leftDepth > rightDepth) {
    depth = leftDepth;
    return leftLCA;
  } else {
    depth = rightDepth;
    return rightLCA;
  }
}
