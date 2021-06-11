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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DERMA", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 1280,800 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.appName = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,60 ), wx.TAB_TRAVERSAL )
		self.appName.SetBackgroundColour( wx.Colour( 32, 223, 218 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap4 = wx.StaticBitmap( self.appName, wx.ID_ANY, wx.Bitmap( u"picture/LogoDERMA.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_bitmap4, 1, wx.ALIGN_CENTER, 5 )


		bSizer8.Add( bSizer9, 1, wx.ALIGN_CENTER, 5 )


		self.appName.SetSizer( bSizer8 )
		self.appName.Layout()
		fgSizer3.Add( self.appName, 1, wx.EXPAND, 5 )

		self.title = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 980,60 ), wx.BORDER_THEME|wx.TAB_TRAVERSAL )
		self.title.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer19.SetMinSize( wx.Size( 980,60 ) )
		self.menuName = wx.StaticText( self.title, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.menuName.Wrap( -1 )

		self.menuName.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer19.Add( self.menuName, 0, wx.ALIGN_CENTER|wx.LEFT, 50 )


		self.title.SetSizer( bSizer19 )
		self.title.Layout()
		fgSizer3.Add( self.title, 1, wx.EXPAND, 5 )

		self.sideFrame = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.sideFrame.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.sideFrame.SetForegroundColour( wx.Colour( 214, 255, 254 ) )
		self.sideFrame.SetBackgroundColour( wx.Colour( 32, 223, 218 ) )
		self.sideFrame.SetMinSize( wx.Size( 300,740 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer4.SetMinSize( wx.Size( 300,740 ) )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.sideFrame, wx.ID_ANY, u"Masukkan Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.m_staticText4.SetForegroundColour( wx.Colour( 204, 255, 254 ) )

		bSizer5.Add( self.m_staticText4, 0, wx.BOTTOM, 5 )

		self.searchEngine = wx.Panel( self.sideFrame, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.searchEngine.SetBackgroundColour( wx.Colour( 0, 203, 188 ) )
		self.searchEngine.SetMinSize( wx.Size( 240,35 ) )

		bSizer81 = wx.BoxSizer( wx.VERTICAL )

		bSizer81.SetMinSize( wx.Size( 240,35 ) )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap41 = wx.StaticBitmap( self.searchEngine, wx.ID_ANY, wx.Bitmap( u"picture/search.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bitmap41, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 10 )

		self.search = wx.TextCtrl( self.searchEngine, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.BORDER_NONE )
		self.search.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.search.SetForegroundColour( wx.Colour( 155, 235, 231 ) )
		self.search.SetBackgroundColour( wx.Colour( 25, 193, 173 ) )
		self.search.SetMinSize( wx.Size( 189,-1 ) )

		bSizer10.Add( self.search, 0, wx.ALIGN_CENTER, 13 )


		bSizer81.Add( bSizer10, 1, wx.ALIGN_CENTER, 5 )


		self.searchEngine.SetSizer( bSizer81 )
		self.searchEngine.Layout()
		bSizer81.Fit( self.searchEngine )
		bSizer5.Add( self.searchEngine, 0, wx.ALIGN_CENTER|wx.BOTTOM, 50 )

		self.dashboard_btn = wx.BitmapButton( self.sideFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE|wx.BORDER_NONE )

		self.dashboard_btn.SetBitmap( wx.Bitmap( u"picture/btn_pressed_dashboard.png", wx.BITMAP_TYPE_ANY ) )
		self.dashboard_btn.SetBitmapPressed( wx.Bitmap( u"picture/btn_pressed_dashboard.png", wx.BITMAP_TYPE_ANY ) )
		self.dashboard_btn.SetMinSize( wx.Size( 240,-1 ) )

		bSizer5.Add( self.dashboard_btn, 0, wx.ALIGN_CENTER, 50 )

		self.keluarga_btn = wx.BitmapButton( self.sideFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE|wx.BORDER_NONE )

		self.keluarga_btn.SetBitmap( wx.Bitmap( u"picture/btn_keluarga.png", wx.BITMAP_TYPE_ANY ) )
		self.keluarga_btn.SetBitmapPressed( wx.Bitmap( u"picture/btn_pressed_keluarga.png", wx.BITMAP_TYPE_ANY ) )
		self.keluarga_btn.SetMinSize( wx.Size( 240,-1 ) )

		bSizer5.Add( self.keluarga_btn, 0, wx.ALIGN_CENTER, 5 )

		self.rekom_btn = wx.BitmapButton( self.sideFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE|wx.BORDER_NONE )

		self.rekom_btn.SetBitmap( wx.Bitmap( u"picture/btn_rekomen.png", wx.BITMAP_TYPE_ANY ) )
		self.rekom_btn.SetBitmapPressed( wx.Bitmap( u"picture/btn_pressed_rekomen.png", wx.BITMAP_TYPE_ANY ) )
		self.rekom_btn.SetMinSize( wx.Size( 240,-1 ) )

		bSizer5.Add( self.rekom_btn, 0, wx.ALIGN_CENTER, 5 )

		self.rekap_btn = wx.BitmapButton( self.sideFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE|wx.BORDER_NONE )

		self.rekap_btn.SetBitmap( wx.Bitmap( u"picture/btn_rekap.png", wx.BITMAP_TYPE_ANY ) )
		self.rekap_btn.SetBitmapPressed( wx.Bitmap( u"picture/btn_pressed_rekap.png", wx.BITMAP_TYPE_ANY ) )
		self.rekap_btn.SetMinSize( wx.Size( 240,-1 ) )

		bSizer5.Add( self.rekap_btn, 0, wx.ALIGN_CENTER, 5 )


		bSizer4.Add( bSizer5, 1, wx.ALIGN_CENTER|wx.TOP, 20 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.tanggal = wx.StaticText( self.sideFrame, wx.ID_ANY, u"1 Januari 2021", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal.Wrap( -1 )

		bSizer15.Add( self.tanggal, 0, wx.ALIGN_CENTER|wx.BOTTOM|wx.TOP, 10 )


		bSizer4.Add( bSizer15, 0, wx.EXPAND, 5 )


		self.sideFrame.SetSizer( bSizer4 )
		self.sideFrame.Layout()
		bSizer4.Fit( self.sideFrame )
		fgSizer3.Add( self.sideFrame, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()
		fgSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.search.Bind( wx.EVT_TEXT_ENTER, self.searchEnter )
		self.dashboard_btn.Bind( wx.EVT_BUTTON, self.btn_dashboard_click )
		self.keluarga_btn.Bind( wx.EVT_BUTTON, self.btn_keluarga_click )
		self.rekom_btn.Bind( wx.EVT_BUTTON, self.btn_rekom_click )
		self.rekap_btn.Bind( wx.EVT_BUTTON, self.btn_rekap_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def searchEnter( self, event ):
		event.Skip()

	def btn_dashboard_click( self, event ):
		event.Skip()

	def btn_keluarga_click( self, event ):
		event.Skip()

	def btn_rekom_click( self, event ):
		event.Skip()

	def btn_rekap_click( self, event ):
		event.Skip()


###########################################################################
## Class dashboardPanel
###########################################################################

class dashboardPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.Point( 350,80 ), size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMaxSize( wx.Size( 880,-1 ) )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap6 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"picture/welcome_banner.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		bSizer17.Add( self.m_bitmap6, 0, 0, 20 )

		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_bpButton6 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0|wx.BORDER_NONE )

		self.m_bpButton6.SetBitmap( wx.Bitmap( u"picture/btn_lihatKeluargaDB.png", wx.BITMAP_TYPE_ANY ) )
		gSizer1.Add( self.m_bpButton6, 0, 0, 5 )

		self.m_bpButton7 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0|wx.BORDER_NONE )

		self.m_bpButton7.SetBitmap( wx.Bitmap( u"picture/btn_rekomenDB.png", wx.BITMAP_TYPE_ANY ) )
		gSizer1.Add( self.m_bpButton7, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 100 )

		self.m_bpButton8 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0|wx.BORDER_NONE )

		self.m_bpButton8.SetBitmap( wx.Bitmap( u"picture/btn_catatDB.png", wx.BITMAP_TYPE_ANY ) )
		gSizer1.Add( self.m_bpButton8, 0, wx.ALIGN_RIGHT, 5 )


		bSizer17.Add( gSizer1, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 20 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		dataKeluargaRendah = wx.BoxSizer( wx.VERTICAL )

		dataKeluargaRendah.SetMinSize( wx.Size( 410,-1 ) )
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Data Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		dataKeluargaRendah.Add( self.m_staticText6, 0, 0, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap7 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"picture/timer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		bSizer27.Add( self.m_bitmap7, 0, wx.ALIGN_CENTER, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"5 data dengan pendapatan terendah", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Roboto" ) )
		self.m_staticText8.SetForegroundColour( wx.Colour( 132, 133, 132 ) )

		bSizer27.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )


		dataKeluargaRendah.Add( bSizer27, 0, wx.LEFT, 2 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.namaRendah = wx.StaticText( self, wx.ID_ANY, u"1. Abdul Salim", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaRendah.Wrap( -1 )

		self.namaRendah.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.namaRendah.SetForegroundColour( wx.Colour( 133, 133, 133 ) )

		gSizer3.Add( self.namaRendah, 0, 0, 5 )

		self.gajiRendah = wx.StaticText( self, wx.ID_ANY, u"Rp500000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gajiRendah.Wrap( -1 )

		self.gajiRendah.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.gajiRendah.SetForegroundColour( wx.Colour( 132, 133, 132 ) )

		gSizer3.Add( self.gajiRendah, 0, wx.ALIGN_RIGHT, 30 )


		dataKeluargaRendah.Add( gSizer3, 1, wx.EXPAND|wx.TOP, 17 )


		bSizer14.Add( dataKeluargaRendah, 1, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 10,200 ), wx.LI_VERTICAL )
		bSizer14.Add( self.m_staticline2, 0, wx.LEFT|wx.RIGHT, 30 )

		riwayatBantuanBaru = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Riwayat Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		riwayatBantuanBaru.Add( self.m_staticText7, 0, 0, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap8 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"picture/timer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_bitmap8, 0, wx.ALIGN_CENTER, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"5 data terbaru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Roboto" ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 133, 133, 133 ) )

		bSizer28.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )


		riwayatBantuanBaru.Add( bSizer28, 0, wx.LEFT, 2 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.namaBaru = wx.StaticText( self, wx.ID_ANY, u"1. Rudi Amrullah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaBaru.Wrap( -1 )

		self.namaBaru.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.namaBaru.SetForegroundColour( wx.Colour( 133, 133, 133 ) )

		gSizer4.Add( self.namaBaru, 0, 0, 5 )

		self.bantuanBaru = wx.StaticText( self, wx.ID_ANY, u"Rp1200000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bantuanBaru.Wrap( -1 )

		self.bantuanBaru.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.bantuanBaru.SetForegroundColour( wx.Colour( 134, 133, 134 ) )

		gSizer4.Add( self.bantuanBaru, 0, wx.ALIGN_RIGHT, 5 )


		riwayatBantuanBaru.Add( gSizer4, 1, wx.EXPAND|wx.TOP, 17 )


		bSizer14.Add( riwayatBantuanBaru, 1, wx.EXPAND, 5 )


		bSizer17.Add( bSizer14, 1, wx.BOTTOM|wx.EXPAND, 46 )


		self.SetSizer( bSizer17 )
		self.Layout()
		bSizer17.Fit( self )

		# Connect Events
		self.m_bpButton6.Bind( wx.EVT_BUTTON, self.btn_keluargaDB_click )
		self.m_bpButton7.Bind( wx.EVT_BUTTON, self.btn_rekomDB_click )
		self.m_bpButton8.Bind( wx.EVT_BUTTON, self.btn_catatDB_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_keluargaDB_click( self, event ):
		event.Skip()

	def btn_rekomDB_click( self, event ):
		event.Skip()

	def btn_catatDB_click( self, event ):
		event.Skip()


###########################################################################
## Class dataKeluargaPanel
###########################################################################

class dataKeluargaPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.Point( 300,60 ), size = wx.Size( 980,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMaxSize( wx.Size( 980,-1 ) )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_THEME|wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 133, 133, 133 ) )

		bSizer18.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.LEFT, 50 )

		m_comboBox5Choices = []
		self.m_comboBox5 = wx.ComboBox( self.m_panel7, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox5Choices, 0 )
		self.m_comboBox5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.m_comboBox5.SetForegroundColour( wx.Colour( 133, 133, 133 ) )

		bSizer18.Add( self.m_comboBox5, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 20 )

		self.m_bpButton14 = wx.BitmapButton( self.m_panel7, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW|0|wx.BORDER_NONE )

		self.m_bpButton14.SetBitmap( wx.Bitmap( u"picture/btn_apply.png", wx.BITMAP_TYPE_ANY ) )
		bSizer18.Add( self.m_bpButton14, 0, wx.BOTTOM|wx.TOP, 10 )


		self.m_panel7.SetSizer( bSizer18 )
		self.m_panel7.Layout()
		bSizer18.Fit( self.m_panel7 )
		bSizer17.Add( self.m_panel7, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		# Connect Events
		self.m_comboBox5.Bind( wx.EVT_COMBOBOX, self.filterOneSelected )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def filterOneSelected( self, event ):
		event.Skip()


