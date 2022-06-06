using System;

namespace uloha2ksp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            long[] vstup = new long[4];
            int aktualny = 0;
            string pis = "";
            string pis2 = "";
            int skoncenie = 0;
            int vysledok = 0;
            string a = Console.ReadLine();
            for (int i = 0; i < a.Length; i++)
            {
                if (Convert.ToString(a[i]) == " ")
                {
                    vstup[skoncenie] = Convert.ToInt32(pis);
                    if (skoncenie < 2) { vstup[skoncenie] = Convert.ToInt32(pis); }
                    skoncenie += 1;
                    pis = "";
                }
                else
                {

                    pis2 = Convert.ToString(a[i]);
                    pis += pis2;
                }

            }
            vstup[skoncenie] = Convert.ToInt32(pis);
            if (skoncenie == 2) { vstup[skoncenie] = Convert.ToInt32(pis); }
            skoncenie += 1;
            pis = "";

            long[] vstupzaloha = new long[4];
            for (int i = 0;i<4;i++)
            {
                vstupzaloha[i] =  vstup[i]; 
            }
            string inputzat = Console.ReadLine();
            int ano = 1;
            for (int i2 = 0; i2 < inputzat.Length; i2++)
            {
                if (Convert.ToString( inputzat[i2]) == "(")
                {
                    vstup[0] --; 
                }
                if (Convert.ToString(inputzat[i2]) == "{")
                {
                    vstup[1] --;
                }
                if (Convert.ToString(inputzat[i2]) == "<")
                {
                    vstup[2] --;
                }
                if (Convert.ToString(inputzat[i2]) == "[")
                {
                    vstup[3] --;
                }
                if (Convert.ToString(inputzat[i2]) == ")")
                {
                    vstup[0] ++;
                }
                if (Convert.ToString(inputzat[i2]) == "}")
                {
                    vstup[1] ++;
                }
                if (Convert.ToString(inputzat[i2]) == ">")
                {
                    vstup[2] ++;
                }
                if (Convert.ToString(inputzat[i2]) == "]")
                {
                    vstup[3] ++;
                }
                if (vstup[0] < 0 || vstup[1] < 0 || vstup[2] < 0 || vstup[3] < 0 || vstup[0] > vstupzaloha[0] || vstup[1] > vstupzaloha[1] || vstup[2] > vstupzaloha[2] || vstup[3] > vstupzaloha[3])
                {
                    Console.WriteLine("NIE");
                    ano = 0;
                    break;
                }
               // vstup[0] < 0 || vstup[1] < 0 || vstup[2] < 0 || vstup[3] < 0 ||
            }
            if (ano == 1)
            {
                if (vstup[0] == vstupzaloha[0] && vstup[1] == vstupzaloha[1] && vstup[2] == vstupzaloha[2] && vstup[3] == vstupzaloha[3])
                {
                    Console.WriteLine("ANO");
                }
                if (vstup[0] != vstupzaloha[0] || vstup[1] != vstupzaloha[1] || vstup[2] != vstupzaloha[2] || vstup[3] != vstupzaloha[3])
                {
                    Console.WriteLine("NIE");
                }
            }
            Console.ReadLine();
        }
    }
}
