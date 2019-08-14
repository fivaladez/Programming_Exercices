#include <stdio.h>
int mcd1(int m, int n);
int main()
{
    double decimal;
    int count=10000,i=1,j,mcd;
    double resultado;
    int salir = 1;

    int numerador, denominador;
    /* printf("Dame tu numero\n"); */
    scanf("%lf",&resultado);
    while (salir)
    {
        /* code */
        for ( j = 1; j <= count; j++)
        {
            decimal = (double)i/j;

                mcd = mcd1(i,j);
            //printf("%.5f",resultado);
            if ((resultado==decimal)&&(mcd==1))
            {
                numerador = i;
                denominador = j;
                salir=0;
            }
        }
        i++;
    }
    printf("%d/%d\n",numerador,denominador);
    return 0;
}

int mcd1(int m, int n)
{
   int r;

   r= m%n;
   if (r==0)
   {
        return n;
   }
   else
   {
        return mcd1(n,r);
   }
}
