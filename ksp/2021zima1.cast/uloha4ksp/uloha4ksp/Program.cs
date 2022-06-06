using System;

namespace uloha4ksp
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 0;
            int s = 0;
            string nn = "";
            string c = "";
            int skoncenie = 0;
            string a = Console.ReadLine();
            for (int i2 = 0; i2 < a.Length; i2++)
            {
                if (Convert.ToString(a[i2]) == " ")
                {
                    n = Convert.ToInt32(c);
                    c = "";
                }
                else
                {
                    nn = Convert.ToString(a[i2]);
                    c = c + nn;
                }

            }
            s = Convert.ToInt32(c);
            c = "";
            int [] k = new int[n];
            string b = Console.ReadLine();
            string[] kstring = b.Split(new Char[] { ' ' });
            for (int i =0; i < n; i++)
            {
                k[i]=Convert.ToInt32(kstring[i]);
            }
            Array.Sort(k);
            c = "";
            long vysledok = 1000000000000000000;
            long dvysledok = 0;
           for (int i = 0; i < s; i++)
                {
                    for (int i2 = 0; i2 < n; i2++)
                    {
                        if (k[i2] > i)
                        {
                            if (k[i2] - i > s / 2)
                            {
                                dvysledok += s - (k[i2] - i);
                            }
                            else
                            {
                                dvysledok += k[i2] - i;
                            }
                        }
                        else
                        {
                            if (i - k[i2] > s / 2)
                            {
                                dvysledok += s - (i - k[i2]);
                            }
                            else
                            {
                                dvysledok += i - k[i2];
                            }
                        }
                        if (dvysledok >= vysledok)
                        {
                            break;
                        }
                    }
                    if (dvysledok < vysledok)
                    {
                        vysledok = dvysledok;
                    }
                    dvysledok = 0;

                }
            
            Console.WriteLine(vysledok);
            Console.ReadLine();
            }
        }
    }

