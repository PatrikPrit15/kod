#include <iostream>
#include <queue>
#include <algorithm>
#include <array>
#include <string>
using namespace std;
int main (int argc, char *argv[])
{
    int hodz [10];
    int cieloveskore;
    int stop = 0;
    int vysledok;
    int aktualnei;
    int doc=1;
    int vys=0;
    for (int ia = 0; ia < 10; ++ia)
    {
      cin >> hodz[ia];
    }
    cin >> cieloveskore;
    int i =0;
    while (stop==0)
    {
        vysledok=0;
        if(i<10)
        {
            if (hodz[i]==cieloveskore){vysledok=i;
            stop=1;}
        }
        if(i>9)
        {
            aktualnei=i);
            while (stop==0)
            {
                doc=1;
                for(int i2=0;i2<sizeof(aktualnei);i2++)
                {

                    doc=doc*aktualnei[i2];
                    cout<<aktualnei[i2]<<" "<<doc<<endl;
                    if (doc == 0) {stop=1; break; }
                }
                aktualnei=doc;
            }
            stop=0;
            if (vysledok==cieloveskore){stop=1;}
            if (doc > 9) { vysledok += 1; }
            else { break; }
        }

        if (vysledok == cieloveskore) { vys = i; stop = 1; break; }
        i++;

        vysledok=0;
    }
    //cout<<vys<<endl;
}
