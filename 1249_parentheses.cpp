#include <iostream>

using namespace std;

string solve(string s) {
  deque<pair<char, int>> stack = deque<pair<char, int>>();
  vector<bool> flg = vector<bool>(s.size(), false);

  for (size_t i = 0; i < s.size(); i++) {
    if (s[i] == '(')
      stack.push_back({s[i], i});
    else if (s[i] == ')') {
      if (stack.size()) {
        pair<char, int> prev = stack.back();

        flg[i] = true;
        flg[prev.second] = true;

        stack.pop_back();
      } else
        flg[i] = false;
    } else
      flg[i] = true;
  }

  string ans = "";
  for (size_t i = 0; i < s.size(); i++) {
    if (flg[i])
      ans += s[i];
  }

  return ans;
}

int main() {
  cout << solve("lee(t(c)o)de)") << endl;
  cout << solve("a)b(c)d") << endl;
  cout << solve("))((") << endl;
}
