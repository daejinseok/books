using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace test_Progress
{
    public partial class Form1 : Form
    {
        readonly Random r;
        CancellationTokenSource cts;

        public Form1()
        {
            InitializeComponent();
            r = new Random();
        }

        private async void button1_ClickAsync(object sender, EventArgs e)
        {
            btnStart.Enabled = false;
            btnStop.Enabled = true;
            cts = new CancellationTokenSource();

            Task t1 = PP_a_Async(progressBar1, label1, cts.Token);
            Task t2 = PP_a_Async(progressBar2, label2, cts.Token);
            Task t3 = PP_a_Async(progressBar3, label3, cts.Token);
            Task all = Task.WhenAll(t1, t2, t3);

            try
            {
                await all;
            }
            catch (OperationCanceledException) 
            { 

            }
            
            

            //int b_max = await GetRand(100, 10000);
            //int b_n = await GetRand(1, 100);

            //int c_max = await GetRand(100, 10000);
            //int c_n = await GetRand(1, 100);

            cts.Dispose();
            btnStop.Enabled = false;
            btnStart.Enabled = true;

        }

        private Task<int> GetRand(int minn, int maxn)
        {
            return Task.Run(() => { return r.Next(minn, maxn); });
        }

        async Task PP_a_Async(ProgressBar p1, Label l1, CancellationToken ct)
        {
            p1.Maximum = await this.GetRand(100, 10000);
            p1.Step = await this.GetRand(1, 100);

            for (int i = 0; i < p1.Maximum; i = i + p1.Step)
            {
                ct.ThrowIfCancellationRequested();

                await Task.Delay(p1.Step * 10);

                p1.Value = i;
                l1.Text = $"{(i * 100 / p1.Maximum)}% ({i} / {p1.Maximum})";
            }
        }

        private void btnStop_Click(object sender, EventArgs e)
        {
            cts?.Cancel();
        }
    }
}
