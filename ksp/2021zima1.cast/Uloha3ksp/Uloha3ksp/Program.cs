using System;

namespace Uloha3ksp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int[] d = new int[n];
            int[] dz = new int[n];
            int vysledok = 0;
            for (int i = 0; i < n; i++)
            {
                d[i] = Convert.ToInt32(Console.ReadLine());
                dz[i] = d[i];
            }
            int m = Convert.ToInt32(Console.ReadLine());
            int[] c = new int[m];
            int[] k = new int[m];
            string nic;
            string nn = "";
            string cc = "";
            int skoncenie = 0;
            int skoncenie2 = 0;
            for (int i2 = 0; i2 < m; i2++)
            {
                nic = Convert.ToString(Console.ReadLine());
                for (int i3 = 0; i3 < nic.Length; i3++)
                {
                    if (Convert.ToString(nic[i3]) == " ")
                    {
                        if (i3 != nic.Length - 1)
                        {
                            k[skoncenie] = Convert.ToInt32(cc);
                            skoncenie += 1;
                            cc = "";
                        }
                    }
                    else
                    {
                        nn = Convert.ToString(nic[i3]);
                        cc = cc + nn;

                    }
                }
                c[skoncenie2] = Convert.ToInt32(cc);
                skoncenie2 += 1;
                cc = "";
            }
            int aktualne_d = 0;
            int vys = 0;
            int prechod = 0;
            int zvysok = 0;
            int menc = 0;

            for (int i = 0; i < m; i++)
            {
                for (int i2 = 0; i2 < k[i]; i2++)
                {
                    menc = c[i];
                    while (prechod == 0)
                    {
                        vys =vys+1;
                        zvysok = menc - dz[aktualne_d];
                        if (zvysok == 0)
                        {
                            prechod = 1;
                            aktualne_d = aktualne_d+1;
                        }
                        if (zvysok > 0)
                        {
                            aktualne_d = aktualne_d+1;
                            menc = zvysok;
                        }
                        if (zvysok < 0)
                        {
                            prechod = 1;
                            if (-zvysok >= 2 * c[i] && i2 + 2 < k[i] && k[i] > 600)
                            {
                                
                                if (-zvysok / c[i] <= ((k[i] - i2) - 1))
                                {
                                    i2 += -zvysok / c[i];
                                    zvysok =  zvysok +  (c[i] * (-zvysok / c[i]));
                                    dz[aktualne_d] = -zvysok;
                                    if (dz[aktualne_d] == 0) { aktualne_d++; }
                                }
                                else
                                {
                                    zvysok +=  c[i] * (k[i] - i2 - 1);
                                    i2 += k[i] - i2 - 1;
                                    dz[aktualne_d] = -zvysok;
                                }
                            }
                            else
                            {
                                dz[aktualne_d] = (-zvysok);
                            }
                        }
                    }
                    prechod = 0;
                    if (vys > 1)
                    {
                        vysledok++;
                    }
                    vys = 0;
                }
            }
            Console.WriteLine(vysledok);
        }
    }
}