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
  sort (knihapos, knihapos + pocetpolicn);
  if (pocetpolicn > 100000 || dlzkapolices > 200000)
    {

   for (int i = 0; i < pocetpolicn; i++)
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
	    }
	  if (vys < vysledok)
	    {
	      vysledok = vys;
	    }
	    if (vys==0)
        {
            break;
        }
	    vysledkypn=1;
	    if (vysledok2==0&&vysledok1!=0)
	    {vysledok2=vys;
	    if (vysledok2==0)
	    {
	        i=dlzkapolices+1;
	        break;
	    }
	    if (vysledok1/vysledok2<1)
	    {i+=99000;
	    }
	    if (vysledok1/vysledok2>=1){i+=10000;}
	    vysledok2=0;
	    vysledok1=0;
	    vysledkypn=0;
	    }
	    if (vysledok1==0&&vysledkypn==1)
	    {vysledok=vys;}
        vysledkypn=1;
	  	  vys = 0;

	}
    }

  else
    {
        if()
      for (int i = 0; i < pocetpolicn; i ++)
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

		}
	      if (vys < vysledok)
		{
		  vysledok = vys;
		  poz=i;

		}
		vys=0;

	}
    }
  cout << vysledok << endl;
}

