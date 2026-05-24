# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from pages.shortcut_page import ShortcutPage
from pages.body_classifier_page import BodyClassifierPage

# ==================== 三大高奢艺术主题 QSS 矩阵 ====================
THEMES = {
    # 1. 黑曜金华 (High Contrast Luxury Gold Theme)
    "obsidian_gold": """
        QMainWindow { background-color: #08080A; }
        QWidget { color: #E4E4E9; font-family: "PingFang SC", "-apple-system", "SF Pro SC", "Microsoft YaHei", sans-serif; font-size: 13px; }
        
        /* 强制覆盖子页面与Tab容器的背景，防止系统白色底色溢出 */
        ShortcutPage, BodyClassifierPage, QTabWidget, QTabWidget::pane { 
            background-color: transparent !important; 
            background: transparent !important;
            border: none !important;
        }
        
        QFrame#CardFrame { background-color: #131318; border: 1.5px solid rgba(229, 195, 101, 0.15); border-radius: 16px; }
        QFrame#SeparatorLine { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(229, 195, 101, 0.35), stop:0.5 rgba(229, 195, 101, 0.05), stop:1 rgba(229, 195, 101, 0.35)); }
        
        QMenuBar { background-color: #08080A; border-bottom: 2px solid rgba(229, 195, 101, 0.25); color: #A1A1AA; font-weight: 600; }
        QMenuBar::item { background: transparent; padding: 10px 20px; }
        QMenuBar::item:selected { background: rgba(229, 195, 101, 0.12); color: #E5C365; border-radius: 6px; }
        
        QMenu { background-color: #131318; border: 1.5px solid rgba(229, 195, 101, 0.3); border-radius: 10px; color: #E4E4E9; padding: 6px; }
        QMenu::item { padding: 8px 24px; border-radius: 6px; }
        QMenu::item:selected { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E5C365, stop:1 #B8860B); color: #08080A; font-weight: bold; }
        
        QTabBar { background-color: #131318; border-radius: 12px; padding: 4px; border: 1px solid rgba(255, 255, 255, 0.05); }
        QTabBar::tab { background: transparent; color: #8E8E93; border-radius: 8px; padding: 10px 24px; font-weight: bold; }
        QTabBar::tab:selected { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #E5C365, stop: 1 #B8860B); color: #08080A; }
        
        QLineEdit { background-color: #0A0A0D; border: 1.5px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 10px 14px; color: #FFFFFF; }
        QLineEdit:focus { border: 1.5px solid #E5C365; background-color: #121217; }
        
        QPushButton { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2A2A33, stop: 1 #1C1C22); border: 1.5px solid rgba(255, 255, 255, 0.1); border-radius: 8px; color: #E4E4E9; font-weight: bold; height: 32px; }
        QPushButton:hover { background: #33333E; border-color: #E5C365; color: #FFFFFF; }
        QPushButton#GoldActionButton { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #FBE395, stop: 1 #B8860B); border: none; border-radius: 10px; color: #08080A; font-weight: 800; font-size: 14px; }
        
        QTextEdit { background-color: #09090C; border: 1px solid rgba(255, 255, 255, 0.04); border-radius: 12px; color: #D4D4D8; }
        QListWidget { background-color: #09090C; border: 1px solid rgba(255, 255, 255, 0.04); border-radius: 10px; }
        QListWidget::item { background-color: rgba(255, 255, 255, 0.02); color: #D4D4D8; border-radius: 6px; margin-bottom: 4px; padding: 8px; }
        QListWidget::item:selected { background: rgba(229, 195, 101, 0.15); color: #FBE395; border: 1.5px solid #E5C365; }
        
        QProgressBar { border: none; background-color: rgba(255, 255, 255, 0.05); border-radius: 6px; text-align: right; color: #FFFFFF; font-weight: bold; }
        QProgressBar::chunk { background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #E5C365, stop:1 #B8860B); border-radius: 6px; }
        QSpinBox { background-color: #0A0A0D; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 6px; padding: 5px; color: #FFFFFF; }
        QCheckBox { color: #E4E4E9; font-weight: bold; }
        QDialog { background-color: #131318; border: 1.5px solid #E5C365; }
    """,

    # 2. 冰晶海蓝 (Optimized Apple Style Light Blue Theme)
    "ice_blue": """
        QMainWindow { background-color: #EAF0F6; }
        QWidget { color: #0F172A; font-family: "PingFang SC", "-apple-system", "SF Pro SC", "Microsoft YaHei", sans-serif; font-size: 13px; }
        
        /* 消除背景溢白 */
        ShortcutPage, BodyClassifierPage, QTabWidget, QTabWidget::pane { 
            background-color: transparent !important; 
            background: transparent !important;
            border: none !important;
        }
        
        QFrame#CardFrame { background-color: #FFFFFF; border: 1.5px solid rgba(2, 132, 199, 0.22); border-radius: 16px; }
        QFrame#SeparatorLine { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(2, 132, 199, 0.4), stop:0.5 rgba(2, 132, 199, 0.08), stop:1 rgba(2, 132, 199, 0.4)); }
        
        QMenuBar { background-color: #EAF0F6; border-bottom: 2px solid #0284C7; color: #0F172A; font-weight: 600; }
        QMenuBar::item { background: transparent; padding: 10px 20px; }
        QMenuBar::item:selected { background: rgba(2, 132, 199, 0.1); color: #0369A1; border-radius: 6px; }
        
        QMenu { background-color: #FFFFFF; border: 2px solid #0284C7; border-radius: 10px; color: #0F172A; padding: 6px; }
        QMenu::item { padding: 8px 24px; border-radius: 6px; }
        QMenu::item:selected { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #38BDF8, stop:1 #0284C7); color: #FFFFFF; font-weight: bold; }
        
        QTabBar { background-color: #D1DBE6; border-radius: 12px; padding: 4px; border: 1px solid rgba(0, 0, 0, 0.05); }
        QTabBar::tab { background: transparent; color: #475569; border-radius: 8px; padding: 10px 24px; font-weight: bold; }
        QTabBar::tab:selected { background: #FFFFFF; color: #0284C7; }
        
        QLineEdit { background-color: #F1F5F9; border: 1.5px solid rgba(2, 132, 199, 0.25); border-radius: 8px; padding: 10px 14px; color: #0F172A; }
        QLineEdit:focus { border: 2px solid #0284C7; background-color: #FFFFFF; }
        
        QPushButton { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FFFFFF, stop: 1 #F1F5F9); border: 1.5px solid rgba(2, 132, 199, 0.35); border-radius: 8px; color: #0284C7; font-weight: bold; height: 32px; }
        QPushButton:hover { background: #E2E8F0; border-color: #0369A1; color: #0369A1; }
        QPushButton#GoldActionButton { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #38BDF8, stop: 1 #0284C7); border: none; border-radius: 10px; color: #FFFFFF; font-weight: bold; font-size: 14px; }
        
        QTextEdit { background-color: #F8FAFC; border: 1.5px solid rgba(2, 132, 199, 0.15); border-radius: 12px; color: #0F172A; }
        QListWidget { background-color: #F8FAFC; border: 1.5px solid rgba(2, 132, 199, 0.15); border-radius: 10px; }
        QListWidget::item { background-color: rgba(255, 255, 255, 0.9); color: #0F172A; border-radius: 6px; margin-bottom: 4px; padding: 8px; border: 1px solid rgba(0, 0, 0, 0.05); }
        QListWidget::item:selected { background: rgba(2, 132, 199, 0.15); color: #0369A1; border: 1.5px solid #0284C7; }
        
        QProgressBar { border: none; background-color: rgba(0, 0, 0, 0.05); border-radius: 6px; text-align: right; color: #0F172A; font-weight: bold; }
        QProgressBar::chunk { background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #38BDF8, stop:1 #0284C7); border-radius: 6px; }
        QSpinBox { background-color: #FFFFFF; border: 1.5px solid rgba(2, 132, 199, 0.25); border-radius: 6px; padding: 5px; color: #0F172A; }
        QCheckBox { color: #0F172A; font-weight: bold; }
        QDialog { background-color: #FFFFFF; border: 1.5px solid #0284C7; }
    """,

    # 3. 帕特农神庙 (Athens Marble Textured Theme - Real Sandstone feel)
    "athens_marble": """
        QMainWindow { background-color: #ECE5D8; }
        QWidget { color: #433D35; font-family: "PingFang SC", "-apple-system", "SF Pro SC", "Microsoft YaHei", sans-serif; font-size: 13px; }
        
        /* 消除背景溢白 */
        ShortcutPage, BodyClassifierPage, QTabWidget, QTabWidget::pane { 
            background-color: transparent !important; 
            background: transparent !important;
            border: none !important;
        }
        
        QFrame#CardFrame { 
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FAF7F2, stop:0.4 #F4ECE0, stop:0.8 #EDE3D0, stop:1 #E5D6BD); 
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #C2B095, stop:1 #806A50);
            border-radius: 16px; 
        }
        QFrame#SeparatorLine { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(144, 115, 80, 0.4), stop:0.5 rgba(144, 115, 80, 0.08), stop:1 rgba(144, 115, 80, 0.4)); }
        
        QMenuBar { background-color: #ECE5D8; border-bottom: 2px solid #806A50; color: #433D35; font-weight: 600; }
        QMenuBar::item { background: transparent; padding: 10px 20px; }
        QMenuBar::item:selected { background: rgba(128, 106, 80, 0.12); color: #806A50; border-radius: 6px; }
        
        QMenu { background-color: #FAF7F2; border: 2px solid #806A50; border-radius: 10px; color: #433D35; padding: 6px; }
        QMenu::item { padding: 8px 24px; border-radius: 6px; }
        QMenu::item:selected { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #C2B095, stop:1 #806A50); color: #FAF7F2; font-weight: bold; }
        
        QTabBar { background-color: #DCD4C4; border-radius: 12px; padding: 4px; border: 1px solid rgba(0, 0, 0, 0.08); }
        QTabBar::tab { background: transparent; color: #5C5446; border-radius: 8px; padding: 10px 24px; font-weight: bold; }
        QTabBar::tab:selected { background: #FAF7F2; color: #806A50; border: 1px solid #C2B095; }
        
        QLineEdit { background-color: #F7F3EB; border: 1.5px solid rgba(128, 106, 80, 0.3); border-radius: 8px; padding: 10px 14px; color: #433D35; }
        QLineEdit:focus { border: 2px solid #806A50; background-color: #FAF7F2; }
        
        QPushButton { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAF7F2, stop: 1 #ECE5D8); border: 1.5px solid #C2B095; border-radius: 8px; color: #5C5446; font-weight: bold; height: 32px; }
        QPushButton:hover { background: #DFD7C7; border-color: #806A50; color: #433D35; }
        QPushButton#GoldActionButton { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #D4C1A5, stop: 1 #806A50); border: 1.5px solid #C2B095; border-radius: 10px; color: #FAF7F2; font-weight: bold; font-size: 14px; }
        
        QTextEdit { background-color: #FAF7F2; border: 1.5px solid rgba(128, 106, 80, 0.2); border-radius: 12px; color: #433D35; }
        QListWidget { background-color: #FAF7F2; border: 1.5px solid rgba(128, 106, 80, 0.2); border-radius: 10px; }
        QListWidget::item { background-color: rgba(128, 106, 80, 0.05); color: #433D35; border-radius: 6px; margin-bottom: 4px; padding: 8px; }
        QListWidget::item:selected { background: rgba(128, 106, 80, 0.15); color: #806A50; border: 1.5px solid #806A50; }
        
        QProgressBar { border: none; background-color: rgba(128, 106, 80, 0.1); border-radius: 6px; text-align: right; color: #433D35; font-weight: bold; }
        QProgressBar::chunk { background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #D4C1A5, stop:1 #806A50); border-radius: 6px; }
        QSpinBox { background-color: #FAF7F2; border: 1.5px solid rgba(128, 106, 80, 0.3); border-radius: 6px; padding: 5px; color: #433D35; }
        QCheckBox { color: #5C5446; font-weight: bold; }
        QDialog { background-color: #FAF7F2; border: 2px solid #806A50; }
    """
}

