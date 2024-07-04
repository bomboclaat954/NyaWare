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
using System.Media;

namespace NyaWare
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            Random random = new Random();
            int x = random.Next(0, 1270);
            int y = random.Next(0, 920);
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(x, y);
            this.ShowInTaskbar = false;

            new Thread(() => {
                RandomPayload();
            }).Start();

            new Thread(() => {
                SoundPlayer player = new SoundPlayer(Properties.Resources.ahh);
                player.PlayLooping();
            }).Start();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        public void RandomPayload()
        {
            Payload payload  = new Payload();
            while (true) 
            {
                Random random = new Random();
                int x = random.Next(1, 6);
                switch(x)
                {
                    case 1:
                        payload.payload1();
                        break;
                    case 2:
                        payload.payload2();
                        break;
                }
                Thread.Sleep(10000);
            }
        }
    }
}
