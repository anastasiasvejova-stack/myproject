import io
import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>958</width>
    <height>703</height>
   </rect>
  </property>
  <property name="maximumSize">
   <size>
    <width>16777</width>
    <height>16777</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: white; /* Синий фон */
</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout_2">
    <item>
     <layout class="QVBoxLayout" name="verticalLayout_2">
      <item>
       <widget class="QWidget" name="widget" native="true">
        <layout class="QHBoxLayout" name="horizontalLayout">
         <item>
          <widget class="QPushButton" name="category_btn">
           <property name="palette">
            <palette>
             <active>
              <colorrole role="WindowText">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Button">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Text">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="ButtonText">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Base">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Window">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="ToolTipBase">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>198</green>
                 <blue>24</blue>
                </color>
               </brush>
              </colorrole>
             </active>
             <inactive>
              <colorrole role="WindowText">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Button">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Text">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="ButtonText">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Base">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Window">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="ToolTipBase">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>198</green>
                 <blue>24</blue>
                </color>
               </brush>
              </colorrole>
             </inactive>
             <disabled>
              <colorrole role="WindowText">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Button">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Text">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="ButtonText">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>216</green>
                 <blue>19</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Base">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="Window">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>255</green>
                 <blue>255</blue>
                </color>
               </brush>
              </colorrole>
              <colorrole role="ToolTipBase">
               <brush brushstyle="SolidPattern">
                <color alpha="255">
                 <red>255</red>
                 <green>198</green>
                 <blue>24</blue>
                </color>
               </brush>
              </colorrole>
             </disabled>
            </palette>
           </property>
           <property name="font">
            <font>
             <pointsize>10</pointsize>
            </font>
           </property>
           <property name="styleSheet">
            <string notr="true">color: #ffd813; /* Белый цвет текста */
background-color: white; /* Синий фон */
</string>
           </property>
           <property name="text">
            <string>Категории</string>
           </property>
           <property name="icon">
            <iconset>
             <normaloff>../../Downloads/54410.png</normaloff>../../Downloads/54410.png</iconset>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QPushButton" name="calendar_btn">
           <property name="font">
            <font>
             <pointsize>10</pointsize>
            </font>
           </property>
           <property name="styleSheet">
            <string notr="true">color: #ffd813; /* Белый цвет текста */
background-color: white; /* Синий фон */
</string>
           </property>
           <property name="text">
            <string>Календарь</string>
           </property>
           <property name="icon">
            <iconset>
             <normaloff>../../Downloads/747310.png</normaloff>../../Downloads/747310.png</iconset>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QPushButton" name="search_btn">
           <property name="font">
            <font>
             <pointsize>10</pointsize>
            </font>
           </property>
           <property name="styleSheet">
            <string notr="true">color: #ffd813; /* Белый цвет текста */
background-color: white; /* Синий фон */
</string>
           </property>
           <property name="text">
            <string>Поиск</string>
           </property>
           <property name="icon">
            <iconset>
             <normaloff>../../Downloads/1828948.png</normaloff>../../Downloads/1828948.png</iconset>
           </property>
          </widget>
         </item>
        </layout>
       </widget>
      </item>
      <item>
       <spacer name="verticalSpacer">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item>
       <widget class="QWidget" name="widget_2" native="true">
        <layout class="QVBoxLayout" name="verticalLayout">
         <item>
          <widget class="QComboBox" name="date_cmb">
           <property name="font">
            <font>
             <pointsize>10</pointsize>
            </font>
           </property>
           <item>
            <property name="text">
             <string>&quot;сегодня&quot;</string>
            </property>
           </item>
           <item>
            <property name="text">
             <string>&quot;завтра&quot;</string>
            </property>
           </item>
           <item>
            <property name="text">
             <string>&quot;на неделе&quot;</string>
            </property>
           </item>
           <item>
            <property name="text">
             <string>&quot;в этом месяце&quot;</string>
            </property>
           </item>
           <item>
            <property name="text">
             <string>&quot;потом&quot;</string>
            </property>
           </item>
          </widget>
         </item>
         <item>
          <spacer name="verticalSpacer_2">
           <property name="orientation">
            <enum>Qt::Vertical</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>20</width>
             <height>40</height>
            </size>
           </property>
          </spacer>
         </item>
         <item>
          <widget class="QPushButton" name="new_event_btn">
           <property name="maximumSize">
            <size>
             <width>62</width>
             <height>62</height>
            </size>
           </property>
           <property name="font">
            <font>
             <pointsize>22</pointsize>
            </font>
           </property>
           <property name="styleSheet">
            <string notr="true">QPushButton {
    border-radius: 30px; /* Радиус скругления, должен быть равен половине высоты/ширины */
    min-width: 60px;    /* Минимальная ширина */
    max-width: 60px;    /* Максимальная ширина */
    min-height: 60px;   /* Минимальная высота */
    max-height: 60px;   /* Максимальная высота */
    background-color: #ff8fab; /* Пример цвета фона */
    color: white;             /* Пример цвета текста */
    border: 1px solid #4CAF50; /* Пример границы */
}
</string>
           </property>
           <property name="text">
            <string/>
           </property>
           <property name="icon">
            <iconset>
             <normaloff>../../Downloads/7794550.png</normaloff>../../Downloads/7794550.png</iconset>
           </property>
           <property name="iconSize">
            <size>
             <width>40</width>
             <height>40</height>
            </size>
           </property>
          </widget>
         </item>
        </layout>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <widget class="QWidget" name="widget_3" native="true">
      <widget class="QLabel" name="pic_label">
       <property name="geometry">
        <rect>
         <x>10</x>
         <y>0</y>
         <width>451</width>
         <height>621</height>
        </rect>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="pixmap">
        <pixmap resource="resources.qrc">:/istockphoto-518854697-612x612.jpg</pixmap>
       </property>
       <property name="scaledContents">
        <bool>true</bool>
       </property>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>958</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="resources.qrc"/>
 </resources>
 <connections/>
