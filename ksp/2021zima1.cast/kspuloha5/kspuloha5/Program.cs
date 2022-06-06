using System;

namespace kspuloha5
{
    internal class Program
    {
        static void Main(string[] args)
        {
        string aktualnei = Console.ReadLine();
        string [] hodzstring =  aktualnei.Split(new char[] {' '});
        int [] hodz = new int [10];
        int stop = 0;
        int vysledok=0;
        int vys = 0;
        int doc = 1;
        int nas = 0;
        for (int ia = 0; ia < 10; ++ia)
        {
            hodz [ia]= Convert.ToInt32(hodzstring [ia]);
        }
        aktualnei = "";
        int cieloveskore = Convert.ToInt32(Console.ReadLine());
        int i = 0;
        while (stop == 0)
        {
            if (i < 10)
            {
                    
                if (hodz[i] == cieloveskore)
                {
                    vysledok = i;
                    vys= i;
                    stop = 1;
                        
                }
                
            }
            if (i >= 10)
            {
                    aktualnei =Convert.ToString(i);
                    vysledok = 1;
                    while (stop == 0)
                    {
                        doc = 1;
                        
                        for (int i2 = 0; i2 < aktualnei.Length; i2++)
                        {
                            
                            doc = doc *Convert.ToInt32( Convert.ToString(aktualnei[i2]));
                            //if (doc == 0) { break; }

                            
                        }
                        vysledok += 1;
                        aktualnei = Convert.ToString(doc);
                        if (doc<10) { stop = 1; }
                        
                    }
                    stop = 0;
                    
                    if (doc <10)
                    {
                            vysledok += hodz[doc]-1;
                            
                    }                             
            }
            if (vysledok == cieloveskore) { vys = i; stop = 1; break; }
            i++;
            vysledok = 0;
        }
        Console.WriteLine(vys);
    }

}
}

