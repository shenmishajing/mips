# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import os

import assembler


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(821, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_toolBar1 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.open = wx.StaticText(self.m_toolBar1, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0)
        self.open.Wrap(-1)

        self.m_toolBar1.AddControl(self.open)
        self.save = wx.StaticText(self.m_toolBar1, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        self.save.Wrap(-1)

        self.m_toolBar1.AddControl(self.save)
        self.assembler = wx.StaticText(self.m_toolBar1, wx.ID_ANY, u"assembler", wx.DefaultPosition, wx.DefaultSize, 0)
        self.assembler.Wrap(-1)

        self.m_toolBar1.AddControl(self.assembler)
        self.inv_assembler = wx.StaticText(self.m_toolBar1, wx.ID_ANY, u"inv_assembler", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.inv_assembler.Wrap(-1)

        self.m_toolBar1.AddControl(self.inv_assembler)
        self.m_toolBar1.Realize()

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.code_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, 530),
                                     wx.HSCROLL | wx.TE_MULTILINE)
        fgSizer1.Add(self.code_text, 0, wx.ALL, 5)

        self.binary_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, 530),
                                       wx.HSCROLL | wx.TE_MULTILINE)
        fgSizer1.Add(self.binary_text, 0, wx.ALL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.open.Bind(wx.EVT_LEFT_DOWN, self.open_click)
        self.save.Bind(wx.EVT_LEFT_DOWN, self.save_click)
        self.assembler.Bind(wx.EVT_LEFT_DOWN, self.assembler_click)
        self.inv_assembler.Bind(wx.EVT_LEFT_DOWN, self.inv_assembler_click)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def open_click(self, event):
        file_wildcard = "汇编文件(*.asm)|*.asm|二进制文件(*.bin)|*.bin|coe 文件(*.coe)|*.coe"
        dlg = wx.FileDialog(self, "打开文件",
                            os.getcwd(),
                            style=wx.FD_OPEN,
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if filename.endswith('asm'):
                f = open(filename, 'r')
                code = f.read()
                f.close()
                self.code_text.SetValue(code)
            else:
                if filename.endswith('bin'):
                    bin = []
                    f = open(filename, 'rb')
                    while True:
                        binary = int.from_bytes(f.read(4), byteorder='big')
                        if not binary:
                            break
                        bin.append(assembler.dec2bin(binary, length=32))
                else:
                    f = open(filename, 'r')
                    binary = f.read().split(';')
                    f.close()
                    base = int(binary[0][28:])
                    binary = binary[1][30:].split(',')
                    for i in range(len(binary)):
                        binary[i] = assembler.dec2bin(binary[i], length=32, base=base)
                    bin = binary

                binary = ''
                for b in bin:
                    binary += b + '\n'
                self.binary_text.SetValue(binary)
        dlg.Destroy()

    def save_click(self, event):
        file_wildcard = "汇编文件(*.asm)|*.asm|二进制文件(*.bin)|*.bin|coe 文件(*.coe)|*.coe"
        dlg = wx.FileDialog(self, "保存文件",
                            os.getcwd(),
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
                            wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if filename.endswith('asm'):
                f = open(filename, 'w')
                code = self.code_text.GetValue()
                f.write(code)
                f.close()
            else:
                if filename.endswith('bin'):
                    f = open(filename, 'wb')
                    binary = self.binary_text.GetValue().split('\n')
                    for b in binary:
                        if not b:
                            continue
                        f.write(bytes([int(b[:8], 2), int(b[8:16], 2), int(b[16:24], 2), int(b[24:], 2)]))
                    f.close()
                else:
                    f = open(filename, 'w')
                    f.write('MEMORY_INITIALIZATION_RADIX=16;\nMEMORY_INITIALIZATION_VECTOR=')
                    binary = self.binary_text.GetValue().split('\n')
                    for i, b in enumerate(binary):
                        if not b:
                            continue
                        if i:
                            f.write(',')
                        f.write(assembler.dec2hex(b, length=8, base=2))
                    f.write(';\n')
                    f.close()
        dlg.Destroy()

    def assembler_click(self, event):
        code = self.code_text.GetValue().split('\n')
        bin = assembler.assembler(code)
        binary = ''
        for b in bin:
            binary += b + '\n'
        self.binary_text.SetValue(binary)

    def inv_assembler_click(self, event):
        binary = self.binary_text.GetValue().split('\n')
        co = assembler.inv_assembler(binary)
        code = ''
        for c in co:
            code += c + '\n'
        self.code_text.SetValue(code)
