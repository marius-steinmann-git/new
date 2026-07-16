#include <iostream>

int main()
{
    int x{}; //definition of variable x
    std::cout<< "wie gross soll x sein?";
    std::cin >> x;

    std::cout<< "du hast" <<x<< "eingegeben"<<std::endl;
    return 0;
}