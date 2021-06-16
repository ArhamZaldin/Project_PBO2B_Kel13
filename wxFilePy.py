# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

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

		self.top = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 980,60 ), wx.BORDER_THEME|wx.TAB_TRAVERSAL )
		self.top.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.top.SetMinSize( wx.Size( 980,60 ) )

		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer57.SetMinSize( wx.Size( 980,60 ) )
		self.titleMenu = wx.StaticText( self.top, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titleMenu.Wrap( -1 )

		self.titleMenu.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer57.Add( self.titleMenu, 0, wx.ALIGN_CENTER|wx.LEFT, 50 )


		self.top.SetSizer( bSizer57 )
		self.top.Layout()
		fgSizer3.Add( self.top, 1, wx.EXPAND, 5 )

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

		self.searchPanel = wx.Panel( self.sideFrame, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.searchPanel.SetBackgroundColour( wx.Colour( 0, 203, 188 ) )
		self.searchPanel.SetMinSize( wx.Size( 240,35 ) )

		bSizer81 = wx.BoxSizer( wx.VERTICAL )

		bSizer81.SetMinSize( wx.Size( 240,35 ) )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap41 = wx.StaticBitmap( self.searchPanel, wx.ID_ANY, wx.Bitmap( u"picture/search.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bitmap41, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 10 )

		self.searchEngine = wx.TextCtrl( self.searchPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.BORDER_NONE )
		self.searchEngine.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.searchEngine.SetForegroundColour( wx.Colour( 155, 235, 231 ) )
		self.searchEngine.SetBackgroundColour( wx.Colour( 25, 193, 173 ) )
		self.searchEngine.SetMinSize( wx.Size( 189,-1 ) )

		bSizer10.Add( self.searchEngine, 0, wx.ALIGN_CENTER, 13 )


		bSizer81.Add( bSizer10, 1, wx.ALIGN_CENTER, 5 )


		self.searchPanel.SetSizer( bSizer81 )
		self.searchPanel.Layout()
		bSizer81.Fit( self.searchPanel )
		bSizer5.Add( self.searchPanel, 0, wx.ALIGN_CENTER|wx.BOTTOM, 50 )

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
		self.searchEngine.Bind( wx.EVT_TEXT_ENTER, self.searchEnter )
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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.Point( 350,80 ), size = wx.Size( 880,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 880,720 ) )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap6 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"picture/welcome_banner.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		bSizer17.Add( self.m_bitmap6, 0, 0, 20 )

		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_bitmap61 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"picture/btn_lihatKeluargaDB.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap61, 0, 0, 5 )

		self.m_bitmap71 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"picture/btn_rekomenDB.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap71, 0, wx.ALIGN_CENTER, 5 )

		self.m_bitmap81 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"picture/btn_catatDB.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap81, 0, wx.ALIGN_RIGHT, 5 )


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

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Terurut dari yang terendah", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Roboto" ) )
		self.m_staticText8.SetForegroundColour( wx.Colour( 132, 133, 132 ) )

		bSizer27.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )


		dataKeluargaRendah.Add( bSizer27, 0, wx.LEFT, 2 )

		self.keluargaRendah = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.keluargaRendah.CreateGrid( 0, 2 )
		self.keluargaRendah.EnableEditing( False )
		self.keluargaRendah.EnableGridLines( False )
		self.keluargaRendah.EnableDragGridSize( False )
		self.keluargaRendah.SetMargins( 0, 0 )

		# Columns
		self.keluargaRendah.EnableDragColMove( False )
		self.keluargaRendah.EnableDragColSize( False )
		self.keluargaRendah.SetColLabelSize( 0 )
		self.keluargaRendah.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.keluargaRendah.EnableDragRowSize( False )
		self.keluargaRendah.SetRowLabelSize( 0 )
		self.keluargaRendah.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.keluargaRendah.SetDefaultCellTextColour( wx.Colour( 100, 100, 100 ) )
		self.keluargaRendah.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.keluargaRendah.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		dataKeluargaRendah.Add( self.keluargaRendah, 1, wx.TOP|wx.EXPAND, 17 )


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

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Terurut dari yang terbaru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Roboto" ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 133, 133, 133 ) )

		bSizer28.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )


		riwayatBantuanBaru.Add( bSizer28, 0, wx.LEFT, 2 )

		self.bantuanBaru = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.bantuanBaru.CreateGrid( 0, 2 )
		self.bantuanBaru.EnableEditing( False )
		self.bantuanBaru.EnableGridLines( False )
		self.bantuanBaru.EnableDragGridSize( False )
		self.bantuanBaru.SetMargins( 0, 0 )

		# Columns
		self.bantuanBaru.EnableDragColMove( False )
		self.bantuanBaru.EnableDragColSize( False )
		self.bantuanBaru.SetColLabelSize( 0 )
		self.bantuanBaru.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.bantuanBaru.EnableDragRowSize( False )
		self.bantuanBaru.SetRowLabelSize( 0 )
		self.bantuanBaru.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.bantuanBaru.SetDefaultCellTextColour( wx.Colour( 100, 100, 100 ) )
		self.bantuanBaru.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.bantuanBaru.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		riwayatBantuanBaru.Add( self.bantuanBaru, 1, wx.TOP|wx.EXPAND, 17 )


		bSizer14.Add( riwayatBantuanBaru, 1, wx.EXPAND, 5 )


		bSizer17.Add( bSizer14, 1, wx.BOTTOM|wx.EXPAND, 46 )


		self.SetSizer( bSizer17 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class dataKeluargaPanel
###########################################################################

class dataKeluargaPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.Point( 300,60 ), size = wx.Size( 980,740 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 980,740 ) )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		bSizer17.SetMinSize( wx.Size( 980,740 ) )
		self.filterPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.BORDER_THEME|wx.TAB_TRAVERSAL )
		self.filterPanel.SetMaxSize( wx.Size( -1,50 ) )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer18.SetMinSize( wx.Size( -1,100 ) )
		bSizer56 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( self.filterPanel, wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

		bSizer56.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.LEFT, 50 )

		filterSatuChoices = [ u"Tidak Ada", u"Total Pendapatan", u"Anggota Keluarga" ]
		self.filterSatu = wx.Choice( self.filterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, filterSatuChoices, 0 )
		self.filterSatu.SetSelection( 0 )
		self.filterSatu.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.filterSatu.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.filterSatu.SetMinSize( wx.Size( 140,-1 ) )

		bSizer56.Add( self.filterSatu, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 10 )

		filterDuaChoices = [ u"Lebih Dari", u"Kurang Dari" ]
		self.filterDua = wx.Choice( self.filterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, filterDuaChoices, 0 )
		self.filterDua.SetSelection( 0 )
		self.filterDua.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.filterDua.SetMinSize( wx.Size( 100,-1 ) )

		bSizer56.Add( self.filterDua, 0, wx.ALIGN_CENTER, 5 )

		self.filterValue = wx.TextCtrl( self.filterPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.filterValue.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.filterValue.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

		bSizer56.Add( self.filterValue, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 10 )


		bSizer18.Add( bSizer56, 0, wx.EXPAND, 5 )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton23 = wx.BitmapButton( self.filterPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0|wx.BORDER_NONE )

		self.m_bpButton23.SetBitmap( wx.Bitmap( u"picture/tambah.png", wx.BITMAP_TYPE_ANY ) )
		bSizer58.Add( self.m_bpButton23, 0, 0, 10 )

		self.m_bpButton26 = wx.BitmapButton( self.filterPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE|wx.BORDER_NONE )

		self.m_bpButton26.SetBitmap( wx.Bitmap( u"picture/btn_ubah.png", wx.BITMAP_TYPE_ANY ) )
		bSizer58.Add( self.m_bpButton26, 0, wx.LEFT|wx.RIGHT, 5 )

		self.m_bpButton25 = wx.BitmapButton( self.filterPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE|wx.BORDER_NONE )

		self.m_bpButton25.SetBitmap( wx.Bitmap( u"picture/btn_hapus.png", wx.BITMAP_TYPE_ANY ) )
		bSizer58.Add( self.m_bpButton25, 0, wx.RIGHT, 50 )


		bSizer57.Add( bSizer58, 0, wx.ALIGN_RIGHT, 5 )


		bSizer18.Add( bSizer57, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.filterPanel.SetSizer( bSizer18 )
		self.filterPanel.Layout()
		bSizer18.Fit( self.filterPanel )
		bSizer17.Add( self.filterPanel, 0, wx.BOTTOM|wx.EXPAND, 20 )

		sizerForGrid = wx.BoxSizer( wx.VERTICAL )

		self.dataKeluargaGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataKeluargaGrid.CreateGrid( 0, 5 )
		self.dataKeluargaGrid.EnableEditing( False )
		self.dataKeluargaGrid.EnableGridLines( True )
		self.dataKeluargaGrid.EnableDragGridSize( False )
		self.dataKeluargaGrid.SetMargins( 0, 0 )

		# Columns
		self.dataKeluargaGrid.EnableDragColMove( False )
		self.dataKeluargaGrid.EnableDragColSize( False )
		self.dataKeluargaGrid.SetColLabelSize( 30 )
		self.dataKeluargaGrid.SetColLabelValue( 0, u"Nomor KK" )
		self.dataKeluargaGrid.SetColLabelValue( 1, u"Kepala Keluarga" )
		self.dataKeluargaGrid.SetColLabelValue( 2, u"Anggota Keluarga" )
		self.dataKeluargaGrid.SetColLabelValue( 3, u"Total Pendapatan" )
		self.dataKeluargaGrid.SetColLabelValue( 4, u"Alamat" )
		self.dataKeluargaGrid.SetColLabelValue( 5, wx.EmptyString )
		self.dataKeluargaGrid.SetColLabelValue( 6, wx.EmptyString )
		self.dataKeluargaGrid.SetColLabelValue( 7, wx.EmptyString )
		self.dataKeluargaGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataKeluargaGrid.EnableDragRowSize( False )
		self.dataKeluargaGrid.SetRowLabelSize( 60 )
		self.dataKeluargaGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.dataKeluargaGrid.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.dataKeluargaGrid.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )
		self.dataKeluargaGrid.SetLabelTextColour( wx.Colour( 100, 100, 100 ) )

		# Cell Defaults
		self.dataKeluargaGrid.SetDefaultCellTextColour( wx.Colour( 100, 100, 100 ) )
		self.dataKeluargaGrid.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.dataKeluargaGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		self.dataKeluargaGrid.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.dataKeluargaGrid.SetMinSize( wx.Size( 880,-1 ) )

		sizerForGrid.Add( self.dataKeluargaGrid, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 50 )


		bSizer17.Add( sizerForGrid, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		# Connect Events
		self.filterSatu.Bind( wx.EVT_CHOICE, self.filterOneSelected )
		self.filterValue.Bind( wx.EVT_TEXT, self.filterValueChange )
		self.m_bpButton23.Bind( wx.EVT_BUTTON, self.btn_tambahData )
		self.m_bpButton26.Bind( wx.EVT_BUTTON, self.btn_ubahData )
		self.m_bpButton25.Bind( wx.EVT_BUTTON, self.btn_hapusData )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def filterOneSelected( self, event ):
		event.Skip()

	def filterValueChange( self, event ):
		event.Skip()

	def btn_tambahData( self, event ):
		event.Skip()

	def btn_ubahData( self, event ):
		event.Skip()

	def btn_hapusData( self, event ):
		event.Skip()


###########################################################################
## Class addData
###########################################################################

class addData ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 402,380 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		self.m_staticText63.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer59.Add( self.m_staticText63, 0, wx.LEFT|wx.TOP, 20 )

		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		self.m_staticText65.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer60.Add( self.m_staticText65, 1, wx.ALIGN_CENTER, 5 )

		self.nomorKK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.nomorKK, 0, wx.ALIGN_CENTER, 5 )


		bSizer59.Add( bSizer60, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 20 )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"Kepala Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )

		self.m_staticText66.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer61.Add( self.m_staticText66, 1, wx.ALIGN_CENTER, 10 )

		self.kepKeluarga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.kepKeluarga, 0, wx.ALIGN_CENTER, 5 )


		bSizer59.Add( bSizer61, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 20 )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"NIK Kepala Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer66.Add( self.m_staticText45, 1, wx.ALIGN_CENTER, 5 )

		self.nikKepala = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.nikKepala, 0, wx.ALIGN_CENTER, 5 )


		bSizer59.Add( bSizer66, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 20 )

		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText67 = wx.StaticText( self, wx.ID_ANY, u"Anggota Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )

		self.m_staticText67.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer62.Add( self.m_staticText67, 1, wx.ALIGN_CENTER, 5 )

		self.jumAnggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.jumAnggota, 0, wx.ALIGN_CENTER, 5 )


		bSizer59.Add( bSizer62, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 20 )

		bSizer64 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, u"Total Pendapatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		self.m_staticText68.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer64.Add( self.m_staticText68, 1, wx.ALIGN_CENTER, 5 )

		self.totalPendapatan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer64.Add( self.totalPendapatan, 0, wx.ALIGN_CENTER, 5 )


		bSizer59.Add( bSizer64, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 20 )

		bSizer65 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		self.m_staticText69.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer65.Add( self.m_staticText69, 1, wx.ALIGN_CENTER, 5 )

		self.alamatBaru = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer65.Add( self.alamatBaru, 0, wx.ALIGN_CENTER, 5 )


		bSizer59.Add( bSizer65, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 20 )

		self.m_bpButton27 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton27.SetBitmap( wx.Bitmap( u"picture/tambah.png", wx.BITMAP_TYPE_ANY ) )
		bSizer59.Add( self.m_bpButton27, 0, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 15 )


		self.SetSizer( bSizer59 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_bpButton27.Bind( wx.EVT_BUTTON, self.btn_addKeluarga )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_addKeluarga( self, event ):
		event.Skip()


###########################################################################
## Class changeData
###########################################################################

class changeData ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 402,290 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer66 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText70 = wx.StaticText( self, wx.ID_ANY, u"Ubah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )

		self.m_staticText70.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer66.Add( self.m_staticText70, 0, wx.LEFT|wx.TOP, 10 )

		self.ubahNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ubahAnggota = wx.Panel( self.ubahNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer67 = wx.BoxSizer( wx.VERTICAL )

		bSizer75 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText71 = wx.StaticText( self.ubahAnggota, wx.ID_ANY, u"Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		self.m_staticText71.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer75.Add( self.m_staticText71, 1, wx.ALIGN_CENTER, 10 )

		self.nomorKK_anggota = wx.TextCtrl( self.ubahAnggota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.nomorKK_anggota, 0, 0, 5 )


		bSizer67.Add( bSizer75, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer73 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText73 = wx.StaticText( self.ubahAnggota, wx.ID_ANY, u"Nama Anggota Baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )

		self.m_staticText73.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer73.Add( self.m_staticText73, 1, wx.ALIGN_CENTER, 5 )

		self.namaAnggota = wx.TextCtrl( self.ubahAnggota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer73.Add( self.namaAnggota, 0, 0, 5 )


		bSizer67.Add( bSizer73, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer72 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText74 = wx.StaticText( self.ubahAnggota, wx.ID_ANY, u"NIK Anggota Baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		self.m_staticText74.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer72.Add( self.m_staticText74, 1, wx.ALIGN_CENTER, 5 )

		self.nikAnggota = wx.TextCtrl( self.ubahAnggota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer72.Add( self.nikAnggota, 0, 0, 5 )


		bSizer67.Add( bSizer72, 0, wx.ALL|wx.EXPAND, 10 )

		self.m_bpButton28 = wx.BitmapButton( self.ubahAnggota, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton28.SetBitmap( wx.Bitmap( u"picture/btn_ubah.png", wx.BITMAP_TYPE_ANY ) )
		bSizer67.Add( self.m_bpButton28, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 10 )


		self.ubahAnggota.SetSizer( bSizer67 )
		self.ubahAnggota.Layout()
		bSizer67.Fit( self.ubahAnggota )
		self.ubahNotebook.AddPage( self.ubahAnggota, u"a page", False )
		self.ubahTotal = wx.Panel( self.ubahNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer76 = wx.BoxSizer( wx.VERTICAL )

		bSizer78 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText78 = wx.StaticText( self.ubahTotal, wx.ID_ANY, u"Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		self.m_staticText78.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer78.Add( self.m_staticText78, 1, wx.ALIGN_CENTER, 10 )

		self.nomorKK_total = wx.TextCtrl( self.ubahTotal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78.Add( self.nomorKK_total, 0, 0, 5 )


		bSizer76.Add( bSizer78, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer77 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText77 = wx.StaticText( self.ubahTotal, wx.ID_ANY, u"Total Pendapatan Baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		self.m_staticText77.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer77.Add( self.m_staticText77, 1, wx.ALIGN_CENTER, 10 )

		self.totalBaru = wx.TextCtrl( self.ubahTotal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer77.Add( self.totalBaru, 0, 0, 5 )


		bSizer76.Add( bSizer77, 0, wx.ALL|wx.EXPAND, 10 )

		self.m_bpButton29 = wx.BitmapButton( self.ubahTotal, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton29.SetBitmap( wx.Bitmap( u"picture/btn_ubah.png", wx.BITMAP_TYPE_ANY ) )
		bSizer76.Add( self.m_bpButton29, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 10 )


		self.ubahTotal.SetSizer( bSizer76 )
		self.ubahTotal.Layout()
		bSizer76.Fit( self.ubahTotal )
		self.ubahNotebook.AddPage( self.ubahTotal, u"a page", False )
		self.ubahAlamat = wx.Panel( self.ubahNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		bSizer80 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText79 = wx.StaticText( self.ubahAlamat, wx.ID_ANY, u"Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		self.m_staticText79.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer80.Add( self.m_staticText79, 1, wx.ALIGN_CENTER, 10 )

		self.nomorKK_alamat = wx.TextCtrl( self.ubahAlamat, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.nomorKK_alamat, 0, 0, 5 )


		bSizer79.Add( bSizer80, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText80 = wx.StaticText( self.ubahAlamat, wx.ID_ANY, u"Alamat Baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		self.m_staticText80.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer81.Add( self.m_staticText80, 1, wx.ALIGN_CENTER, 5 )

		self.alamatBaru = wx.TextCtrl( self.ubahAlamat, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer81.Add( self.alamatBaru, 0, 0, 5 )


		bSizer79.Add( bSizer81, 0, wx.ALL|wx.EXPAND, 10 )

		self.m_bpButton30 = wx.BitmapButton( self.ubahAlamat, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton30.SetBitmap( wx.Bitmap( u"picture/btn_ubah.png", wx.BITMAP_TYPE_ANY ) )
		bSizer79.Add( self.m_bpButton30, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 10 )


		self.ubahAlamat.SetSizer( bSizer79 )
		self.ubahAlamat.Layout()
		bSizer79.Fit( self.ubahAlamat )
		self.ubahNotebook.AddPage( self.ubahAlamat, u"a page", False )

		bSizer66.Add( self.ubahNotebook, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer66 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_bpButton28.Bind( wx.EVT_BUTTON, self.btn_ubahAnggota )
		self.m_bpButton29.Bind( wx.EVT_BUTTON, self.btn_ubahTotal )
		self.m_bpButton30.Bind( wx.EVT_BUTTON, self.btn_ubahAlamat )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_ubahAnggota( self, event ):
		event.Skip()

	def btn_ubahTotal( self, event ):
		event.Skip()

	def btn_ubahAlamat( self, event ):
		event.Skip()


###########################################################################
## Class delData
###########################################################################

class delData ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 402,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Hapus Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer52.Add( self.m_staticText38, 0, wx.LEFT|wx.TOP, 10 )

		self.delNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.delKeluarga = wx.Panel( self.delNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer54 = wx.BoxSizer( wx.VERTICAL )

		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText39 = wx.StaticText( self.delKeluarga, wx.ID_ANY, u"Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer55.Add( self.m_staticText39, 1, wx.ALIGN_CENTER, 5 )

		self.nomorKK_keluarga = wx.TextCtrl( self.delKeluarga, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer55.Add( self.nomorKK_keluarga, 0, 0, 5 )


		bSizer54.Add( bSizer55, 0, wx.ALL|wx.EXPAND, 10 )

		self.m_bpButton19 = wx.BitmapButton( self.delKeluarga, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton19.SetBitmap( wx.Bitmap( u"picture/btn_hapus.png", wx.BITMAP_TYPE_ANY ) )
		bSizer54.Add( self.m_bpButton19, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 10 )


		self.delKeluarga.SetSizer( bSizer54 )
		self.delKeluarga.Layout()
		bSizer54.Fit( self.delKeluarga )
		self.delNotebook.AddPage( self.delKeluarga, u"a page", False )
		self.delAnggota = wx.Panel( self.delNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText40 = wx.StaticText( self.delAnggota, wx.ID_ANY, u"Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer57.Add( self.m_staticText40, 1, wx.ALIGN_CENTER, 5 )

		self.nomorKK_anggota = wx.TextCtrl( self.delAnggota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer57.Add( self.nomorKK_anggota, 0, 0, 5 )


		bSizer56.Add( bSizer57, 0, wx.ALL|wx.EXPAND, 10 )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( self.delAnggota, wx.ID_ANY, u"NIK Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer58.Add( self.m_staticText41, 1, wx.ALIGN_CENTER, 5 )

		self.nikAnggota = wx.TextCtrl( self.delAnggota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.nikAnggota, 0, 0, 5 )


		bSizer56.Add( bSizer58, 0, wx.ALL|wx.EXPAND, 10 )

		self.m_bpButton21 = wx.BitmapButton( self.delAnggota, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton21.SetBitmap( wx.Bitmap( u"picture/btn_hapus.png", wx.BITMAP_TYPE_ANY ) )
		bSizer56.Add( self.m_bpButton21, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 10 )


		self.delAnggota.SetSizer( bSizer56 )
		self.delAnggota.Layout()
		bSizer56.Fit( self.delAnggota )
		self.delNotebook.AddPage( self.delAnggota, u"a page", False )

		bSizer52.Add( self.delNotebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer52 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_bpButton19.Bind( wx.EVT_BUTTON, self.btn_delKeluarga )
		self.m_bpButton21.Bind( wx.EVT_BUTTON, self.btn_delAnggota )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_delKeluarga( self, event ):
		event.Skip()

	def btn_delAnggota( self, event ):
		event.Skip()


###########################################################################
## Class searchData
###########################################################################

class searchData ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( 800,400 ), wx.DefaultSize )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		bSizer59.SetMinSize( wx.Size( -1,350 ) )
		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Data Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

		bSizer57.Add( self.m_staticText42, 0, wx.BOTTOM|wx.TOP, 10 )


		bSizer59.Add( bSizer57, 0, wx.LEFT, 50 )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		self.m_staticText43.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

		bSizer63.Add( self.m_staticText43, 0, 0, 5 )

		self.nomorKK = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nomorKK.Wrap( -1 )

		self.nomorKK.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.nomorKK.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

		bSizer63.Add( self.nomorKK, 0, wx.TOP, 5 )


		bSizer66.Add( bSizer63, 1, wx.BOTTOM, 20 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Kepala Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

		bSizer62.Add( self.m_staticText45, 0, 0, 5 )

		self.kepKeluarga = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kepKeluarga.Wrap( -1 )

		self.kepKeluarga.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.kepKeluarga.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

		bSizer62.Add( self.kepKeluarga, 0, wx.TOP, 5 )


		bSizer66.Add( bSizer62, 1, 0, 5 )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"Anggota Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		self.m_staticText47.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

		bSizer61.Add( self.m_staticText47, 0, 0, 5 )

		self.anggota = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.anggota.Wrap( -1 )

		self.anggota.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.anggota.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

		bSizer61.Add( self.anggota, 0, wx.TOP, 5 )


		bSizer66.Add( bSizer61, 1, 0, 5 )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Total Pendapatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		self.m_staticText49.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

		bSizer60.Add( self.m_staticText49, 0, 0, 5 )

		self.total = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.total.Wrap( -1 )

		self.total.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.total.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

		bSizer60.Add( self.total, 0, wx.TOP, 5 )


		bSizer66.Add( bSizer60, 1, 0, 5 )

		bSizer64 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

		bSizer64.Add( self.m_staticText51, 0, 0, 5 )

		self.alamat = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alamat.Wrap( -1 )

		self.alamat.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.alamat.SetForegroundColour( wx.Colour( 100, 100, 100 ) )

		bSizer64.Add( self.alamat, 0, wx.TOP, 5 )


		bSizer66.Add( bSizer64, 1, 0, 5 )


		bSizer59.Add( bSizer66, 0, wx.EXPAND|wx.LEFT, 50 )

		bSizer58 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Anggota Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		self.m_staticText53.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )

		bSizer58.Add( self.m_staticText53, 0, wx.BOTTOM, 10 )


		bSizer59.Add( bSizer58, 0, wx.LEFT, 50 )

		self.searchGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		# Grid
		self.searchGrid.CreateGrid( 0, 2 )
		self.searchGrid.EnableEditing( False )
		self.searchGrid.EnableGridLines( True )
		self.searchGrid.EnableDragGridSize( False )
		self.searchGrid.SetMargins( 0, 0 )

		# Columns
		self.searchGrid.EnableDragColMove( False )
		self.searchGrid.EnableDragColSize( True )
		self.searchGrid.SetColLabelSize( 30 )
		self.searchGrid.SetColLabelValue( 0, u"Nomor Induk Keluarga" )
		self.searchGrid.SetColLabelValue( 1, u"Nama Lengkap" )
		self.searchGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.searchGrid.EnableDragRowSize( True )
		self.searchGrid.SetRowLabelSize( 60 )
		self.searchGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.searchGrid.SetLabelBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.searchGrid.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )
		self.searchGrid.SetLabelTextColour( wx.Colour( 100, 100, 100 ) )

		# Cell Defaults
		self.searchGrid.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.searchGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		bSizer59.Add( self.searchGrid, 0, wx.LEFT, 50 )


		self.SetSizer( bSizer59 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class rekomDanaPanel
###########################################################################

class rekomDanaPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.Point( 300,60 ), size = wx.Size( 980,740 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 980,740 ) )

		bSizer54 = wx.BoxSizer( wx.VERTICAL )

		bSizer54.SetMinSize( wx.Size( 980,740 ) )
		self.valueRekomPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_THEME|wx.TAB_TRAVERSAL )
		self.valueRekomPanel.SetMaxSize( wx.Size( -1,50 ) )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer58.SetMinSize( wx.Size( -1,100 ) )
		self.m_staticText43 = wx.StaticText( self.valueRekomPanel, wx.ID_ANY, u"Upah Minimum Regional", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		self.m_staticText43.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer58.Add( self.m_staticText43, 0, wx.ALIGN_CENTER|wx.LEFT, 50 )

		self.umrInput = wx.TextCtrl( self.valueRekomPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.umrInput.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.umrInput.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer58.Add( self.umrInput, 0, wx.ALIGN_CENTER|wx.LEFT, 30 )


		self.valueRekomPanel.SetSizer( bSizer58 )
		self.valueRekomPanel.Layout()
		bSizer58.Fit( self.valueRekomPanel )
		bSizer54.Add( self.valueRekomPanel, 0, wx.BOTTOM|wx.EXPAND, 20 )

		self.rekomGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,880 ), 0 )

		# Grid
		self.rekomGrid.CreateGrid( 0, 4 )
		self.rekomGrid.EnableEditing( False )
		self.rekomGrid.EnableGridLines( True )
		self.rekomGrid.EnableDragGridSize( False )
		self.rekomGrid.SetMargins( 0, 0 )

		# Columns
		self.rekomGrid.EnableDragColMove( False )
		self.rekomGrid.EnableDragColSize( False )
		self.rekomGrid.SetColLabelSize( 30 )
		self.rekomGrid.SetColLabelValue( 0, u"Nomor KK" )
		self.rekomGrid.SetColLabelValue( 1, u"Kepala Keluarga" )
		self.rekomGrid.SetColLabelValue( 2, u"Alamat" )
		self.rekomGrid.SetColLabelValue( 3, u"Saran Bantuan" )
		self.rekomGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.rekomGrid.EnableDragRowSize( False )
		self.rekomGrid.SetRowLabelSize( 60 )
		self.rekomGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.rekomGrid.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.rekomGrid.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )
		self.rekomGrid.SetLabelTextColour( wx.Colour( 100, 100, 100 ) )

		# Cell Defaults
		self.rekomGrid.SetDefaultCellTextColour( wx.Colour( 100, 100, 100 ) )
		self.rekomGrid.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.rekomGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )
		self.rekomGrid.SetMinSize( wx.Size( 880,-1 ) )

		bSizer54.Add( self.rekomGrid, 1, wx.LEFT|wx.EXPAND, 50 )


		self.SetSizer( bSizer54 )
		self.Layout()

		# Connect Events
		self.umrInput.Bind( wx.EVT_TEXT, self.umrChange )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def umrChange( self, event ):
		event.Skip()


###########################################################################
## Class rekapDataPanel
###########################################################################

class rekapDataPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.Point( 350,80 ), size = wx.Size( 880,720 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 880,720 ) )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.rekapOption = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.rekapOption.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_bpButton17 = wx.BitmapButton( self.rekapOption, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 420,160 ), wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton17.SetBitmap( wx.Bitmap( u"picture/catat_btn.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton17.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.m_bpButton17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_bpButton17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_bpButton17.SetMinSize( wx.Size( 420,220 ) )

		gSizer3.Add( self.m_bpButton17, 0, 0, 64 )

		self.m_bpButton18 = wx.BitmapButton( self.rekapOption, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 420,220 ), wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton18.SetBitmap( wx.Bitmap( u"picture/riwayat_btn.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton18.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.m_bpButton18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_bpButton18.SetMinSize( wx.Size( 420,220 ) )

		gSizer3.Add( self.m_bpButton18, 0, wx.ALIGN_RIGHT, 64 )


		self.rekapOption.SetSizer( gSizer3 )
		self.rekapOption.Layout()
		gSizer3.Fit( self.rekapOption )
		bSizer60.Add( self.rekapOption, 1, wx.EXPAND, 5 )

		self.riwayatBantuan = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.riwayatBantuan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.riwayatBantuan.Enable( False )
		self.riwayatBantuan.Hide()

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText56 = wx.StaticText( self.riwayatBantuan, wx.ID_ANY, u"Riwayat Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		self.m_staticText56.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.m_staticText56.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer71.Add( self.m_staticText56, 0, wx.BOTTOM, 20 )

		self.rekapGrid = wx.grid.Grid( self.riwayatBantuan, wx.ID_ANY, wx.DefaultPosition, wx.Size( 880,720 ), 0 )

		# Grid
		self.rekapGrid.CreateGrid( 0, 4 )
		self.rekapGrid.EnableEditing( False )
		self.rekapGrid.EnableGridLines( True )
		self.rekapGrid.EnableDragGridSize( False )
		self.rekapGrid.SetMargins( 0, 0 )

		# Columns
		self.rekapGrid.EnableDragColMove( False )
		self.rekapGrid.EnableDragColSize( False )
		self.rekapGrid.SetColLabelSize( 30 )
		self.rekapGrid.SetColLabelValue( 0, u"Nomor KK" )
		self.rekapGrid.SetColLabelValue( 1, u"Kepala Keluarga" )
		self.rekapGrid.SetColLabelValue( 2, u"Besar Bantuan" )
		self.rekapGrid.SetColLabelValue( 3, u"Tanggal" )
		self.rekapGrid.SetColLabelValue( 4, wx.EmptyString )
		self.rekapGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.rekapGrid.EnableDragRowSize( False )
		self.rekapGrid.SetRowLabelSize( 60 )
		self.rekapGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.rekapGrid.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.rekapGrid.SetLabelFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto" ) )
		self.rekapGrid.SetLabelTextColour( wx.Colour( 100, 100, 100 ) )

		# Cell Defaults
		self.rekapGrid.SetDefaultCellTextColour( wx.Colour( 100, 100, 100 ) )
		self.rekapGrid.SetDefaultCellFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.rekapGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.rekapGrid.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.rekapGrid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.rekapGrid.SetMinSize( wx.Size( 880,720 ) )

		bSizer71.Add( self.rekapGrid, 1, wx.EXPAND, 10 )


		self.riwayatBantuan.SetSizer( bSizer71 )
		self.riwayatBantuan.Layout()
		bSizer71.Fit( self.riwayatBantuan )
		bSizer60.Add( self.riwayatBantuan, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer60 )
		self.Layout()

		# Connect Events
		self.m_bpButton17.Bind( wx.EVT_BUTTON, self.catatBantuan_btn )
		self.m_bpButton18.Bind( wx.EVT_BUTTON, self.riwayatBantuan_btn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def catatBantuan_btn( self, event ):
		event.Skip()

	def riwayatBantuan_btn( self, event ):
		event.Skip()


###########################################################################
## Class catatData
###########################################################################

class catatData ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,250 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Catat Pemberian Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer63.Add( self.m_staticText41, 0, wx.BOTTOM|wx.LEFT|wx.TOP, 20 )

		bSizer64 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Nomor KK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		self.m_staticText43.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer64.Add( self.m_staticText43, 1, wx.ALIGN_CENTER|wx.BOTTOM|wx.RIGHT, 10 )

		self.nomorKK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,150 ), 0 )
		self.nomorKK.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.nomorKK.SetMinSize( wx.Size( 150,-1 ) )

		bSizer64.Add( self.nomorKK, 0, wx.ALIGN_CENTER|wx.RIGHT, 20 )


		bSizer63.Add( bSizer64, 0, wx.LEFT|wx.EXPAND, 20 )

		bSizer65 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Dana yang diberikan", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText44.Wrap( -1 )

		self.m_staticText44.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )

		bSizer65.Add( self.m_staticText44, 1, wx.ALIGN_CENTER|wx.RIGHT, 10 )

		self.danaBeri = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,150 ), 0 )
		self.danaBeri.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Roboto" ) )
		self.danaBeri.SetMinSize( wx.Size( 150,-1 ) )

		bSizer65.Add( self.danaBeri, 0, wx.ALIGN_CENTER|wx.RIGHT, 20 )


		bSizer63.Add( bSizer65, 0, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 20 )

		self.m_bpButton19 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.m_bpButton19.SetBitmap( wx.Bitmap( u"picture/tambah.png", wx.BITMAP_TYPE_ANY ) )
		bSizer63.Add( self.m_bpButton19, 0, wx.ALIGN_RIGHT|wx.RIGHT, 20 )


		self.SetSizer( bSizer63 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_bpButton19.Bind( wx.EVT_BUTTON, self.addCatat_btn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def addCatat_btn( self, event ):
		event.Skip()


