#include <iostream>

using namespace std;

bool is_valid(string start, string target)
{
    string remstart = "";
    for (auto alpha : start)
    {
        if (alpha == 'L' || alpha == 'R')
            remstart += alpha;
    }

    string remtarget = "";
    for (auto alpha : target)
    {
        if (alpha == 'L' || alpha == 'R')
            remtarget += alpha;
    }

    return remstart == remtarget;
}

bool solve(string start, string target)
{
    if (!is_valid(start, target))
        return false;
    int length = start.size();

    int count = 0;
    for (size_t i = 0; i < length; i++)
    {
        if (start[i] == 'L')
            count = 0;
        if (start[i] == 'R')
            count++;
        if (target[i] == 'R')
        {
            if (count)
                count--;
            else
                return false;
        }
    }
    if (count != 0)
        return false;

    count = 0;
    size_t i = length - 1;
    for (; i >= 0; i--)
    {
        if (start[i] == 'R')
            count = 0;
        if (start[i] == 'L')
            count++;
        if (target[i] == 'L')
        {
            if (count)
                count--;
            else
                return false;
        }
    }
    if (count != 0)
        return false;

    return true;
}

int main()
{
    // cout << solve("_L__R__R_", "L______RR") << endl;
    // cout << solve("R_L_", "__LR") << endl;
    // cout << solve("_R", "R_") << endl;
    cout << solve("R_L__R__R_", "_L______RR") << endl;
}
