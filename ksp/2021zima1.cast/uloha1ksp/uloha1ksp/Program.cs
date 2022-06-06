using System;

namespace uloha1ksp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            decimal [] hodnota  = new decimal [9];
            decimal[] aktualny = new decimal[3];
            string n = "";
            string c = "";
            int skoncenie = 0;
            int vysledok = 0;
            int am = 500000000;
            for (int i = 0; i<3;i++)
            {
                string a = Console.ReadLine();
                for (int i2 = 0; i2 < a.Length;i2++)
                {
                    if (Convert.ToString(a[i2]) == " ")
                    {
                        hodnota[skoncenie] = Convert.ToInt32(c);
                        if (skoncenie < 2) { aktualny[skoncenie] = Convert.ToInt32(c); }
                        skoncenie += 1;
                        c = "";
                    }
                    else
                    {

                        n = Convert.ToString( a[i2]);
                        c = c + n;
                    }
                    
                }
                hodnota[skoncenie] = Convert.ToInt32(c);
                if (skoncenie == 2) { aktualny[skoncenie] = Convert.ToInt32(c); }
                skoncenie += 1;
                c = "";
            }
            int min = 50000000;
            int min2 = 500000000;
            decimal [] delene = new decimal [3];
            delene[0] = hodnota[0] / hodnota[3];
            delene[1] = hodnota[1] / hodnota[4];
            delene[2] = hodnota[2] / hodnota[5];
            decimal[] delene2 = new decimal[3];
            delene2[0] = hodnota[0] / hodnota[6];
            delene2[1] = hodnota[1] / hodnota[7];
            delene2[2] = hodnota[2] / hodnota[8];
            foreach(decimal a in delene)
            {
                if(a<min)
                {
                    min = Convert.ToInt32(Math.Floor(a));
                }
            }
            foreach (decimal b in delene2)
            {
                if (b < min2)
                {
                    min2 = Convert.ToInt32(Math.Floor(b));
                }
            }
            if(min > min2)
            {
                for (int i = 0; i < min; i++)
                {
                    aktualny[0] -= i * Convert.ToInt32(hodnota[3]);
                    aktualny[1] -= i * Convert.ToInt32(hodnota[4]);
                    aktualny[2] -= i * Convert.ToInt32(hodnota[5]);
                    aktualny[0] = Convert.ToInt32(Math.Floor(aktualny[0] / hodnota[6]));
                    aktualny[1] = Convert.ToInt32(Math.Floor(aktualny[1] / hodnota[7]));
                    aktualny[2] = Convert.ToInt32(Math.Floor(aktualny[2] / hodnota[8]));
                    foreach (int d in aktualny)
                    {
                        if (d < am)
                        {
                            am = d;
                        }
                    }
                     if (am + i > vysledok)
                    {
                        vysledok = am + i;
                    }
                    if (am < 1 && i + 1 > vysledok) //tu
                    {
                        vysledok = i+1;
                    }
                    aktualny[0] = Convert.ToInt32(hodnota[0]);
                    aktualny[1] = Convert.ToInt32(hodnota[1]);
                    aktualny[2] = Convert.ToInt32(hodnota[2]);
                    am = 500000000;
                }
               
            }
            else
            {
                for (int i = 0; i < min2; i++)
                {
                    aktualny[0] -= i * Convert.ToInt32(hodnota[6]);
                    aktualny[1] -= i * Convert.ToInt32(hodnota[7]);
                    aktualny[2] -= i * Convert.ToInt32(hodnota[8]);
                    aktualny[0] = Convert.ToInt32(Math.Floor(aktualny[0] / hodnota[3]));
                    aktualny[1] = Convert.ToInt32(Math.Floor(aktualny[1] / hodnota[4]));
                    aktualny[2] = Convert.ToInt32(Math.Floor(aktualny[2] / hodnota[5]));
                    foreach (int d in aktualny)
                    {
                        if (d < am)
                        {
                            am = d;
                        }
                    }
                    if (am + i > vysledok)
                    {
                        vysledok = am + i;
                    }
                    if (am < 1 && i+1>vysledok) //tu
                    {
                        vysledok = i+1;
                    }
                    aktualny[0] = Convert.ToInt32(hodnota[0]);
                    aktualny[1] = Convert.ToInt32(hodnota[1]);
                    aktualny[2] = Convert.ToInt32(hodnota[2]);
                    am = 500000000;
                }
                
            }
            Console.WriteLine(vysledok);
            Console.ReadLine();
        }
    }
}
