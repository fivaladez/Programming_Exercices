#include <stdio.h>

void printFM(unsigned int n);

unsigned int cantidad_casos = 0;

void main( void ) {
    printf("\n\tIntroduce the qty of cases: ");
    scanf("%d", &cantidad_casos);
    unsigned int casos[cantidad_casos];

    for(int cnt = 0; cnt < cantidad_casos; cnt++)
    {
        printf("\n\tIntroduce a positive enter number: ");
        scanf("%d", &casos[cnt]);
        printFM(casos[cnt]);
    }

}

void printFM(unsigned int n)
{
    printf("\n\t%d = ", n);
    while( (n%2 != 0) || (n%3 != 0) || (n%5 != 0) || (n%7 != 0) || (n%9 != 0)){
        if (n%2 == 0){
            printf(" 2");
            n /= 2;
        }
        else if(n%3 == 0){
            printf(" 3");
            n /= 3;
        }
        else if(n%5 == 0){
            printf(" 5");
            n /= 5;
        }
        else if(n%7 == 0){
            printf(" 7");
            n /= 7;
        }
        else if(n%9 == 0){
            printf(" 9");
            n /= 9;
        }
        else
            break;
    }
}
