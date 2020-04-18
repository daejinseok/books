using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace test_GetPrimeCount
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private async void Form1_Shown(object sender, EventArgs e)
        {
            Type t = listView1.GetType();
            PropertyInfo pi = t.GetProperty("DoubleBuffered", BindingFlags.Instance | BindingFlags.NonPublic); 
            pi.SetValue(listView1, true, null);

            await DisplayPrimeCountsAsync();



        }

        Task<int> GetPrimesCountAsync(int start, int count)
        {
            return Task.Run(() => ParallelEnumerable.Range(start, count).Count(n =>
               Enumerable.Range(2, (int)Math.Sqrt(n) - 1).All(i => n % i > 0)));
        }

        async Task DisplayPrimeCountsAsync()
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();

            const int OM = 1000000;
            for (int i = 0; i < 30; i++)
            {
                string pc = (await GetPrimesCountAsync(i * OM + 2, OM)).ToString();
                string start = (i * OM).ToString();
                string end = ((i + 1) * OM - 1).ToString();

                listView1.Items.Add($"{pc} primes between {start} and {end}");
                Console.WriteLine($"{pc} primes between {start} and {end}");
            }
            sw.Stop();
            string elapse_time = sw.ElapsedMilliseconds.ToString();
            Console.WriteLine($"Done! ( {elapse_time} )");
        }

        async private void button1_Click(object sender, EventArgs e)
        {
            await Task.Delay(5000);
            throw new Exception("예외!!");
        }
    }
}
