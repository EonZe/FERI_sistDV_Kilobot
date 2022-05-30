using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;
using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;
using Emgu.CV.UI;

namespace ComPortV2
{
    public partial class Form1 : Form
    {
        /// <Variable>
        /// //////////////////////////////////////////////////////////////////////////////////////////////////
        /// </summary>
        string dataOUT;
        string dataIN;
        string valM1;
        string valM2;
        string R="P";
        string L=" ";
        string valM1send;
        string valM2send;
        string KiloBot1 = "0";
        string KiloBot2 = "1";
        string sendM1;
        string sendM2;
        string sendAll;


        /// <Emgu.CV>
        /// //////////////////////////////////////////////////////////////////////////////////////////////////
        /// </summary>
        //VideoCapture capWebcam = null;
        //bool blnCapturingInProcess = false;
        // Image<Bgr, Byte> imgOriginal;
        //Image<Gray, Byte> imgProcessed;
        public Form1()
        {
            InitializeComponent();
        }

       

        private void button3_Click(object sender, EventArgs e)
        {
            if(serialPort1.IsOpen)
            {
                dataOUT = tBoxDataOut.Text;
                serialPort1.Write(dataOUT);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] ports = SerialPort.GetPortNames();
            cBoxCOMPORT.Items.AddRange(ports);

            chBoxAddToOldData.Checked = false;
            chBoxAlwaysUpdate.Checked = true;
            SendValueM1.Checked = false;
            SendValueM2.Checked = false;
            checkBox1.Checked = true;
            checkBox2.Checked = false;
            /*
            try
            {
                capWebcam = new VideoCapture();
            }catch (NullReferenceException except)
            {
                txtBoxXYZ.Text = except.Message;
                return;
            }
            // one we have good capture object
            Application.Idle += processFrameAndUpdateGUI;
            blnCapturingInProcess = true;*/
        }
        /*
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if(capWebcam != null)
            {
                capWebcam.Dispose();
            }
        }
       /*
        void processFrameAndUpdateGUI(object sender, EventArgs arg)
        {
            
            //imgOriginal = capWebcam.QueryFrame(); // get the next frame from the webcam
            if (imgOriginal == null) return; //if we did not get a frame 

            imgProcessed = imgOriginal.InRange(new Bgr(0, 0, 175),  //min filter value
                                               new Bgr(100, 100, 256)); //max filter value

            imgProcessed = imgProcessed.SmoothGaussian(9);

            CircleF[] circles = imgProcessed.HoughCircles(new Gray(100),
                                                          new Gray(50),
                                                          2,
                                                          imgProcessed.Height / 4,
                                                          10,
                                                          400)[0];

            foreach(CircleF circle in circles)
            {
                if (txtBoxXYZ.Text != "") txtBoxXYZ.AppendText(Environment.NewLine);
                txtBoxXYZ.AppendText("Ball position = x" + circle.Center.X.ToString().PadLeft(4) +
                                                    "y=" + circle.Center.Y.ToString().PadLeft(4) +
                                            "y radius =" + circle.Radius.ToString("###.000").PadLeft(7));
                txtBoxXYZ.ScrollToCaret();
               
               /* CvInvoke.cvCircle(imgOriginal,
                                  new Point((int)circle.Center.X, (int)circle.Center.Y),
                                  3,
                                  new MCvScalar(0, 255, 0),
                                  -1,
                                  LineType.AntiAlias,
                                  0);
               
                imgOriginal.Draw(circle, new Bgr(Color.Red), 3);

                
            }
            ibOriginal.Image = imgOriginal;
            ibProcessed.Image = imgProcessed;
        }*/


