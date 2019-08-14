#include <stdio.h>

void suma_digitos(unsigned int numero);

unsigned int cantidad_casos = 0;

void main( void ) {
    printf("\n\tIntroduce the qty of cases: ");
    scanf("%d", &cantidad_casos);
    unsigned int casos[cantidad_casos];

    for(int cnt = 0; cnt < cantidad_casos; cnt++)
    {
        printf("\n\tIntroduce a positive enter number: ");
        scanf("%d", &casos[cnt]);
        suma_digitos(casos[cnt]);
    }

}

void suma_digitos(unsigned int numero)
{
    unsigned int result = 0;
    unsigned int count;

    printf("\n\t");
    for(count=100000;count>0;count/=10)
    {
        if(numero/count >= 1)
        {
            if(count < 10)
                printf("%d ", numero/count);
            else
                printf("%d + ", numero/count);
            result += numero/count;
            numero -= (numero/count)*count;
        }
    }
    printf("= %d", result);
}
