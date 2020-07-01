#include<bits/stdc++.h>

using namespace std;

string transform(string input)
{
    if (input.size() <= 1) {
        return input;
    }

    string result;

    char start = '\0';
    uint freq = 0;
    char last = start;

    uint freqCount[26];
    int index;
    uint uniqLength = 0;

    for (int i = 0; i < input.length(); i++) {
        index = toLower(input[i]) - 65;
        freqCount[index]++;
    }

    for (int i = input.length() - 1; i >= 0; i--) {
        if (start == '\0' || input[i] != last) {
            result.insert(result.begin(), input[i]);
            start = input[i];
            last = input[i];
        } else {
            freq++;
        }
    }

    return result;
}

int main()
{
    string s;
    cout << "Enter the string->" << endl;
    cin >> s;

    cout << transform(s);
}