        private void btnOPEN_Click(object sender, EventArgs e)
        {
            try
            {
                serialPort1.PortName = cBoxCOMPORT.Text;
                serialPort1.BaudRate = Convert.ToInt32(CBoxBaudRate.Text);
                serialPort1.DataBits = Convert.ToInt32(cBoxDataBits.Text);
                serialPort1.StopBits = (StopBits)Enum.Parse(typeof(StopBits), cBoxStopBits.Text);
                serialPort1.Parity = (Parity)Enum.Parse(typeof(Parity), CBoxParityBits.Text);

                serialPort1.Open();
                progressBar1.Value = 100;
            }

            catch (Exception err)
            {
                MessageBox.Show(err.Message,"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            
        }
        private void button2_Click(object sender, EventArgs e)
        {
            if(serialPort1.IsOpen)
            {
                serialPort1.Close();
                progressBar1.Value = 0;
            }
        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void SliderM1_ValueChanged(object sender, EventArgs e)
        {
            ValueM1.Text = SliderM1.Value.ToString();
        }

        private void SliderM2_ValueChanged(object sender, EventArgs e)
        {
            ValueM2.Text = SliderM2.Value.ToString();
        }

        private void serialPort1_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            dataIN = serialPort1.ReadExisting();
            this.Invoke(new EventHandler(ShowData));

        }

        private void ShowData(object sender, EventArgs e)
        {
            tBoxDataIn.Text = dataIN;
            if(chBoxAlwaysUpdate.Checked)
            {
                tBoxDataIn.Text = dataIN;
            }
            else if (chBoxAddToOldData.Checked)
            {
                tBoxDataIn.Text += dataIN;
            }
        }

        private void chBoxAlwaysUpdate_CheckedChanged(object sender, EventArgs e)
        {
            if (chBoxAlwaysUpdate.Checked)
            {
                chBoxAlwaysUpdate.Checked = true;
                chBoxAddToOldData.Checked = false;
            }
            else { chBoxAddToOldData.Checked = true; }
        }

        private void chBoxAddToOldData_CheckedChanged(object sender, EventArgs e)
        {
            if (chBoxAddToOldData.Checked)
            {
                chBoxAlwaysUpdate.Checked = false;
                chBoxAddToOldData.Checked = true;
            }
            else
            {
                chBoxAlwaysUpdate.Checked = true;
             }
        }

        private void btnDataIn_Click(object sender, EventArgs e)
        {
            if(tBoxDataIn.Text != "")
            {
                tBoxDataIn.Text = "";
            }
        }

        private void SendValueM1_CheckedChanged(object sender, EventArgs e)
        {
            if( SendValueM1.Checked)
            {
                SendValueM1.Checked = true;
            }
            else
            {
                SendValueM1.Checked = false;
            }
        }

        private void SendValueM2_CheckedChanged(object sender, EventArgs e)
        {
            if (SendValueM2.Checked)
            {
                SendValueM2.Checked = true;
            }
            else
            {
                SendValueM2.Checked = false;
            }
        }

        private void SliderM1_Scroll(object sender, EventArgs e)
        {
            valM1 = ValueM1.Text;
            if (SendValueM1.Checked)
            {/*
                if (valM1.Length < 4)
                    {




                    if (checkBox1.Checked)
                    {
                        serialPort1.Write(KiloBot1);
                        valM1send = "0" + valM1;
                        serialPort1.Write(R);
                        // serialPort1.Write(valM1);
                        serialPort1.Write(valM1send);
                        serialPort1.WriteLine(valM1send);
                    }
                    else if (checkBox2.Checked)
                    {
                        serialPort1.Write(KiloBot2);
                        valM1send = "0" + valM1;
                        serialPort1.Write(R);
                        // serialPort1.Write(valM1);
                        serialPort1.WriteLine(valM1send);

                    }

                }
                else 
                {
                    if (checkBox1.Checked)
                    {
                        serialPort1.Write(KiloBot1);
                        serialPort1.Write(R);
                        serialPort1.WriteLine(valM1);
                    }
                    else if (checkBox2.Checked)
                    {
                        serialPort1.Write(KiloBot2);
                        serialPort1.Write(R);
                        serialPort1.WriteLine(valM1);

                    }
                    
                }*/
                
                if (checkBox1.Checked)
                {
                    valM1send = KiloBot1 + "P";
                }
                else if (checkBox2.Checked)
                {
                    valM1send = KiloBot2 + "P";
                }
                if (valM1.Length < 4)
                {
                    sendM1 = valM1send + "0" + valM1;
                }
                else
                {
                    sendM1 = valM1send + valM1;
                }
                sendAll = sendM1 + " " + sendM2;
                serialPort1.WriteLine(sendAll);

            }
            
        }

        private void SliderM2_Scroll(object sender, EventArgs e)
        {
            valM2 = ValueM2.Text;
            /*if (SendValueM1.Checked)
            {
                serialPort1.Write(L);
                serialPort1.WriteLine(valM2);
            }
            */
            if (SendValueM2.Checked)
            {
                if (valM2.Length < 4)
                {

                    sendM2 = "0" + valM2;
                }
                else
                {
                    sendM2 = valM2;
                }
                sendAll = sendM1 + " " + sendM2;
                serialPort1.WriteLine(sendAll);

            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                checkBox1.Checked = true;
                checkBox2.Checked = false;
            }
            else
            {
                checkBox2.Checked = true;
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.Checked)
            {
                checkBox2.Checked = true;
                checkBox1.Checked = false;
            }
            else
            {
                checkBox1.Checked = true;
            }
        }

        /* private void btnPauseOrResume_Click(object sender, EventArgs e)
         {
             if(blnCapturingInProcess == true)
             {
                 Application.Idle -= processFrameAndUpdateGUI;
                 blnCapturingInProcess = false;
                 btnPauseOrResume.Text = "Resume";
             }
             else
             {
                 Application.Idle += processFrameAndUpdateGUI;
                 blnCapturingInProcess = true;
                 btnPauseOrResume.Text = "Pause";
             }
         }*/
    }
}
