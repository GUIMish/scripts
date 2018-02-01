/** Copyright 2017 GUIMish <Mish7913@gmail.com> **/

/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 */

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
