from .ui_window import UIWindow
from .widgets.pie_chart import PieChart
from .dialogs.new_account import NewAccountDialog
from .dialogs.accounts_filter import AccountsFilterDialog


class MainWindow(UIWindow):
    """Основное окно приложения.

    *Файл интерфейса:* ``ui/main.ui``
    """

    ui_path = 'ui/main.ui'

    def __init__(self, user):
        super().__init__()

        self.user = user
        self.checked_accounts = []

        self.add_account_btn.clicked.connect(self.show_add_account_dialog)
        self.accounts_filter_btn.clicked.connect(self.show_accounts_filter_dialog)

        PieChart(self.pie_place, self.checked_accounts)

    def show_add_account_dialog(self):
        self.add_account_dialog = NewAccountDialog(self.user, self.checked_accounts)
        self.add_account_dialog.exec()

    def show_accounts_filter_dialog(self):
        self.accounts_filter_dialog = AccountsFilterDialog(self.user, self.checked_accounts)
        self.accounts_filter_dialog.exec()
        self.checked_accounts = self.accounts_filter_dialog.get_checked_accounts()
