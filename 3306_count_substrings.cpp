#include <iostream>
#include <map>

using namespace std;

long long helper(string word, int k) {
  long long count = 0;

  map<char, int> vowel_count = {
      {'a', 0}, {'e', 0}, {'i', 0}, {'o', 0}, {'u', 0}};
  int consonant_count = 0;

  int left = 0, right = 0;
  while (right < word.size()) {
    if (vowel_count.count(word[right]))
      vowel_count[word[right]]++;
    else
      consonant_count++;

    bool flg = true;
    for (auto item : vowel_count)
      flg &= item.second > 0;

    while (flg && consonant_count >= k) {
      count += word.size() - right;
      if (vowel_count.count(word[left]))
        vowel_count[word[left]]--;
      else
        consonant_count--;

      for (auto item : vowel_count)
        flg &= item.second > 0;

      left++;
    }
    right++;
  }

  return count;
}

long long solve(string word, int k) {
  return helper(word, k) - helper(word, k + 1);
}

int main() {
  cout << solve("aeioqq", 1) << endl;
  cout << solve("aeiou", 0) << endl;
  cout << solve("ieaouqqieaouqq", 1) << endl;
  cout << solve("iqeaouqi", 2) << endl;
}