</ui>
"""


new_task = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QLabel" name="label_3">
     <property name="text">
      <string>введите название задачи</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QLineEdit" name="lineEdit"/>
   </item>
   <item>
    <widget class="QLabel" name="label_2">
     <property name="text">
      <string>выберите категорию</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QComboBox" name="comboBox">
     <item>
      <property name="text">
       <string/>
      </property>
     </item>
     <item>
      <property name="text">
       <string>'работа'</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>'дом'</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>'покупки'</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>'другое'</string>
      </property>
     </item>
    </widget>
   </item>
   <item>
    <widget class="QLabel" name="label">
     <property name="text">
      <string>выберите время напоминания</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QTimeEdit" name="timeEdit"/>
   </item>
   <item>
    <widget class="QDialogButtonBox" name="buttonBox">
     <property name="standardButtons">
      <set>QDialogButtonBox::Cancel|QDialogButtonBox::Ok</set>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


calendar = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <layout class="QHBoxLayout" name="horizontalLayout">
   <item>
    <widget class="QTableView" name="tableView"/>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


category_dialog = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>374</width>
    <height>430</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QPushButton" name="pushButton">
     <property name="styleSheet">
      <string notr="true">QPushButton{
    min-width:  350px;
    max-width:  100px;
    min-height: 35px;
    max-height: 35px;
	color: #ff007f; /* Белый цвет текста */
	background-color: white; /* Синий фон */
	}

</string>
     </property>
     <property name="text">
      <string>работа</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="pushButton_2">
     <property name="styleSheet">
      <string notr="true">QPushButton{
    min-width:  350px;
    max-width:  100px;
    min-height: 35px;
    max-height: 35px;
	color: #aa00ff; /* Белый цвет текста */
	background-color: white; /* Синий фон */
	}</string>
     </property>
     <property name="text">
      <string>дом</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="pushButton_3">
     <property name="styleSheet">
      <string notr="true">QPushButton{
    min-width:  350px;
    max-width:  100px;
    min-height: 35px;
    max-height: 35px;
	color:  #ffd900; /* Белый цвет текста */
	background-color: white; /* Синий фон */
	}</string>
     </property>
     <property name="text">
      <string>покупки</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="pushButton_4">
     <property name="styleSheet">
      <string notr="true">QPushButton{
    min-width:  350px;
    max-width:  100px;
    min-height: 35px;
    max-height: 35px;
	color:  #ffaa00; /* Белый цвет текста */
	background-color: white; /* Синий фон */
	}</string>
     </property>
     <property name="text">
      <string>другое</string>
     </property>
    </widget>
   </item>
   <item>
    <spacer name="verticalSpacer">
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="sizeHint" stdset="0">
      <size>
       <width>20</width>
       <height>40</height>
      </size>
     </property>
    </spacer>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Dairy(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setWindowTitle("Ежедневник")
        self.category_btn.clicked.connect(self.categories)
        self.calendar_btn.clicked.connect(self.calendar)
        self.new_event_btn.clicked.connect(self.new_event)
        self.date_cmb.activated.connect(self.date)
        self.connect_bd("dairy.db")

    def connect_bd(self, name):
        con = sqlite3.connect(name)
        cur = con.cursor()

        result = cur.execute('''CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, 
        category TEXT NOT NULL CHECK (category in ('работа', 'дом', 'покупки', 'другое')),
        date TEXT NOT NULL,
        reminder TEXT NOT NULL)''').fetchone()
        con.commit()

    def categories(self):
        pass

    def calendar(self):
        pass

    def new_event(self):
        pass

    def date(self):
        pass


class newtask(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(new_task, self)
        self.reminder_time.setDisplayFormat("HH:mm")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dairy()
    ex.show()
    sys.exit(app.exec())