# ==================== 苹果拟物风格“关于”窗口（已修复截断问题） ====================
class AboutDialog(QDialog):
    def __init__(self, parent=None, current_theme_qss=""):
        super().__init__(parent)
        self.setWindowTitle("关于 ToolBox")
        self.setFixedSize(500, 380)  # 扩大高宽上限，确保充足的空间
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setStyleSheet(current_theme_qss)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        card = QFrame()
        card.setObjectName("CardFrame")
        
        card_shadow = QGraphicsDropShadowEffect(self)
        card_shadow.setBlurRadius(20)
        card_shadow.setYOffset(4)
        card_shadow.setColor(QColor(0, 0, 0, 70))
        card.setGraphicsEffect(card_shadow)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 22, 24, 22)
        card_layout.setAlignment(Qt.AlignCenter)
        card_layout.setSpacing(10)

        logo = QLabel("🧰")
        logo.setStyleSheet("font-size: 42px; margin-bottom: 2px;")
        
        title = QLabel("ToolBox 管理器 Pro")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        version = QLabel("Enterprise Release v2.8 (Build 2024.11)")
        version.setStyleSheet("opacity: 0.6; font-size: 11px;")

        # 将文案换行调整，彻底预防截断
        desc = QLabel("By:BadPig QQ:3629202342 基于AI创作")
        desc.setAlignment(Qt.AlignCenter)
        desc.setWordWrap(True)
        desc.setStyleSheet("font-size: 12px; line-height: 20px; margin-top: 6px; padding: 0 5px;")

        card_layout.addWidget(logo, 0, Qt.AlignCenter)
        card_layout.addWidget(title, 0, Qt.AlignCenter)
        card_layout.addWidget(version, 0, Qt.AlignCenter)
        card_layout.addWidget(desc, 0, Qt.AlignCenter)

        btn_ok = QPushButton("确定")
        btn_ok.setFixedSize(140, 36)  # 从容的宽阔物理按钮
        btn_ok.setCursor(Qt.PointingHandCursor)
        btn_ok.clicked.connect(self.accept)

        layout.addWidget(card)
        layout.addWidget(btn_ok, 0, Qt.AlignCenter)

