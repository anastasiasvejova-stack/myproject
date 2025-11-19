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
    <width>707</width>
    <height>630</height>
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
   <string notr="true"/>
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
       <widget class="QLabel" name="label">
        <property name="styleSheet">
         <string notr="true">font: 10pt &quot;MS Shell Dlg 2&quot;;</string>
        </property>
        <property name="text">
         <string>задачи на:</string>
        </property>
       </widget>
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
             <string/>
            </property>
           </item>
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
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>707</width>
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
    <height>325</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QPushButton" name="work_btn">
     <property name="styleSheet">
      <string notr="true">QPushButton{
    min-width:  350px;
    max-width:  100px;
    min-height: 38px;
    max-height: 35px;
	color: purple;           /* Например, белый цвет текста */
	background-color: white
}</string>
     </property>
     <property name="text">
      <string>работа</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="home_btn">
     <property name="styleSheet">
      <string notr="true">QPushButton{
    min-width:  350px;
    max-width:  100px;
    min-height: 38px;
    max-height: 35px;
	color: #ff557f;           /* Например, белый цвет текста */
	background-color: white
}</string>
     </property>
     <property name="text">
      <string>дом</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="store_btn">
     <property name="styleSheet">
      <string notr="true">QPushButton{
    min-width:  350px;
    max-width:  100px;
    min-height: 38px;
    max-height: 35px;
	color: #ffe308;           /* Например, белый цвет текста */
	background-color: white
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
    min-height: 38px;
    max-height: 35px;
	color: orange;           /* Например, белый цвет текста */
	background-color: white
}</string>
     </property>
     <property name="text">
      <string>другое</string>
     </property>
    </widget>
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


class Dairy(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setWindowTitle("Ежедневник")
        self.current_category = ""
        self.category_btn.clicked.connect(self.categories)
        self.calendar_btn.clicked.connect(self.calendar)
        self.new_event_btn.clicked.connect(self.new_event)
        self.date_cmb.activated.connect(self.date)
        self.connect_bd("dairy.db")


    def connect_bd(self, name):
        self.con = sqlite3.connect(name)
        self.cur = self.con.cursor()

        result = self.cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT, 
        category TEXT CHECK (category in ('работа', 'дом', 'покупки', 'другое')),
        date TEXT,
        reminder TEXT)''').fetchall()
        self.con.commit()

    def categories(self):
        pass

    def load_events(self):
        pass

    def calendar(self):
        pass

    def new_event(self):
        pass

    def date(self):
        pass


class Newtask(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = io.StringIO(new_task)
        uic.loadUi(f, self)
        self.reminder_time.setDisplayFormat("HH:mm")


class CategoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = io.StringIO(category_dialog)
        uic.loadUi(f, self)
        self.category = None
        self.work_btn.clicked.connect(lambda: self.select_category("работа"))
        self.home_btn.clicked.connect(lambda: self.select_category("дом"))
        self.store_btn.clicked.connect(lambda: self.select_category("покупки"))
        self.other_btn.clicked.connect(lambda: self.select_category("другое"))

    def select_category(self, category):
        self.category = category
        self.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dairy()
    ex.show()
    sys.exit(app.exec())
