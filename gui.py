# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Kontrol af magnet", pos = wx.DefaultPosition, size = wx.Size( 707,598 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Kontrol af magnet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0|wx.BORDER_SIMPLE )

		self.m_bpButton2.SetBitmap( wx.Bitmap( u"on.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer2.Add( self.m_bpButton2, 0, wx.ALL, 5 )

		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0|wx.BORDER_SIMPLE )

		self.m_bpButton3.SetBitmap( wx.Bitmap( u"off.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		bSizer2.Add( self.m_bpButton3, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Kontrol af motorer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Joint mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText14.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Motor ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

		id_choiceChoices = []
		self.id_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, id_choiceChoices, 0 )
		self.id_choice.SetSelection( 0 )
		bSizer3.Add( self.id_choice, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Position:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.spin_pos = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -150, 150, -16 )
		bSizer3.Add( self.spin_pos, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Gå til valgt position", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Wheel mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText12.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer6.Add( self.m_staticText12, 0, wx.ALL, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Vælg omgange, trin, hastighed og retning:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer7.Add( self.m_staticText10, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer7, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Omgange:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.spin_omgange = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 100, 0 )
		bSizer8.Add( self.spin_omgange, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Trin:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer8.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.spin_trin = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 100, 0 )
		bSizer8.Add( self.spin_trin, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Hastighed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer8.Add( self.m_staticText11, 0, wx.ALL, 5 )

		lst_hastighedChoices = [ u"200", u"400", u"600", u"800" ]
		self.lst_hastighed = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lst_hastighedChoices, 0 )
		bSizer8.Add( self.lst_hastighed, 0, wx.ALL, 5 )

		radio_retningChoices = [ u"Frem", u"Tilbage" ]
		self.radio_retning = wx.RadioBox( self, wx.ID_ANY, u"Retning", wx.DefaultPosition, wx.DefaultSize, radio_retningChoices, 1, wx.RA_SPECIFY_COLS )
		self.radio_retning.SetSelection( 0 )
		self.radio_retning.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer8.Add( self.radio_retning, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer8, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Motor ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		id_choice2Choices = []
		self.id_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, id_choice2Choices, 0 )
		self.id_choice2.SetSelection( 0 )
		bSizer5.Add( self.id_choice2, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Kør", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.m_menuItem1.GetId() )
		self.m_bpButton2.Bind( wx.EVT_BUTTON, self.OnOn )
		self.m_bpButton3.Bind( wx.EVT_BUTTON, self.OnOff )
		self.id_choice.Bind( wx.EVT_CHOICE, self.OnValg )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnGoto )
		self.id_choice2.Bind( wx.EVT_CHOICE, self.OnValg2 )
		self.m_button2.Bind( wx.EVT_BUTTON, self.run )
		self.m_button3.Bind( wx.EVT_BUTTON, self.stop )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnExit( self, event ):
		event.Skip()

	def OnOn( self, event ):
		event.Skip()

	def OnOff( self, event ):
		event.Skip()

	def OnValg( self, event ):
		event.Skip()

	def OnGoto( self, event ):
		event.Skip()

	def OnValg2( self, event ):
		event.Skip()

	def run( self, event ):
		event.Skip()

	def stop( self, event ):
		event.Skip()


