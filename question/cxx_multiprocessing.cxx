#include <iostream>
#include <unistd.h>

void pricess_func(){sleep(5); std::cout << "done" << std::endl;}

int main (int argc, char * argv[]) {
	
	std::string text;
	while (text != "exit") {
		std::cout << "-> command ~$ "; std::cin >> text;
		if (text == "start") {
			/* ??? */
		}
		else if (text == "stop") {
			/* ??? */
		}
	}
	return 0;
}
