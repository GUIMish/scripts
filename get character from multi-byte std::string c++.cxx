#include <iostream>
#include <map>

std::string str_get_substr(std::string str, int pos, int len){
    std::map <int, std::string> get_char; int num_char = 0;
    std::wstring wstr_char, wstr_get, tmp; std::string str_char;
    std::wstring wsTmp(str.begin(), str.end()); wstr_char = wsTmp;

    for (int i = 0; i < (int)wstr_char.size(); i++) {
        if ((int)wstr_char[num_char] < 0){
            tmp = wstr_char.substr(num_char, 2);
            std::string sTmp(tmp.begin(), tmp.end()); str_char = sTmp;
            get_char[i] = str_char; num_char = num_char + 2;
        } else {
            tmp = wstr_char.substr(num_char, 1);
            std::string sTmp(tmp.begin(), tmp.end()); str_char = sTmp;
            get_char[i] = str_char; num_char = num_char + 1;
        }
        if (num_char == (int)wstr_char.size()){break;}
    } str_char.clear();
    for (int i = 0; i < len; i++) {str_char = str_char + get_char[pos + i];}
    return str_char;
};

int main (int argc, char * argv[]) {

    std::string string = "Hello Світ!";
    std::cout << str_get_substr(string, 0, 1) << std::endl;

    return 0;
}
