#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright: 2017 GUIMish <mish7913@gmail.com>
#  License:   GNU General Public License v2 or later

import pygtk, gtk, os, getpass, datetime
from PIL import Image

date = datetime.datetime.now();
pygtk.require("2.0")

class Window:
    def __init__(self):
		self.window = gtk.Window(); self.window.set_title("Android Projects");
		self.window.set_default_size(300, 350); 		self.window.set_border_width(5);
		self.window.set_position(gtk.WIN_POS_CENTER); 	self.window.connect("destroy", self.quit);
        
		self.main_box = gtk.VBox(); self.window.add(self.main_box);
        
		self.hbox1 = gtk.HBox(); self.main_box.pack_start(self.hbox1, 0, 1, 5);
		self.label = gtk.Label("Application name: "); self.hbox1.pack_start(self.label, 0, 1);
		self.AppName = gtk.Entry(); self.hbox1.add(self.AppName);
		self.AppName.connect("changed", self.ComApp);
  
		self.hbox2 = gtk.HBox(); self.main_box.pack_start(self.hbox2, 0, 1, 5);
		self.label = gtk.Label("Company Domain: "); self.hbox2.pack_start(self.label, 0, 1);
		self.ComDom = gtk.Entry(); self.hbox2.add(self.ComDom); 
		self.ComDom.connect("changed", self.ComApp);
		
		self.label_ComApp = gtk.Label("."); self.main_box.pack_start(self.label_ComApp, 0, 1, 5);
		
		self.HSep = gtk.HSeparator(); self.main_box.pack_start(self.HSep, 0, 1, 5);
		
		self.hbox3 = gtk.HBox(); self.main_box.pack_start(self.hbox3, 0, 1, 5);
		self.label = gtk.Label("Min SDK Version: "); self.hbox3.pack_start(self.label, 0, 1);
		self.AdjMinSDK = gtk.Adjustment(); self.AdjMinSDK.set_all(15, 15, 25, 1.0);
		self.MinSDK = gtk.SpinButton(); self.MinSDK.set_adjustment(self.AdjMinSDK);
		self.hbox3.add(self.MinSDK); self.MinSDK.set_value(15);
		
		self.hbox4 = gtk.HBox(); self.main_box.pack_start(self.hbox4, 0, 1, 5);
		self.label = gtk.Label("Target SDK Version: "); self.hbox4.pack_start(self.label, 0, 1);
		self.AdjTarSDK = gtk.Adjustment(); self.AdjTarSDK.set_all(16, 15, 25, 1.0);
		self.TarSDK = gtk.SpinButton(); self.TarSDK.set_adjustment(self.AdjTarSDK);
		self.hbox4.add(self.TarSDK); self.TarSDK.set_value(16);
		
		self.hbox5 = gtk.HBox(); self.main_box.pack_start(self.hbox5, 0, 1, 5);
		self.label = gtk.Label("Max SDK Version: "); self.hbox5.pack_start(self.label, 0, 1);
		self.AdjMaxSDK = gtk.Adjustment(); self.AdjMaxSDK.set_all(17, 15, 25, 1.0);
		self.MaxSDK = gtk.SpinButton(); self.MaxSDK.set_adjustment(self.AdjMaxSDK);
		self.hbox5.add(self.MaxSDK); self.MaxSDK.set_value(17);
		
		self.HSep = gtk.HSeparator(); self.main_box.pack_start(self.HSep, 0, 1, 5);
		
		self.hbox6 = gtk.HBox(); self.main_box.pack_start(self.hbox6, 0, 1, 5);
		
		self.imageFrame = gtk.Frame(); 		self.hbox6.pack_start(self.imageFrame, 0, 1, 5);
		self.image = gtk.Image(); 			self.image.set_size_request(55, 55);
		self.imageFrame.add(self.image); 	self.image.set_from_stock(gtk.STOCK_MISSING_IMAGE, gtk.ICON_SIZE_MENU);
		
		self.alignment0 = gtk.Alignment(0, 0); 	self.hbox6.pack_start(self.alignment0, 0, 1);
		self.hbox7 = gtk.VBox(); self.alignment0.add(self.hbox7);
		self.hbox8 = gtk.HBox(); self.hbox7.add(self.hbox8);
		self.btn_image = gtk.Button("Open Image"); self.hbox7.pack_end(self.btn_image, 0, 1, 5);
		self.btn_image.connect("clicked", self.img_click);
		
		self.alignment1 = gtk.Alignment(0, 0); 	self.hbox8.pack_start(self.alignment1, 0, 1);
		self.alignment1.set_padding(5, 0, 0, 0);
		self.label = gtk.Label("Path SDK: "); 	self.alignment1.add(self.label);
		self.alignment2 = gtk.Alignment(0, 0); 	self.hbox8.pack_start(self.alignment2, 0, 1);
		self.PathSDK = gtk.Entry(); 			self.alignment2.add(self.PathSDK);
		self.PathSDK.set_text(os.environ['HOME'] + "/Android/Sdk");
		
		
		self.btn_create = gtk.Button("Create"); self.main_box.pack_end(self.btn_create, 0, 1, 5);
		self.btn_create.connect("clicked", self.btn_click);
		
		self.HSep = gtk.HSeparator(); self.main_box.pack_end(self.HSep, 0, 1, 2);
		
		self.window.show_all();
		
		self.ComDom.set_text(getpass.getuser().title());
		self.AppName.set_text("AppName");
		
		self.image_path = "";
 
    def quit(self, widget, data = None):
        gtk.main_quit();

    def img_click(self, widget):
		dialog = gtk.FileChooserDialog("Open..", None, gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, 
																						   gtk.STOCK_OPEN,   gtk.RESPONSE_OK))
		filter = gtk.FileFilter();
		filter.set_name("All Images");
		filter.add_mime_type("image/png");  filter.add_pattern("*.png");
		filter.add_mime_type("image/jpeg"); filter.add_pattern("*.jpg");
		filter.add_mime_type("image/gif");  filter.add_pattern("*.gif");
		dialog.add_filter(filter);
		
		filter = gtk.FileFilter(); filter.set_name('Image PNG (*.png)');
		filter.add_mime_type("image/png");  filter.add_pattern("*.png"); dialog.add_filter(filter);
		filter = gtk.FileFilter(); filter.set_name('Image JPG (*.jpg)');
		filter.add_mime_type("image/jpeg");  filter.add_pattern("*.jpg"); dialog.add_filter(filter);
		filter = gtk.FileFilter(); filter.set_name('Image GIF (*.gif)');
		filter.add_mime_type("image/gif");  filter.add_pattern("*.gif"); dialog.add_filter(filter);
		
		if dialog.run() == gtk.RESPONSE_OK:
			self.image_path = str(dialog.get_filename());
			Img = self.fileicon(dialog.get_filename());
			if Img.get_width() < 40:
				if Img.get_height() < 40: self.image.set_from_pixbuf(Img)
			else:
				if Img.get_width() > Img.get_height():
					height = int((float(Img.get_height()) / float(Img.get_width())) * 40)
					self.image.set_from_pixbuf(Img.scale_simple(40, height, gtk.gdk.INTERP_BILINEAR))
				else:
					width = int((float(Img.get_width()) / float(Img.get_height())) * 40)
					self.image.set_from_pixbuf(Img.scale_simple(width, 40, gtk.gdk.INTERP_BILINEAR))
		dialog.destroy();
		
    def btn_click(self, widget):
		dialog = gtk.FileChooserDialog("Open..", None, gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, 
			(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK));
		dialog.set_current_folder(os.environ['HOME']);
		
		if dialog.run() == gtk.RESPONSE_OK:
			path = str(dialog.get_filename()) + "/" + self.AppName.get_text();
			if not os.path.isdir(path): os.makedirs(path); self.CreateApp(path);
			else: print ("Error: filder is exist."); 
				
		dialog.destroy();
        
    def ComApp(self, widget): self.label_ComApp.set_label(self.ComDom.get_text().lower() + "." + self.AppName.get_text().lower());
    def fileicon(self, file): return gtk.gdk.pixbuf_new_from_file(file);
    
    def CreateApp(self, path):
		App_name = self.AppName.get_text(); 			Com_Dom = self.ComDom.get_text();			
		App_SDK = self.PathSDK.get_text();				labComApp = self.label_ComApp.get_text();
		MinSDK = str(int(self.MinSDK.get_value()));		TarSDK = str(int(self.TarSDK.get_value()));
		MaxSDK = str(int(self.MaxSDK.get_value()));
		
		
		path_assets = path + "/assets";
		if not os.path.isdir(path_assets): os.makedirs(path_assets);
		
		path_bin = path + "/bin";
		if not os.path.isdir(path_bin): os.makedirs(path_bin);
		
		path_gen = path + "/gen";
		if not os.path.isdir(path_gen): os.makedirs(path_gen);
		path_gen_com = path_gen + "/" + Com_Dom.lower();
		if not os.path.isdir(path_gen_com): os.makedirs(path_gen_com);
		path_gen_com_app = path_gen_com + "/" + App_name.lower();
		if not os.path.isdir(path_gen_com_app): os.makedirs(path_gen_com_app);
		
		App_set_com_BC = open(path_gen_com_app + "/BuildConfig.java", 'w+');
		App_set_com_BC.write('/** Automatically generated file. DO NOT MODIFY */\n' +
							 'package '+labComApp+';\n' +
							 '\n' +
							 'public final class BuildConfig {\n' +
							 '    public final static boolean DEBUG = true;\n' +
							 '}');
		App_set_com_BC.close();
		
		App_set_com_R = open(path_gen_com_app + "/R.java", 'w+');
		App_set_com_R.write('/* AUTO-GENERATED FILE.  DO NOT MODIFY.\n' +
							 ' *\n' +
							 ' * This class was automatically generated by the\n' +
							 ' * aapt tool from the resource data it found.  It\n' +
							 ' * should not be modified by hand.\n' +
							 ' */\n' +
							 '\n' +
							 'package '+labComApp+';\n' +
							 '\n' +
							 'public final class R {\n' +
							 '    public static final class attr {\n' +
							 '    }\n' +
							 '    public static final class dimen {\n' +
							 '        /**  Default screen margins, per the Android Design guidelines. \n' +
							 '\n' +
							 '         Example customization of dimensions originally defined in res/values/dimens.xml\n' +
							 '         (such as screen margins) for screens with more than 820dp of available width. This\n' +
							 '         would include 7" and 10" devices in landscape (~960dp and ~1280dp respectively).\n' +
							 '\n' +
							 '         */\n' +
							 '        public static final int activity_horizontal_margin=0x7f040000;\n' +
							 '        public static final int activity_vertical_margin=0x7f040001;\n' +
							 '    }\n' +
							 '    public static final class drawable {\n' +
							 '        public static final int ic_launcher=0x7f020000;\n' +
							 '    }\n' +
							 '    public static final class id {\n' +
							 '        public static final int action_settings=0x7f080000;\n' +
							 '    }\n' +
							 '    public static final class layout {\n' +
							 '        public static final int activity_main=0x7f030000;\n' +
							 '    }\n' +
							 '    public static final class menu {\n' +
							 '        public static final int main=0x7f070000;\n' +
							 '    }\n' +
							 '    public static final class string {\n' +
							 '        public static final int action_settings=0x7f050002;\n' +
							 '        public static final int app_name=0x7f050000;\n' +
							 '        public static final int hello_world=0x7f050001;\n' +
							 '    }\n' +
							 '    public static final class style {\n' +
							 '        /** \n' +
							 '        Base application theme, dependent on API level. This theme is replaced\n' +
							 '        by AppBaseTheme from res/values-vXX/styles.xml on newer devices.\n' +
							 '\n\n' +
							 '            Theme customizations available in newer API levels can go in\n' +
							 '            res/values-vXX/styles.xml, while customizations related to\n' +
							 '            backward-compatibility can go here.\n' +
							 '\n\n' +
							 '        Base application theme for API 11+. This theme completely replaces\n' +
							 '        AppBaseTheme from res/values/styles.xml on API 11+ devices.\n' +
							 '\n' +
							 ' API 11 theme customizations can go here. \n' +
							 '\n' +
							 '        Base application theme for API 14+. This theme completely replaces\n' +
							 '        AppBaseTheme from BOTH res/values/styles.xml and\n' +
							 '        res/values-v11/styles.xml on API 14+ devices.\n' +
							 '\n' +
							 ' API 14 theme customizations can go here. \n' +
							 '         */\n' +
							 '        public static final int AppBaseTheme=0x7f060000;\n' +
							 '        /**  Application theme. \n' +
							 ' All customizations that are NOT specific to a particular API-level can go here.\n' +
							 '         */\n' +
							 '        public static final int AppTheme=0x7f060001;\n' +
							 '    }\n' +
							 '}');
		App_set_com_R.close();
		
		path_res = path + "/res";
		if not os.path.isdir(path_res): os.makedirs(path_res);
		if (path_res):
			path_res_drhd = path_res + "/drawable-hdpi";
			if not os.path.isdir(path_res_drhd): os.makedirs(path_res_drhd);
			path_res_drld = path_res + "/drawable-ldpi";
			if not os.path.isdir(path_res_drld): os.makedirs(path_res_drld);
			path_res_drmd = path_res + "/drawable-mdpi";
			if not os.path.isdir(path_res_drmd): os.makedirs(path_res_drmd);
			path_res_xhdpi = path_res + "/drawable-xhdpi";
			if not os.path.isdir(path_res_xhdpi): os.makedirs(path_res_xhdpi);
			path_res_xxhdpi = path_res + "/drawable-xxhdpi";
			if not os.path.isdir(path_res_xxhdpi): os.makedirs(path_res_xxhdpi);
			path_res_xxxhdpi = path_res + "/drawable-xxxhdpi";
			if not os.path.isdir(path_res_xxxhdpi): os.makedirs(path_res_xxxhdpi);
			path_res_layout = path_res + "/layout";
			if not os.path.isdir(path_res_layout): os.makedirs(path_res_layout);
			path_res_menu = path_res + "/menu";
			if not os.path.isdir(path_res_menu): os.makedirs(path_res_menu);
			path_res_values = path_res + "/values";
			if not os.path.isdir(path_res_values): os.makedirs(path_res_values);
			path_res_values_v11 = path_res + "/values-v11";
			if not os.path.isdir(path_res_values_v11): os.makedirs(path_res_values_v11);
			path_res_values_v14 = path_res + "/values-v14";
			if not os.path.isdir(path_res_values_v14): os.makedirs(path_res_values_v14);
			path_res_values_w820dp = path_res + "/values-w820dp";
			if not os.path.isdir(path_res_values_w820dp): os.makedirs(path_res_values_w820dp);
			
		if (self.image_path != ''):
			image = Image.open(self.image_path);
			if (image):
				new_image = image.resize((72, 72));   new_image.save(path_res_drhd + '/ic_launcher.png');
				new_image = image.resize((48, 48));   new_image.save(path_res_drmd + '/ic_launcher.png');
				new_image = image.resize((96, 96));   new_image.save(path_res_xhdpi + '/ic_launcher.png');
				new_image = image.resize((144, 144)); new_image.save(path_res_xxhdpi + '/ic_launcher.png');
				new_image = image.resize((192, 192)); new_image.save(path_res_xxxhdpi + '/ic_launcher.png');
				new_image = image.resize((512, 512)); new_image.save(path + '/ic_launcher-web.png');
		
		App_set_lay_acm = open(path_res_layout + "/activity_main.xml", 'w+');
		App_set_lay_acm.write('<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"\n' +
							 '    xmlns:tools="http://schemas.android.com/tools"\n' +
							 '    android:layout_width="match_parent"\n' +
							 '    android:layout_height="match_parent"\n' +
							 '    android:paddingBottom="@dimen/activity_vertical_margin"\n' +
							 '    android:paddingLeft="@dimen/activity_horizontal_margin"\n' +
							 '    android:paddingRight="@dimen/activity_horizontal_margin"\n' +
							 '    android:paddingTop="@dimen/activity_vertical_margin"\n' +
							 '    tools:context="'+labComApp+'.MainActivity" >\n' +
							 '\n' +
							 '    <TextView\n' +
							 '        android:layout_width="wrap_content"\n' +
							 '        android:layout_height="wrap_content"\n' +
							 '        android:text="@string/hello_world" />\n' +
							 '\n' +
							 '</RelativeLayout>');
		App_set_lay_acm.close();
		
		App_set_menu_main = open(path_res_menu + "/main.xml", 'w+');
		App_set_menu_main.write('<menu xmlns:android="http://schemas.android.com/apk/res/android"\n' +
							 '    xmlns:tools="http://schemas.android.com/tools"\n' +
							 '    tools:context="testur.testeroid.MainActivity" >\n' +
							 '\n' +
							 '    <item\n' +
							 '        android:id="@+id/action_settings"\n' +
							 '        android:orderInCategory="100"\n' +
							 '        android:showAsAction="never"\n' +
							 '        android:title="@string/action_settings"/>\n' +
							 '\n' +
							 '</menu>');
		App_set_menu_main.close();
		
		App_set_val_dimens = open(path_res_values + "/dimens.xml", 'w+');
		App_set_val_dimens.write('<resources>\n' +
							 '\n' +
							 '    <!-- Default screen margins, per the Android Design guidelines. -->\n' +
							 '    <dimen name="activity_horizontal_margin">16dp</dimen>\n' +
							 '    <dimen name="activity_vertical_margin">16dp</dimen>\n' +
							 '\n' +
							 '</resources>');
		App_set_val_dimens.close();
		
		App_set_val_str = open(path_res_values + "/strings.xml", 'w+');
		App_set_val_str.write('<?xml version="1.0" encoding="utf-8"?>\n' +
							 '<resources>\n' +
							 '\n' +
							 '    <string name="app_name">'+App_name+'</string>\n' +
							 '    <string name="hello_world">Hello world!</string>\n' +
							 '    <string name="action_settings">Settings</string>\n' +
							 '\n' +
							 '</resources>');
		App_set_val_str.close();
		
		App_set_val_styles = open(path_res_values + "/styles.xml", 'w+');
		App_set_val_styles.write('<resources>\n' +
							 '\n' +
							 '    <!--\n' +
							 '        Base application theme, dependent on API level. This theme is replaced\n' +
							 '        by AppBaseTheme from res/values-vXX/styles.xml on newer devices.\n' +
							 '    -->\n' +
							 '    <style name="AppBaseTheme" parent="android:Theme.Light">\n' +
							 '        <!--\n' +
							 '            Theme customizations available in newer API levels can go in\n' +
							 '            res/values-vXX/styles.xml, while customizations related to\n' +
							 '            backward-compatibility can go here.\n' +
							 '        -->\n' +
							 '    </style>\n' +
							 '\n' +
							 '    <!-- Application theme. -->\n' +
							 '    <style name="AppTheme" parent="AppBaseTheme">\n' +
							 '        <!-- All customizations that are NOT specific to a particular API-level can go here. -->\n' +
							 '    </style>\n' +
							 '\n' +
							 '</resources>');
		App_set_val_styles.close();
		
		App_set_v11_styles = open(path_res_values_v11 + "/styles.xml", 'w+');
		App_set_v11_styles.write('<resources>\n' +
							 '\n' +
							 '    <!--\n' +
							 '        Base application theme for API 11+. This theme completely replaces\n' +
							 '        AppBaseTheme from res/values/styles.xml on API 11+ devices.\n' +
							 '    -->\n' +
							 '    <style name="AppBaseTheme" parent="android:Theme.Holo.Light">\n' +
							 '        <!-- API 11 theme customizations can go here. -->\n' +
							 '    </style>\n' +
							 '\n' +
							 '</resources>');
		App_set_v11_styles.close();
		
		App_set_v14_styles = open(path_res_values_v14 + "/styles.xml", 'w+');
		App_set_v14_styles.write('<resources>\n' +
							 '\n' +
							 '    <!--\n' +
							 '        Base application theme for API 14+. This theme completely replaces\n' +
							 '        AppBaseTheme from BOTH res/values/styles.xml and\n' +
							 '        res/values-v11/styles.xml on API 14+ devices.\n' +
							 '    -->\n' +
							 '    <style name="AppBaseTheme" parent="android:Theme.Holo.Light.DarkActionBar">\n' +
							 '        <!-- API 14 theme customizations can go here. -->\n' +
							 '    </style>\n' +
							 '\n' +
							 '</resources>');
		App_set_v14_styles.close();
		
		App_set_dimens = open(path_res_values_w820dp + "/dimens.xml", 'w+');
		App_set_dimens.write('<resources>\n' +
							 '\n' +
							 '    <!--\n' +
							 '         Example customization of dimensions originally defined in res/values/dimens.xml\n' +
							 '         (such as screen margins) for screens with more than 820dp of available width. This\n' +
							 '         would include 7" and 10" devices in landscape (~960dp and ~1280dp respectively).\n' +
							 '    -->\n' +
							 '    <dimen name="activity_horizontal_margin">64dp</dimen>\n' +
							 '\n' +
							 '</resources>');
		App_set_dimens.close();
		
		
		path_src = path + "/src";
		if not os.path.isdir(path_src): os.makedirs(path_src);
		path_src_com = path_src + "/" + Com_Dom.lower();
		if not os.path.isdir(path_src_com): os.makedirs(path_src_com);
		path_src_com_app = path_src_com + "/" + App_name.lower();
		if not os.path.isdir(path_src_com_app): os.makedirs(path_src_com_app);
		
		App_set_activity = open(path_src_com_app + "/MainActivity.java", 'w+');
		App_set_activity.write('package '+labComApp+';\n' +
							 '\n' +
							 'import android.app.Activity;\n' +
							 'import android.os.Bundle;\n' +
							 'import android.view.Menu;\n' +
							 'import android.view.MenuItem;\n' +
							 '\n' +
							 'public class MainActivity extends Activity {\n' +
							 '\n' +
							 '	@Override\n' +
							 '	protected void onCreate(Bundle savedInstanceState) {\n' +
							 '		super.onCreate(savedInstanceState);\n' +
							 '		setContentView(R.layout.activity_main);\n' +
							 '	}\n' +
							 '\n' +
							 '	@Override\n' +
							 '	public boolean onCreateOptionsMenu(Menu menu) {\n' +
							 '		// Inflate the menu; this adds items to the action bar if it is present.\n' +
							 '		getMenuInflater().inflate(R.menu.main, menu);\n' +
							 '		return true;\n' +
							 '	}\n' +
							 '\n' +
							 '	@Override\n' +
							 '	public boolean onOptionsItemSelected(MenuItem item) {\n' +
							 '		// Handle action bar item clicks here. The action bar will\n' +
							 '		// automatically handle clicks on the Home/Up button, so long\n' +
							 '		// as you specify a parent activity in AndroidManifest.xml.\n' +
							 '		int id = item.getItemId();\n' +
							 '		if (id == R.id.action_settings) {\n' +
							 '			return true;\n' +
							 '		}\n' +
							 '		return super.onOptionsItemSelected(item);\n' +
							 '	}\n' +
							 '}');
		App_set_activity.close();
		
		
		App_set_gradle = open(path+"/AndroidManifest.xml", 'w+');
		App_set_gradle.write('<?xml version="1.0" encoding="utf-8"?>\n' +
							 '<manifest xmlns:android="http://schemas.android.com/apk/res/android"\n' +
							 '    package="'+labComApp+'"\n' +
							 '    android:versionCode="1"\n' +
							 '    android:versionName="1.0" >\n' +
							 '\n' +
							 '    <uses-sdk\n' +
							 '        android:minSdkVersion="'+MinSDK+'"\n' +
							 '        android:targetSdkVersion="'+TarSDK+'"\n' +
							 '		android:maxSdkVersion="'+MaxSDK+'"/>\n' +
							 '\n' +
							 '    <application\n' +
							 '        android:allowBackup="true"\n' +
							 '        android:icon="@drawable/ic_launcher"\n' +
							 '        android:label="@string/app_name"\n' +
							 '        android:theme="@style/AppTheme" >\n' +
							 '        <activity\n' +
							 '            android:name=".MainActivity"\n' +
							 '            android:label="@string/app_name" >\n' +
							 '            <intent-filter>\n' +
							 '                <action android:name="android.intent.action.MAIN" />\n' +
							 '\n' +
							 '                <category android:name="android.intent.category.LAUNCHER" />\n' +
							 '            </intent-filter>\n' +
							 '        </activity>\n' +
							 '    </application>\n' +
							 '\n' +
							 "</manifest>");
		App_set_gradle.close();
		
		App_set_gradle = open(path+"/proguard-project.txt", 'w+');
		App_set_gradle.write("# To enable ProGuard in your project, edit project.properties\n" +
							 "# to define the proguard.config property as described in that file.\n" +
							 "# \n" +
							 "# Add project specific ProGuard rules here.\n" +
							 "# By default, the flags in this file are appended to flags specified\n" +
							 "# in ${sdk.dir}/tools/proguard/proguard-android.txt\n" +
							 "# You can edit the include path and order by changing the ProGuard\n" +
							 "# include property in project.properties.\n" +
							 "# \n" +
							 "# For more details, see\n" +
							 "#   http://developer.android.com/guide/developing/tools/proguard.html\n" +
							 "\n" +
							 "# Add any project specific keep options here:\n" +
							 "\n" +
							 "# If your project uses WebView with JS, uncomment the following\n" +
							 "# and specify the fully qualified class name to the JavaScript interface\n" +
							 "# class:\n" +
							 "#-keepclassmembers class fqcn.of.javascript.interface.for.webview {\n" +
							 "#   public *;\n" +
							 "#}");
		App_set_gradle.close();
		
		App_set_gradle = open(path+"/project.properties", 'w+');
		App_set_gradle.write("# This file is automatically generated by Android Tools.\n" +
							 "# Do not modify this file -- YOUR CHANGES WILL BE ERASED!\n" +
							 "# \n" +
							 "# This file must be checked in Version Control Systems.\n" +
							 "# \n" +
							 "# To customize properties used by the Ant build system edit\n" +
							 '# "ant.properties", and override values to adapt the script to your\n' +
							 "# project structure.\n" +
							 "# \n" +
							 "# To enable ProGuard to shrink and obfuscate your code, uncomment this (available properties: sdk.dir, user.home):\n" +
							 "#proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt\n" +
							 "\n" +
							 "# Project target.\n" +
							 "target=android-"+TarSDK+"\n");
		App_set_gradle.close();
		
 
    def main(self):
        gtk.main();
  
if __name__ == "__main__": Window().main();
