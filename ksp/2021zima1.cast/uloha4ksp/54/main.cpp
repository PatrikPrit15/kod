#include <iostream>
#include <queue>
#include <algorithm>
#include <array>
using namespace std;
int
main (int argc, char *argv[])
{
  int pocetpolicn;
  int dlzkapolices;
  int vysledok = 1000000000;
  int vys = 0;
  cin >> pocetpolicn >> dlzkapolices;
  int knihapos[pocetpolicn];
  int vyspos = 0;
  int poz=0;
  for (int i = 0; i < pocetpolicn; ++i)
    {
      cin >> knihapos[i];
    }
  sort (knihapos, knihapos + pocetpolicn);
  if (pocetpolicn > 1000 || dlzkapolices > 2000)
    {
      for (int i = 0; i < pocetpolicn; i +=300)
	{

	  for (int i = 0 ; i < pocetpolicn; i++)
	    {
	      for (int i2 = 0; i2 < pocetpolicn; i2++)
		{
		  if (knihapos[i2] > knihapos[i])
		    {
		      if (knihapos[i2] - knihapos[i] > dlzkapolices / 2)
			{
			  vys += dlzkapolices - (knihapos[i2] - knihapos[i]);
			}
		      else
			{
			  vys += knihapos[i2] - knihapos[i];
			}
		    }
		  if (knihapos[i2] < knihapos[i])
		    {
		      if (knihapos[i] - knihapos[i2] > dlzkapolices / 2)
			{
			  vys += dlzkapolices - (knihapos[i] - knihapos[i2]);
			}
		      else
			{
			  vys += knihapos[i] - knihapos[i2];
			}
		    }
		    if (vys >= vysledok){break;}
		}
	      if (vys < vysledok)
		{
		  vysledok = vys;

		}
		vys=0;
	    }
	}
    }

  else
    {
      for (int i = 0; i < dlzkapolices; i++)
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
	    }
	  if (vys < vysledok)
	    {
	      vysledok = vys;
	      poz = i;
	    }
	  vys = 0;
	}
    }
  cout << vysledok << endl;

}
