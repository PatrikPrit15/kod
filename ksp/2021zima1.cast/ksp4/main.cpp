#include <iostream>
#include <queue>
#include <algorithm>
#include <array>
using namespace std;
int main (int argc, char *argv[])
{
  int pocetpolicn;
  int dlzkapolices;
  int vysledok = 1000000000;
  int vys = 0;
  int vysledok1 =0;
  int vysledok2 = 0;
  cin >> pocetpolicn >> dlzkapolices;
  int knihapos[pocetpolicn];
  int vysledkypn=0;
  for (int i = 0; i < pocetpolicn; ++i)
    {
      cin >> knihapos[i];
    }
  //sort (knihapos, knihapos + pocetpolicn);

      for (int i = 0; i < dlzkapolices; i ++)
	{

	      for (int i2 = 0; i2 < pocetpolicn; i2++)
		{
		  if (knihapos[i2] > i)
		    {
		      if (knihapos[i2] - i > dlzkapolices / 2)
			{
			  vys += dlzkapolices - (knihapos[i2] - i);
			}
		      else
			{
			  vys += knihapos[i2] - i;
			}
		    }
		  if (knihapos[i2] < i)
		    {
		      if (i - knihapos[i2] > dlzkapolices / 2)
			{
			  vys += dlzkapolices - (i - knihapos[i2]);
			}
		      else
			{
			  vys += i - knihapos[i2];
			}
		    }
		    if (vys >= vysledok){break;}

		}
	      if (vys < vysledok)
		{
		  vysledok = vys;
		  }
		  if (vysledok==0){break;}
		vys=0;


	}

  cout << vysledok << endl;
}