# ==================== 主窗口集成控制 ====================
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToolBox 管理器 Pro")
        self.resize(1300, 920)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.current_theme_key = "obsidian_gold"
        
        self.init_ui()
        self.set_style("obsidian_gold") # 引导高奢黑金默认样式

    def init_ui(self):
        menubar = self.menuBar()
        
        # 精致的“主题”控制器菜单
        theme_menu = menubar.addMenu("  主题 (Themes)  ")
        theme_actions = [
            ("✨ 黑曜金华高阶暗色", "obsidian_gold"),
            ("💎 冰晶海蓝极致对比", "ice_blue"),
            ("🏛️ 雅典卫城大理石质感", "athens_marble")
        ]
        
        for name, key in theme_actions:
            action = QAction(name, self)
            action.triggered.connect(lambda checked, k=key: self.set_style(k))
            theme_menu.addAction(action)

        about_menu = menubar.addMenu("  帮助  ")
        about_action = QAction("关于", self)
        about_action.triggered.connect(self.show_about)
        about_menu.addAction(about_action)

        container_layout = QVBoxLayout(self.central_widget)
        container_layout.setContentsMargins(24, 20, 24, 24)
        container_layout.setSpacing(0)

        self.tabs = QTabWidget()
        self.shortcut_page = ShortcutPage()
        self.body_classifier_page = BodyClassifierPage()
        
        self.tabs.addTab(self.shortcut_page, "相对路径快捷方式")
        self.tabs.addTab(self.body_classifier_page, "身体部位分类")

        container_layout.addWidget(self.tabs)

    def set_style(self, key):
        self.current_theme_key = key
        qss = THEMES.get(key, "")
        self.setStyleSheet(qss)
        self.apply_button_shadows()

    def apply_button_shadows(self):
        buttons = [
            self.shortcut_page.btn_create,
            self.body_classifier_page.btn_start
        ]
        
        if self.current_theme_key == "ice_blue":
            shadow_color = QColor(2, 132, 199, 90)
        elif self.current_theme_key == "athens_marble":
            shadow_color = QColor(128, 106, 80, 110)
        else:
            shadow_color = QColor(0, 0, 0, 150)
            
        for btn in buttons:
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(20)
            shadow.setXOffset(0)
            shadow.setYOffset(6)
            shadow.setColor(shadow_color)
            btn.setGraphicsEffect(shadow)

    def show_about(self):
        about_dialog = AboutDialog(self, THEMES[self.current_theme_key])
        about_dialog.exec_()
