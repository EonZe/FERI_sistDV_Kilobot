
namespace ComPortV2
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.CBoxParityBits = new System.Windows.Forms.ComboBox();
            this.cBoxStopBits = new System.Windows.Forms.ComboBox();
            this.cBoxDataBits = new System.Windows.Forms.ComboBox();
            this.CBoxBaudRate = new System.Windows.Forms.ComboBox();
            this.cBoxCOMPORT = new System.Windows.Forms.ComboBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.progressBar1 = new System.Windows.Forms.ProgressBar();
            this.btnClose = new System.Windows.Forms.Button();
            this.btnOPEN = new System.Windows.Forms.Button();
            this.btnSendData = new System.Windows.Forms.Button();
            this.tBoxDataOut = new System.Windows.Forms.TextBox();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.SliderM1 = new System.Windows.Forms.TrackBar();
            this.SliderM2 = new System.Windows.Forms.TrackBar();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.ValueM1 = new System.Windows.Forms.TextBox();
            this.ValueM2 = new System.Windows.Forms.TextBox();
            this.SendValueM1 = new System.Windows.Forms.CheckBox();
            this.SendValueM2 = new System.Windows.Forms.CheckBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.chBoxAddToOldData = new System.Windows.Forms.CheckBox();
            this.chBoxAlwaysUpdate = new System.Windows.Forms.CheckBox();
            this.btnDataIn = new System.Windows.Forms.Button();
            this.tBoxDataIn = new System.Windows.Forms.TextBox();
            this.TransmitterControl = new System.Windows.Forms.GroupBox();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.checkBox2 = new System.Windows.Forms.CheckBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.SliderM1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.SliderM2)).BeginInit();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.TransmitterControl.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.CBoxParityBits);
            this.groupBox1.Controls.Add(this.cBoxStopBits);
            this.groupBox1.Controls.Add(this.cBoxDataBits);
            this.groupBox1.Controls.Add(this.CBoxBaudRate);
            this.groupBox1.Controls.Add(this.cBoxCOMPORT);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(209, 164);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "ComPortControl";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(7, 130);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(73, 13);
            this.label5.TabIndex = 9;
            this.label5.Text = "PARITY BITS";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(7, 106);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(63, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "STOP BITS";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(7, 79);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(63, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "DATA BITS";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(7, 52);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(69, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "BAUD RATE";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 25);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(64, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "COM PORT";
            // 
            // CBoxParityBits
            // 
            this.CBoxParityBits.FormattingEnabled = true;
            this.CBoxParityBits.Items.AddRange(new object[] {
            "None",
            "Odd",
            "Even"});
            this.CBoxParityBits.Location = new System.Drawing.Point(88, 130);
            this.CBoxParityBits.Name = "CBoxParityBits";
            this.CBoxParityBits.Size = new System.Drawing.Size(121, 21);
            this.CBoxParityBits.TabIndex = 4;
            this.CBoxParityBits.Text = "None";
            // 
            // cBoxStopBits
            // 
            this.cBoxStopBits.FormattingEnabled = true;
            this.cBoxStopBits.Items.AddRange(new object[] {
            "One",
            "Two"});
            this.cBoxStopBits.Location = new System.Drawing.Point(88, 103);
            this.cBoxStopBits.Name = "cBoxStopBits";
            this.cBoxStopBits.Size = new System.Drawing.Size(121, 21);
            this.cBoxStopBits.TabIndex = 3;
            this.cBoxStopBits.Text = "One";
            // 
            // cBoxDataBits
            // 
            this.cBoxDataBits.FormattingEnabled = true;
            this.cBoxDataBits.Items.AddRange(new object[] {
            "6",
            "7",
            "8"});
            this.cBoxDataBits.Location = new System.Drawing.Point(88, 76);
            this.cBoxDataBits.Name = "cBoxDataBits";
            this.cBoxDataBits.Size = new System.Drawing.Size(121, 21);
            this.cBoxDataBits.TabIndex = 2;
            this.cBoxDataBits.Text = "8";
            // 
            // CBoxBaudRate
            // 
            this.CBoxBaudRate.FormattingEnabled = true;
            this.CBoxBaudRate.Items.AddRange(new object[] {
            "4800",
            "9600",
            "115200"});
            this.CBoxBaudRate.Location = new System.Drawing.Point(88, 49);
            this.CBoxBaudRate.Name = "CBoxBaudRate";
            this.CBoxBaudRate.Size = new System.Drawing.Size(121, 21);
            this.CBoxBaudRate.TabIndex = 1;
            this.CBoxBaudRate.Text = "9600";
            // 
            // cBoxCOMPORT
            // 
            this.cBoxCOMPORT.FormattingEnabled = true;
            this.cBoxCOMPORT.Location = new System.Drawing.Point(88, 22);
            this.cBoxCOMPORT.Name = "cBoxCOMPORT";
            this.cBoxCOMPORT.Size = new System.Drawing.Size(121, 21);
            this.cBoxCOMPORT.TabIndex = 0;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.progressBar1);
            this.groupBox2.Controls.Add(this.btnClose);
            this.groupBox2.Controls.Add(this.btnOPEN);
            this.groupBox2.Location = new System.Drawing.Point(12, 182);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(137, 80);
            this.groupBox2.TabIndex = 10;
            this.groupBox2.TabStop = false;
            // 
            // progressBar1
            // 
            this.progressBar1.Location = new System.Drawing.Point(7, 48);
            this.progressBar1.Name = "progressBar1";
            this.progressBar1.Size = new System.Drawing.Size(116, 23);
            this.progressBar1.TabIndex = 2;
            // 
            // btnClose
            // 
            this.btnClose.Location = new System.Drawing.Point(67, 19);
            this.btnClose.Name = "btnClose";
            this.btnClose.Size = new System.Drawing.Size(56, 23);
            this.btnClose.TabIndex = 1;
            this.btnClose.Text = "CLOSE";
            this.btnClose.UseVisualStyleBackColor = true;
            this.btnClose.Click += new System.EventHandler(this.button2_Click);
            // 
            // btnOPEN
            // 
            this.btnOPEN.Location = new System.Drawing.Point(6, 19);
            this.btnOPEN.Name = "btnOPEN";
            this.btnOPEN.Size = new System.Drawing.Size(54, 23);
            this.btnOPEN.TabIndex = 0;
            this.btnOPEN.Text = "OPEN";
            this.btnOPEN.UseVisualStyleBackColor = true;
            this.btnOPEN.Click += new System.EventHandler(this.btnOPEN_Click);
            // 
            // btnSendData
            // 
            this.btnSendData.Location = new System.Drawing.Point(162, 182);
            this.btnSendData.Name = "btnSendData";
            this.btnSendData.Size = new System.Drawing.Size(59, 80);
            this.btnSendData.TabIndex = 11;
            this.btnSendData.Text = "Send Data";
            this.btnSendData.UseVisualStyleBackColor = true;
            this.btnSendData.Click += new System.EventHandler(this.button3_Click);
            // 
            // tBoxDataOut
            // 
            this.tBoxDataOut.Location = new System.Drawing.Point(6, 19);
            this.tBoxDataOut.Multiline = true;
            this.tBoxDataOut.Name = "tBoxDataOut";
            this.tBoxDataOut.Size = new System.Drawing.Size(208, 222);
            this.tBoxDataOut.TabIndex = 12;
            // 
            // serialPort1
            // 
            this.serialPort1.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort1_DataReceived);
            // 
            // SliderM1
            // 
            this.SliderM1.LargeChange = 10;
            this.SliderM1.Location = new System.Drawing.Point(12, 287);
            this.SliderM1.Maximum = 2000;
            this.SliderM1.Minimum = 500;
            this.SliderM1.Name = "SliderM1";
            this.SliderM1.Size = new System.Drawing.Size(435, 45);
            this.SliderM1.SmallChange = 10;
            this.SliderM1.TabIndex = 13;
            this.SliderM1.TickFrequency = 10;
            this.SliderM1.Value = 500;
            this.SliderM1.Scroll += new System.EventHandler(this.SliderM1_Scroll);
            this.SliderM1.ValueChanged += new System.EventHandler(this.SliderM1_ValueChanged);
            // 
            // SliderM2
            // 
            this.SliderM2.LargeChange = 10;
            this.SliderM2.Location = new System.Drawing.Point(12, 338);
            this.SliderM2.Maximum = 2000;
            this.SliderM2.Minimum = 500;
            this.SliderM2.Name = "SliderM2";
            this.SliderM2.Size = new System.Drawing.Size(435, 45);
            this.SliderM2.SmallChange = 10;
            this.SliderM2.TabIndex = 14;
            this.SliderM2.TickFrequency = 10;
            this.SliderM2.Value = 500;
            this.SliderM2.Scroll += new System.EventHandler(this.SliderM2_Scroll);
            this.SliderM2.ValueChanged += new System.EventHandler(this.SliderM2_ValueChanged);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(19, 271);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(43, 13);
            this.label6.TabIndex = 15;
            this.label6.Text = "Motor 1";
            this.label6.Click += new System.EventHandler(this.label6_Click);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(19, 319);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(43, 13);
            this.label7.TabIndex = 16;
            this.label7.Text = "Motor 2";
            // 
            // ValueM1
            // 
            this.ValueM1.Location = new System.Drawing.Point(68, 268);
            this.ValueM1.Name = "ValueM1";
            this.ValueM1.Size = new System.Drawing.Size(100, 20);
            this.ValueM1.TabIndex = 17;
            this.ValueM1.Text = "500";
            this.ValueM1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // ValueM2
            // 
            this.ValueM2.Location = new System.Drawing.Point(68, 316);
            this.ValueM2.Name = "ValueM2";
            this.ValueM2.Size = new System.Drawing.Size(100, 20);
            this.ValueM2.TabIndex = 18;
            this.ValueM2.Text = "500";
            // 
            // SendValueM1
            // 
            this.SendValueM1.AutoSize = true;
            this.SendValueM1.Location = new System.Drawing.Point(175, 271);
            this.SendValueM1.Name = "SendValueM1";
            this.SendValueM1.Size = new System.Drawing.Size(93, 17);
            this.SendValueM1.TabIndex = 19;
            this.SendValueM1.Text = "SendValueM1";
            this.SendValueM1.UseVisualStyleBackColor = true;
            this.SendValueM1.CheckedChanged += new System.EventHandler(this.SendValueM1_CheckedChanged);
            // 
            // SendValueM2
            // 
            this.SendValueM2.AutoSize = true;
            this.SendValueM2.Location = new System.Drawing.Point(175, 319);
            this.SendValueM2.Name = "SendValueM2";
            this.SendValueM2.Size = new System.Drawing.Size(93, 17);
            this.SendValueM2.TabIndex = 20;
            this.SendValueM2.Text = "SendValueM2";
            this.SendValueM2.UseVisualStyleBackColor = true;
            this.SendValueM2.CheckedChanged += new System.EventHandler(this.SendValueM2_CheckedChanged);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.groupBox4);
            this.groupBox3.Controls.Add(this.btnDataIn);
            this.groupBox3.Controls.Add(this.tBoxDataIn);
            this.groupBox3.Location = new System.Drawing.Point(453, 15);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(270, 344);
            this.groupBox3.TabIndex = 21;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Receiver Control";
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.chBoxAddToOldData);
            this.groupBox4.Controls.Add(this.chBoxAlwaysUpdate);
            this.groupBox4.Location = new System.Drawing.Point(98, 253);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(124, 65);
            this.groupBox4.TabIndex = 15;
            this.groupBox4.TabStop = false;
            // 
            // chBoxAddToOldData
            // 
            this.chBoxAddToOldData.AutoSize = true;
            this.chBoxAddToOldData.Location = new System.Drawing.Point(7, 38);
            this.chBoxAddToOldData.Name = "chBoxAddToOldData";
            this.chBoxAddToOldData.Size = new System.Drawing.Size(106, 17);
            this.chBoxAddToOldData.TabIndex = 1;
            this.chBoxAddToOldData.Text = "Add To Old Data";
            this.chBoxAddToOldData.UseVisualStyleBackColor = true;
            this.chBoxAddToOldData.CheckedChanged += new System.EventHandler(this.chBoxAddToOldData_CheckedChanged);
            // 
            // chBoxAlwaysUpdate
            // 
            this.chBoxAlwaysUpdate.AutoSize = true;
            this.chBoxAlwaysUpdate.Location = new System.Drawing.Point(7, 14);
            this.chBoxAlwaysUpdate.Name = "chBoxAlwaysUpdate";
            this.chBoxAlwaysUpdate.Size = new System.Drawing.Size(97, 17);
            this.chBoxAlwaysUpdate.TabIndex = 0;
            this.chBoxAlwaysUpdate.Text = "Always Update";
            this.chBoxAlwaysUpdate.UseVisualStyleBackColor = true;
            this.chBoxAlwaysUpdate.CheckedChanged += new System.EventHandler(this.chBoxAlwaysUpdate_CheckedChanged);
            // 
            // btnDataIn
            // 
            this.btnDataIn.Location = new System.Drawing.Point(33, 256);
            this.btnDataIn.Name = "btnDataIn";
            this.btnDataIn.Size = new System.Drawing.Size(59, 65);
            this.btnDataIn.TabIndex = 14;
            this.btnDataIn.Text = "Clear Data IN";
            this.btnDataIn.UseVisualStyleBackColor = true;
            this.btnDataIn.Click += new System.EventHandler(this.btnDataIn_Click);
            // 
            // tBoxDataIn
            // 
            this.tBoxDataIn.Location = new System.Drawing.Point(6, 22);
            this.tBoxDataIn.Multiline = true;
            this.tBoxDataIn.Name = "tBoxDataIn";
            this.tBoxDataIn.Size = new System.Drawing.Size(254, 219);
            this.tBoxDataIn.TabIndex = 13;
            // 
            // TransmitterControl
            // 
            this.TransmitterControl.Controls.Add(this.tBoxDataOut);
            this.TransmitterControl.Location = new System.Drawing.Point(227, 15);
            this.TransmitterControl.Name = "TransmitterControl";
            this.TransmitterControl.Size = new System.Drawing.Size(220, 250);
            this.TransmitterControl.TabIndex = 22;
            this.TransmitterControl.TabStop = false;
            this.TransmitterControl.Text = "TransmitterControl";
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Location = new System.Drawing.Point(747, 39);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(65, 17);
            this.checkBox1.TabIndex = 23;
            this.checkBox1.Text = "KiloBot1";
            this.checkBox1.UseVisualStyleBackColor = true;
            this.checkBox1.CheckedChanged += new System.EventHandler(this.checkBox1_CheckedChanged);
            // 
            // checkBox2
            // 
            this.checkBox2.AutoSize = true;
            this.checkBox2.Location = new System.Drawing.Point(747, 62);
            this.checkBox2.Name = "checkBox2";
            this.checkBox2.Size = new System.Drawing.Size(65, 17);
            this.checkBox2.TabIndex = 24;
            this.checkBox2.Text = "KiloBot2";
            this.checkBox2.UseVisualStyleBackColor = true;
            this.checkBox2.CheckedChanged += new System.EventHandler(this.checkBox2_CheckedChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1062, 622);
            this.Controls.Add(this.checkBox2);
            this.Controls.Add(this.checkBox1);
            this.Controls.Add(this.TransmitterControl);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.SendValueM2);
            this.Controls.Add(this.SendValueM1);
            this.Controls.Add(this.ValueM2);
            this.Controls.Add(this.ValueM1);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.SliderM2);
            this.Controls.Add(this.SliderM1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.btnSendData);
            this.Controls.Add(this.groupBox2);
            this.Name = "Form1";
            this.Text = "KiloBot Tester G2F";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.SliderM1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.SliderM2)).EndInit();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.TransmitterControl.ResumeLayout(false);
            this.TransmitterControl.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.ProgressBar progressBar1;
        private System.Windows.Forms.Button btnClose;
        private System.Windows.Forms.Button btnOPEN;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox CBoxParityBits;
        private System.Windows.Forms.ComboBox cBoxStopBits;
        private System.Windows.Forms.ComboBox cBoxDataBits;
        private System.Windows.Forms.ComboBox CBoxBaudRate;
        private System.Windows.Forms.ComboBox cBoxCOMPORT;
        private System.Windows.Forms.Button btnSendData;
        private System.Windows.Forms.TextBox tBoxDataOut;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.TrackBar SliderM1;
        private System.Windows.Forms.TrackBar SliderM2;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox ValueM1;
        private System.Windows.Forms.TextBox ValueM2;
        private System.Windows.Forms.CheckBox SendValueM1;
        private System.Windows.Forms.CheckBox SendValueM2;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.CheckBox chBoxAddToOldData;
        private System.Windows.Forms.CheckBox chBoxAlwaysUpdate;
        private System.Windows.Forms.Button btnDataIn;
        private System.Windows.Forms.TextBox tBoxDataIn;
        private System.Windows.Forms.GroupBox TransmitterControl;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.CheckBox checkBox2;
    }
}

